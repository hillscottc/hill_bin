""" From http://www.yaconiello.com/blog/deploying-django-site-fabric/
"""
from __future__ import with_statement
import os
from fabric.api import local, abort, env
from fabric.contrib.files import append

env.hosts = ['scott@scotts-imac']

# env.directory = '/home/shill/dev/obi_django'

# HOME = "/home/shill"
HOME = "/Users/scott"

VENV_ROOT = os.path.join(HOME, 'virtualenvs')
DEV_ROOT = os.path.join(HOME, 'dev')
#
#
# def _bash_wrap(cmd):
#     """Calls that require my bashrc need this to work.
#     Usage: local(_wrap_local("mkvirtualenv foo"))
#     Output: [localhost] local: /bin/bash -l -c 'mkvirtualenv foo'
#     """
#     return "/bin/bash -l -c '{}'".format(cmd)
#
#
# def build_venv(name=None, venv_root=None):
#     """Create (if neccesary) given virtual environment via 'mkvirtualenv'.
#     """
#     usage = "Usage: fab build_venv:myproj"
#
#     if not name:
#         abort(usage)
#
#     if not venv_root:
#         venv_root = VENV_ROOT
#
#     if not os.path.isdir(venv_root):
#         abort("Invalid venv_root %s" % venv_root)
#
#     if os.path.isdir(os.path.join(venv_root, name)):
#         print("Virtual environment already exists.")
#     else:
#         local(_bash_wrap("mkvirtualenv {}".format(name)))
#
#     config_venv(name)


def config_venv(venv_name):
    """Config venv postactivate and postdeactivate.
    """
    print("ok")
    ## Append to POST-ACTIVATE script.
    append(os.path.join(VENV_ROOT, venv_name, 'bin', 'postactivate'),
           os.linesep.join([
               "export OLD_PATH=$PATH",
               "export OLD_PYTHONPATH=$PYTHONPATH",
               "export OLD_DJANGO_SETTINGS_MODULE=$DJANGO_SETTINGS_MODULE",
               "export PATH={}:{}:$PATH".format(DEV_ROOT, os.path.join(DEV_ROOT, venv_name)),
               "export PYTHONPATH={}:{}:$PYTHONPATH".format(DEV_ROOT, os.path.join(DEV_ROOT, venv_name)),
               "export DJANGO_SETTINGS_MODULE={}.settings".format(venv_name),
               "cd {}".format(os.path.join(DEV_ROOT, venv_name)),
           ]))
    #
    # ## Append to POST-DE-ACTIVATE script.
    # append(os.path.join(VENV_ROOT, venv_name, 'bin', 'postdeactivate'),
    #        os.linesep.join([
    #            "export PATH=$OLD_PATH",
    #            "export PYTHONPATH=$OLD_PYTHONPATH",
    #            "export DJANGO_SETTINGS_MODULE=$OLD_DJANGO_SETTINGS_MODULE",
    #            "cd $HOME",
    #        ]))


def hello(name="world"):
    print("Hello there %s!, printed." % name)
    local("echo Hello %s!, echoed." % name)



