# -*- coding: utf-8 -*-
#
# Copyright 2019 Collabora Ltd
#
# This library is free software; you can redistribute it and/or modify it under
# the terms of the GNU Lesser General Public License as published by the Free
# Software Foundation; either version 2.1 of the License, or (at your option)
# any later version.
#
# This library is distributed in the hope that it will be useful, but WITHOUT
# ANY WARRANTY; without even the implied warranty of MERCHANTABILITY or FITNESS
# FOR A PARTICULAR PURPOSE.  See the GNU Lesser General Public License for more
# details.
#
# You should have received a copy of the GNU Lesser General Public License
# along with this library.  If not, see <http://www.gnu.org/licenses/>.

"""C language support for Hotdoc

This extension provides support for providing documentation in C
"""

from hotdoc.extensions.gi.language import *
from hotdoc.extensions.gi.utils import *

class CLanguage(Language):
    language_name = 'c'

    def __init__(self):
        Language.__init__(self)
        self.translated = {}

    def make_translations(self, unique_name, node):
        if node.tag == core_ns('member'):
            self.translated[unique_name] = unique_name
        elif c_ns('identifier') in node.attrib:
            self.translated[unique_name] = unique_name
        elif c_ns('type') in node.attrib:
            self.translated[unique_name] = unique_name
        elif node.tag == core_ns('field'):
            components = []
            get_field_c_name_components(node, components)
            display_name = '.'.join(components[1:])
            self.translated[unique_name] = display_name
        elif node.tag == core_ns('virtual-method'):
            display_name = node.attrib['name']
            self.translated[unique_name] = display_name
        elif node.tag == core_ns('property'):
            display_name = node.attrib['name']
            self.translated[unique_name] = display_name
        else:
            self.translated[unique_name] = node.attrib.get('name')

    def get_translation(self, unique_name):
        return self.translated.get (unique_name)

def get_language_classes():
    """Nothing important, really"""
    return [CLanguage]
