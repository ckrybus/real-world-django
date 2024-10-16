# Real World Django

> Real World Django applications and their open source codebases for developers to learn from

This project brings 30+ (and growing) active, open source Django applications together in one
repository, making it easier for developers to download the collected codebases and learn
from Django apps written by experienced developers. Reading open source code can be an invaluable
learning aid. You&rsquo;ll find the source code in the [`apps/`](apps/) subdirectory.

## Real World Django Applications

{APPS_LIST}

## How to install on your computer

Make sure you have enough free disk space available. Currently ~12GB are needed.

```bash
# Clone this git repo:
git clone git@github.com:ckrybus/real-world-django.git

cd real-world-django/

# The Django apps are linked to as git submodules.
# This will take some time...(see comment below for possible speedup)
git submodule update --init

# OR If you've got git 2.9+ installed try to run updates in parallel:
# git submodule update --init --jobs 4
```

## Other Real World Codebase Collections

- Real world React apps https://github.com/jeromedalbert/real-world-react-apps
- Real World Rails https://github.com/eliotsykes/real-world-rails
- Real World React Native https://github.com/jeromedalbert/real-world-react-native
- Real World Ruby Apps https://github.com/jeromedalbert/real-world-ruby-apps
- Real World Phoenix https://github.com/szTheory/real-world-phoenix
- Real World Sinatra https://github.com/jeromedalbert/real-world-sinatra
- Real World Elixir Apps https://github.com/szTheory/real-world-elixir-apps
- Real World Ember https://github.com/eliotsykes/real-world-ember
- Real World RSpec https://github.com/pirj/real-world-rspec

Know any others? Please open a PR and add the link here

## Information for Contributors

### Is your app the right fit?

- The vast majority of the codebase should be written in Python and use Django as framework.
- Some projects are monorepos and use Django only as backend/API, those are allowed too.
- Only standalone django projects are accepted, no single "django apps" or python libraries.
  If in order to run a project you first need to add it to INSTALLED_APPS then it does not meet
  the criteria.
- The app should be somewhat popular and active, in order to limit the apps in this repo
  to a manageable amount. There is some leeway in what constitutes a popular
  app. A possible indicator can be GitHub stars compared to similar apps.

Don't hesitate to submit a pull request if you meet the criteria!

### How to add a Real World Django app

Given a GitHub repo for a Django app `githubuser/foo`:

```bash
# Inside the project root:
git submodule add -b default_branchname git@github.com:githubuser/foo.git apps/foo
```

### Updating the Django apps submodules to latest

The Django apps in `apps/` are git submodules. Git submodules are locked to a revision
and don't stay in sync with the latest revision.

To update the revisions, run:

```bash
# This will take some time:
git submodule foreach git pull
```

---

## Contributors

- Contributions are welcome, fork the GitHub repo, make your changes, then
  submit your pull request! Reach out if you'd like some help.
