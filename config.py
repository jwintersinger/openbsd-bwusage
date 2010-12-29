import os

# Can't set PATH to os.path.expanduser('~/.openbsd-bwusage/'), as when running
# from cron, the path will expand to /var/log/.openbsd-bwusage/.
PATH = '/root/.openbsd-bwusage/'
DEBUG = False
