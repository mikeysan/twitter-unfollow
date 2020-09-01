# Merge Original Repository into Fork

If you're like me, you've probably seen a project that you like and forked it only to forget about it months later.

Suddenly, you're going through your repos and stumble on it again. You then go down the rabbit hole of checking the original link.

To your utter horror, they moved on and left you behind. In the blink of an eye, you're carrying old news. The repo has left you behind.

What do you do next? Well, first, agdin if you're like me, you click through Github trying to figure out a way to get your forked project up to date. Next, you probably hit Google (or in my case, DuckDuckGo). 

You find mentions of what could be done to 'fix' things, but nothing that says "start here", "end here". Just one or two liners about oh just clone it again and then push it your repo.

By the time your make sense of what they are talking about, given that we are new to Github, we lose interest and move on.

Weeks and months later, you come across another project that has suffered the same fate, so you repeat the cycle.

Well, today I had another experience of this and said enough is enough.

### The Problem

**This branch is 6 commits behind fakename:master.**

### The Solution

- You will need git installed and set up on your system. A good place to start is the [Git website](https://git-scm.com/downloads)
- Launch a terminal (Mac) or Command Prompt (Windows).
- Navigate to the folder containing the project (or create a new folder and cd to it)
- Clone your forked project (the one from your account) if it's not already on your system using (origin):
`git clone https://github.com/Your-Username/Forked-Repo.git`
- Next add a reference to the original project (upstream) using:
`git remote add upstream https://github.com/Original-Owner/Original-Repo].git`
- Run `git remote -v` to confirm you can see both repos, yours (origin) and original (upstream).
- Next get the files from upstream:
`git fetch upstream`
- Before we merge any changes, let's make sure we're on our (fork) master branch:
`git checkout master`
- Now we can merge changes from upstream/master (original author) to local (fork)
`git merge upstream/master`
- Finally, we push those changes to GitHub
`git push origin master`