# ISM2411 — Python for Business

**Name:** Lucas Barrett

**Semester:** Fall 2026

## About This Repo

This repository contains my weekly lab submissions for ISM2411. Each weekly folder contains work for the corresponding module.

## Modules

- `week07/` — Functions: calculate_tax, apply_discount, and final_price; sales debugging; and variable scope.
- Module 8 — Git and GitHub workflow, repository setup, and reflection in this README.

## How to Run

Install Python 3, open a terminal in the repository root, and run:

```sh
python week07/functions.py
```

The script prints tax and discount examples, final order prices, the corrected sales total and count, and a variable scope demonstration. It requires no additional packages.

## Reflection

### 1. Commit history and work habits

Output of `git log --oneline` before this reflection commit:

```text
b6f1932 add README with module listing and run instructions
b045cbe add module 7 functions: calculate_tax, apply_discount, final_price
c622b6d Add .gitignore for Python and OS filesadd .gitignore for Python and OS files
b285aca Initial commit
```

The separate commits show focused changes: setting up exclusions, adding the Module 7 script, and documenting the repository. A hiring reviewer could inspect what each change accomplished and reverse a specific change without untangling unrelated edits. The first message contains duplicated wording, which reminds me to review commit messages before saving them.

### 2. How Git changes my editing process

Git should help me make small, focused edits and test the script before committing each working change. Instead of overwriting my only working copy, I can review the differences and restore an earlier version if an edit introduces a bug. I should also push completed commits so the version on GitHub matches the work I intend to submit.

### 3. An additional exclusion

I added `.venv/` for a local Python virtual environment, beyond the starter exclusions. It contains installed packages and machine-specific executables that can be recreated, so tracking it would add unnecessary files and could cause problems on another computer.

*AI assistance: I used ChatGPT to help organize this repository and draft its documentation and reflection.*
