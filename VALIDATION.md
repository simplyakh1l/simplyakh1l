# Review validation

Validated 10 November 2026.

- Rendered the README through GitHub's authenticated Markdown API in GFM mode.
  GitHub preserves the picture/source elements, navigation links, tables, and images.
- Viewed the resulting HTML with GitHub Markdown CSS at 1014px desktop and 390px
  mobile widths, plus desktop light mode. All ten displayed images loaded;
  there were no JavaScript errors or page-level horizontal overflow.
- Parsed every SVG as XML and checked every relative image/source path on disk.
- Validated contribution totals against the daily API calendar. Tested that an
  authentication failure leaves the prior snapshot untouched.
- Parsed the workflow YAML and checked the GitHub token expression. The scheduled
  workflow activates on main only and proposes updates through a PR; it was not
  run before merge. Repository permission to let Actions create PRs is required.
- GitHub links point to inspected repositories. Public LinkedIn, LeetCode, and
  email links were provided by the profile owner. No Codeforces handle was guessed.
- No external image widgets are loaded. Local activity assets remain visible if
  refresh fails, with a dated window and a direct live-calendar text fallback.
- The review branch contains only profile files. No project repository was edited.

The profile itself appears only after the owner merges the review PR into main.
