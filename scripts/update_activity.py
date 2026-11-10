"""Generate local, dated SVGs from GitHub's authenticated contribution calendar.
No third-party widget, private contribution details, or fabricated fallback values.
"""
import datetime as dt
import json
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
QUERY = '''query { user(login: "simplyakh1l") { contributionsCollection { startedAt endedAt contributionCalendar { totalContributions weeks { contributionDays { date contributionCount weekday } } } } } }'''

def fetch():
    import subprocess
    data = json.loads(subprocess.check_output(['gh', 'api', 'graphql', '-f', 'query=' + QUERY], timeout=45))
    if data.get('errors'):
        raise RuntimeError('GitHub GraphQL returned errors; preserving last successful snapshot')
    return data['data']['user']['contributionsCollection']

def render(collection, mobile=False):
    calendar = collection['contributionCalendar']
    weeks = calendar['weeks']
    days = [day for week in weeks for day in week['contributionDays']]
    if not days or not all(isinstance(d['contributionCount'], int) and d['contributionCount'] >= 0 for d in days):
        raise ValueError('Invalid calendar; preserving last successful snapshot')
    total = calendar['totalContributions']
    assert sum(d['contributionCount'] for d in days) == total, 'Calendar totals do not match'
    active = sum(d['contributionCount'] > 0 for d in days)
    peak = max(d['contributionCount'] for d in days)
    width, height = (600, 440) if mobile else (1200, 360)
    recent = weeks[-20:] if mobile else weeks
    step, size = (25, 18) if mobile else (20, 14)
    x0, y0 = (48, 206) if mobile else (70, 180)
    title = 'GitHub activity'
    parts = [f'<svg xmlns="http://www.w3.org/2000/svg" width="{width}" height="{height}" viewBox="0 0 {width} {height}" role="img" aria-labelledby="title desc">', f'<title id="title">{title}</title><desc id="desc">{total} contributions, {active} active days, peak {peak} contributions in one day. From {days[0]["date"]} to {days[-1]["date"]}. Counts follow GitHub contribution rules.</desc>', f'<rect x="1" y="1" width="{width-2}" height="{height-2}" rx="14" fill="#0d1117" stroke="#293549"/>']
    def text(x,y,value,size=14,color='#9eacc1',weight='400'):
        parts.append(f'<text x="{x}" y="{y}" fill="{color}" font-family="Arial,sans-serif" font-size="{size}" font-weight="{weight}">{value}</text>')
    text(32,37,'GITHUB / CONTRIBUTION SNAPSHOT',12,'#78a9ff')
    for x,value,label in zip(([32,220,408] if mobile else [32,400,780]),[total,active,peak],['Contributions','Active days','Most in one day']):
        text(x,89,str(value),34,'#f0f6fc','700'); text(x,116,label,14)
    text(32,160,('Recent 20 weeks' if mobile else 'Past year') + ' · ' + days[-1]['date'],12)
    previous_month = ''
    for i,week in enumerate(recent):
        month = week['contributionDays'][0]['date'][5:7]
        if month != previous_month:
            text(x0+i*step,y0-12,dt.date.fromisoformat(week['contributionDays'][0]['date']).strftime('%b'),10)
            previous_month = month
        for day in week['contributionDays']:
            n = day['contributionCount']; level = 0 if n == 0 else min(4, max(1, (4*n+peak-1)//max(peak,1)))
            color = ['#18202d','#203c63','#315f9c','#5488cc','#8abbff'][level]
            parts.append(f'<rect x="{x0+i*step}" y="{y0+day["weekday"]*step}" width="{size}" height="{size}" rx="3" fill="{color}"><title>{day["date"]}: {n} contributions</title></rect>')
    text(32,height-22,days[0]['date']+' — '+days[-1]['date']+' · GitHub API',11)
    legend_y = height - 52 if mobile else height - 22
    text(width-170,legend_y,'Less',10)
    for i,c in enumerate(['#18202d','#203c63','#315f9c','#5488cc','#8abbff']):
        parts.append(f'<rect x="{width-140+i*16}" y="{legend_y-10}" width="11" height="11" rx="2" fill="{c}"/>')
    text(width-48,legend_y,'More',10)
    parts.append('</svg>')
    return '\n'.join(parts)

def main():
    data = fetch()
    desktop, mobile = render(data), render(data, True)
    # Fetch and validate both variants before replacing any output.
    for name, content in [('activity.svg', desktop), ('activity-mobile.svg', mobile)]:
        target = ROOT / 'assets' / name
        temporary = target.with_suffix('.tmp')
        temporary.write_text(content + '\n')
        temporary.replace(target)
    print('Updated activity assets from GitHub API')

if __name__ == '__main__':
    main()
