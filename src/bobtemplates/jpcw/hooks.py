#!/usr/bin/env python
# -*- coding: utf-8 -*-

"""Render bobtemplates.jpcw hooks.
"""

__docformat__ = 'restructuredtext en'

try:
    import urllib.request as urllib2
except ImportError:
    import urllib2

import getpass
import os

from datetime import date

from mrbob.bobexceptions import ValidationError


def basicnamespace_pre_pkg_ns(configurator, question):
    """Guess default pkg_ns from Output Directory"""
    names = configurator.target_directory.split(os.sep)[-1].split('.')
    if len(names) == 2:
        question.default = names[0]


def basicnamespace_pre_pkg_project(configurator, question):
    """Guess default pkg_project from Output Directory"""
    names = configurator.target_directory.split(os.sep)[-1].split('.')
    if len(names) == 2:
        question.default = names[1]


def basicnamespace_pre_dcvs_nick(configurator, question):
    """Guess default pkg_project from Output Directory"""
    question.default = getpass.getuser()


def valid_pkg_license(configurator, question, answer):
    """Check license answer."""
    licenses = ['BSD', 'GPL']
    if answer.upper().strip() not in licenses:
        raise ValidationError("'{0}' is not in {1}".format(answer, licenses))
    return answer



def basic_namespace_pre_render(configurator):
    """License stuff."""
    configurator.variables.update({'year': date.today().year})
    if configurator.variables['pkg_license'].lower() == 'gpl':
        configurator.variables.update({'gpl': 'y'})
    else:
        configurator.variables.update({'gpl': 'n'})


def basic_namespace_post_render(configurator):
    """Nothing yet."""

    if configurator.variables['pkg_license'].lower() == 'gpl':
        configurator.variables.update({'gpl': 'y'})
    else:
        configurator.variables.update({'gpl': 'n'})


def basic_namespace_post_render(configurator):
    """
    Execute post renderer hook.
    """
    if configurator.variables['buildout_bootstrap']:
        get_bootstrap(configurator)

def get_bootstrap(configurator):
    """
    Get the last version of bootstrap.py
    """
    url = 'http://downloads.buildout.org/2/bootstrap.py'
    req = urllib2.urlopen(url)

    with open(os.path.join(configurator.target_directory, 'boostrap.py'), 'w') as bootstrap:
        bootstrap.write(str(req.read()))

# vim:set et sts=4 ts=4 tw=80:
