---
name: agentic-workflows
description: Author, compile, and diagnose GitHub Agentic Workflows in this repository.
---

Keep workflow sources in `.github/workflows/`. Edit the Markdown source and generate the corresponding lock file with `gh aw compile`. Review and commit both files together. Keep repository permissions scoped to the workflow and use safe outputs for GitHub writes. Use `gh aw status` to inspect workflows and `gh aw logs` to investigate runs.

See the [upstream CLI reference](https://github.github.com/gh-aw/setup/cli/) for command options and authentication.
