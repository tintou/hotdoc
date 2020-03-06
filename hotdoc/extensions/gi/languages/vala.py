# -*- coding: utf-8 -*-
#
# Copyright 2020 Collabora Ltd
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

"""Vala language support for Hotdoc

This extension provides support for providing documentation in Vala
"""

from hotdoc.extensions.gi.language import *
from hotdoc.extensions.gi.utils import *
from hotdoc.core.links import Link

# FIXME: Avoid the use of a global dictionary
TRANSLATED = {}

class ValaLanguage(Language):
    language_name = 'vala'

    def __init__(self):
        Language.__init__(self)
        self._create_fundamentals();

    def _create_fundamentals(self):
        char_link = \
                Link('https://valadoc.org/glib-2.0/char.html',
                    'char', None)
        uchar_link = \
                Link('https://valadoc.org/glib-2.0/uchar.html',
                    'uchar', None)
        string_link = \
                Link('https://valadoc.org/glib-2.0/string.html',
                    'string', None)
        boolean_link = \
                Link('https://valadoc.org/glib-2.0/bool.html',
                        'bool', None)
        true_link = \
                Link('https://www.vala-project.org/doc/vala/Expressions.html#Literal_expressions',
                    'true', None)
        false_link = \
               Link('https://www.vala-project.org/doc/vala/Expressions.html#Literal_expressions',
                    'false', None)
        pointer_link = \
                Link('https://valadoc.org/glib-2.0/GLib.pointer.html',
                    'GLib.pointer', None)
        integer_link = \
                Link('https://valadoc.org/glib-2.0/int.html',
                        'int', None)
        unsigned_integer_link = \
                Link('https://valadoc.org/glib-2.0/uint.html',
                        'uint', None)
        integer8_link = \
                Link('https://valadoc.org/glib-2.0/int8.html',
                        'int8', None)
        unsigned_integer8_link = \
                Link('https://valadoc.org/glib-2.0/uint8.html',
                        'uint8', None)
        integer16_link = \
                Link('https://valadoc.org/glib-2.0/int16.html',
                        'int16', None)
        unsigned_integer16_link = \
                Link('https://valadoc.org/glib-2.0/uint16.html',
                        'uint16', None)
        integer32_link = \
                Link('https://valadoc.org/glib-2.0/int32.html',
                        'int32', None)
        unsigned_integer32_link = \
                Link('https://valadoc.org/glib-2.0/uint32.html',
                        'uint32', None)
        integer64_link = \
                Link('https://valadoc.org/glib-2.0/int64.html',
                        'int64', None)
        unsigned_integer64_link = \
                Link('https://valadoc.org/glib-2.0/uint64.html',
                        'uint64', None)
        float_link = \
                Link('https://valadoc.org/glib-2.0/float.html',
                        'float', None)
        double_link = \
                Link('https://valadoc.org/glib-2.0/double.html',
                        'double', None)
        long_link = \
                Link('https://valadoc.org/glib-2.0/long.html',
                        'long', None)
        ulong_link = \
                Link('https://valadoc.org/glib-2.0/ulong.html',
                        'ulong', None)
        none_link = \
                Link('https://www.vala-project.org/doc/vala/Expressions.html#Literal_expressions',
                        'null', None)
        list_link = \
                Link('https://valadoc.org/glib-2.0/GLib.List.html',
                     'GLib.List', None)
        gtype_link = \
                Link('https://valadoc.org/gobject-2.0/GLib.Type.html',
                        'GLib.Type', None)
        gvariant_link = \
                Link('https://valadoc.org/glib-2.0/GLib.Variant.html',
                        'GLib.Variant', None)
        gsize_link = \
                Link('https://valadoc.org/glib-2.0/size_t.html',
                        'GLib.size_t', None)
        gssize_link = \
                Link('https://valadoc.org/glib-2.0/ssize_t.html',
                        'GLib.ssize_t', None)

        self.fundamentals = {
                "none": none_link,
                "gpointer": pointer_link,
                "gconstpointer": pointer_link,
                "gboolean": boolean_link,
                "gint8": integer8_link,
                "guint8": unsigned_integer8_link,
                "gint16": integer16_link,
                "guint16": unsigned_integer16_link,
                "gint32": integer_link,
                "guint32": unsigned_integer_link,
                "gchar": char_link,
                "guchar": uchar_link,
                "gshort": integer_link,
                "gushort": unsigned_integer_link,
                "gint": integer_link,
                "guint": unsigned_integer_link,
                "gfloat": float_link,
                "gdouble": double_link,
                "GLib.List": list_link,
                "utf8": string_link,
                "gunichar": string_link,
                "filename": string_link,
                "gchararray": string_link,
                "GType": gtype_link,
                "GVariant": gvariant_link,
                "gsize": gsize_link,
                "gssize": gssize_link,
                "goffset": integer_link,
                "gintptr": integer_link,
                "guintptr": integer_link,
                "glong": long_link,
                "gulong": ulong_link,
                "gint64": integer64_link,
                "guint64": unsigned_integer64_link,
                "TRUE": true_link,
                "FALSE": false_link,
                "NULL": none_link,
        }

    def make_translations(self, unique_name, node):
        if node.attrib.get('introspectable') == '0':
            return

        if node.tag == core_ns('member'):
            components = get_gi_name_components(node)
            components[-1] = components[-1].upper()
            gi_name = '.'.join(components)
            TRANSLATED[unique_name] = 'member %s' % gi_name
        elif c_ns('identifier') in node.attrib:
            components = get_gi_name_components(node)
            if node.tag == core_ns('method'):
                TRANSLATED[unique_name] = components[-1]
            else:
                gi_name = '.'.join(components)
                TRANSLATED[unique_name] = 'identifier %s' % gi_name
        elif c_ns('type') in node.attrib:
            components = get_gi_name_components(node)
            gi_name = '.'.join(components)
            TRANSLATED[unique_name] = 'type %s' % gi_name
        elif node.tag == core_ns('field'):
            components = []
            get_field_c_name_components(node, components)
            display_name = '.'.join(components[1:])
            TRANSLATED[unique_name] = 'field %s' % display_name
        elif node.tag == core_ns('virtual-method'):
            display_name = node.attrib['name']
            TRANSLATED[unique_name] = 'virtual %s' % display_name
        elif node.tag == core_ns('property'):
            display_name = node.attrib['name']
            TRANSLATED[unique_name] = 'property %s' % display_name.replace('-', '_')
        elif node.tag == glib_ns('signal'):
            components = get_gi_name_components(node)
            TRANSLATED[unique_name] = components[-1]
        else:
            TRANSLATED[unique_name] = 'other (%s) %s' % (node.tag, node.attrib.get('name'))

    def get_translation(self, unique_name):
        return TRANSLATED.get (unique_name)

def get_language_classes():
    """Nothing important, really"""
    return [ValaLanguage]
