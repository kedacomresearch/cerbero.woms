# cerbero - a multi-platform build system for Open Source software
# Copyright (C) 2012 Andoni Morales Alastruey <ylatuya@gmail.com>
#
# This library is free software; you can redistribute it and/or
# modify it under the terms of the GNU Library General Public
# License as published by the Free Software Foundation; either
# version 2 of the License, or (at your option) any later version.
#
# This library is distributed in the hope that it will be useful,
# but WITHOUT ANY WARRANTY; without even the implied warranty of
# MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the GNU
# Library General Public License for more details.
#
# You should have received a copy of the GNU Library General Public
# License along with this library; if not, write to the
# Free Software Foundation, Inc., 59 Temple Place - Suite 330,
# Boston, MA 02111-1307, USA.

import os

from cerbero.config import Platform
from cerbero.build.cookbook import CookBook
from cerbero.build import recipe
from cerbero.utils import shell


class Recipe1(recipe.Recipe):

    name = 'recipe1'
    licence = 'LGPL'
    uuid = '1'

    files_misc = ['README', 'libexec/gstreamer-0.10/pluginsloader%(bext)s']
    platform_files_misc = {
        Platform.WINDOWS: ['windows'],
        Platform.LINUX: ['linux']}

    files_bins = ['gst-launch']
    platform_files_bins = {
        Platform.WINDOWS: ['windows'],
        Platform.LINUX: ['linux']}

    files_libs = ['libgstreamer-0.10']
    platform_files_libs = {
        Platform.WINDOWS: ['libgstreamer-win32'],
        Platform.LINUX: ['libgstreamer-x11']}


class Recipe2(recipe.Recipe):

    name = 'recipe2'
    licence = 'GPL'

    files_misc = ['README2']


class Recipe3(recipe.Recipe):

    name = 'recipe3'
    licences = 'BSD'

    files_misc = ['README3']


class Recipe4(recipe.Recipe):

    name = 'recipe4'
    licence = 'LGPL'

    files_misc = ['README4']


class Recipe5(recipe.Recipe):

    name = 'recipe5'
    licence = 'LGPL'

    files_libs = ['libtest']


def add_files(tmp):
    bindir = os.path.join(tmp, 'bin')
    libdir = os.path.join(tmp, 'lib')
    gstlibdir = os.path.join(tmp, 'libexec', 'gstreamer-0.10')
    os.makedirs(bindir)
    os.makedirs(libdir)
    os.makedirs(gstlibdir)
    shell.call('touch '
        'windows '
        'linux '
        'README '
        'README2 '
        'README3 '
        'README4 '
        'bin/gst-launch.exe '
        'bin/gst-launch '
        'bin/windows.exe '
        'bin/linux '
        'bin/libgstreamer-0.10.dll '
        'bin/libgstreamer-win32.dll '
        'bin/libtest.dll '
        'lib/libtest.so.1 '
        'lib/libtest.la '
        'lib/libtest.a '
        'lib/libtest.so '
        'lib/libtest.dll.a '
        'lib/libtest.def '
        'lib/test.lib '
        'lib/libgstreamer-0.10.so.1 '
        'lib/libgstreamer-0.10.la '
        'lib/libgstreamer-0.10.a '
        'lib/libgstreamer-0.10.so '
        'lib/libgstreamer-0.10.dll.a '
        'lib/gstreamer-0.10.lib '
        'lib/libgstreamer-0.10.def '
        'lib/libgstreamer-win32.la '
        'lib/libgstreamer-win32.a '
        'lib/libgstreamer-win32.so '
        'lib/libgstreamer-win32.dll.a '
        'lib/gstreamer-win32.lib '
        'lib/libgstreamer-win32.def '
        'lib/libgstreamer-x11.so.1 '
        'lib/libgstreamer-x11.so '
        'lib/libgstreamer-x11.a '
        'lib/libgstreamer-x11.la '
        'libexec/gstreamer-0.10/pluginsloader '
        'libexec/gstreamer-0.10/pluginsloader.exe ',
        tmp)


def create_cookbook(config):
    cb = CookBook(config, False)

    for klass in [Recipe1, Recipe2, Recipe3, Recipe4, Recipe5]:
        cb.add_recipe(klass(config))
    return cb
