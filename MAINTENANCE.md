# Profile maintenance

## Scope and sources

This repository is the profile README for simplyakh1l. Only profile documentation,
SVG assets, and the snapshot refresh workflow belong here.

- Education, CGPA, competition results, Codeforces peak, and 1,500+ solved problems:
  supplied by Akhil Sharma. The problem total is cross-platform, not a repository count.
- LinkedIn, LeetCode, and public email: supplied explicitly for this profile.
- PinPoint: README, package.json, and report/role/agent implementation at
  c7a8e7fdfacc32124574091cd57921493c48a76d. Presented as a Team EXO project.
- Restaurant Menu Management System: main.py and dbconfig.py at
  41d969394bbd0e125884e3549e549939210722c8. Only implemented add/view/delete operations are listed.
- DSA: C++ solutions at 6bf5354d0b3444c43899b39a9a02f04df1684c8b.
- Resume-Categorization-App was inspected but is not featured: its interface names
  other authors, so this profile does not claim sole authorship.
- EventPulse is marked as a fork and is not presented as a separate original project.
- PinPoint artwork is an original conceptual workflow illustration, not a product screenshot.
- Icons are vendored locally; see assets/icons/NOTICE.md.

## Contribution graphic

Run with Python 3 and authenticated GitHub CLI:

    python3 scripts/update_activity.py

The script queries GitHub's contribution calendar and validates daily totals before
writing the desktop and mobile SVGs. The card shows contributions, active days,
and the largest daily contribution count for the dated API window. These are not
commit counts, problem counts, or measures of developer quality. No stars, streaks,
percentiles, language percentages, or other inferred metrics are displayed.

The weekly workflow proposes an asset refresh PR on main; it never merges it.
GitHub Actions must be permitted to create pull requests in repository settings.
If that permission is disabled, the snapshot stays available with its visible date;
run the script manually and submit the assets for review. A failed API request
leaves the previous assets intact. No third-party image widgets are needed.

GitHub determines the page background from the reader's theme. The custom artwork
has its own dark background; all prose uses normal, accessible GitHub Markdown.
The hero and calendar use picture sources for narrow screens. Tables may scroll
within their own bounds on small screens. Essential information and technology
names remain readable when images are blocked.

## Review

Preview README.md on the branch in GitHub. Relative asset paths follow the branch
and continue to work after merge. Do not merge until Akhil approves the design.
