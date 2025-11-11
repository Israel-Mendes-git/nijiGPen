import bpy
# This program is free software; you can redistribute it and/or modify
# it under the terms of the GNU General Public License as published by
# the Free Software Foundation; either version 3 of the License, or
# (at your option) any later version.
#
# This program is distributed in the hope that it will be useful, but
# WITHOUT ANY WARRANTY; without even the implied warranty of
# MERCHANTIBILITY or FITNESS FOR A PARTICULAR PURPOSE. See the GNU
# General Public License for more details.
#
# You should have received a copy of the GNU General Public License
# along with this program. If not, see <http://www.gnu.org/licenses/>.

bl_info = {
    "name" : "nijiGPen",
    "author" : "https://github.com/chsh2/nijiGPen",
    "description" : "A Grease Pencil toolbox for 2D graphic design and illustrations",
    "blender" : (3, 3, 0),
    "version" : (0, 12, 2),
    "location" : "View3D > Sidebar > NijiGP, in specific modes of Grease Pencil objects",
    "doc_url": "https://chsh2.github.io/nijigp/",
    "wiki_url": "https://chsh2.github.io/nijigp/",
    "tracker_url": "https://github.com/chsh2/nijiGPen/issues",
    "category" : "Object"
}

from . import auto_load
from .api_router import register_alternative_api_paths, unregister_alternative_api_paths

auto_load.init()

def register():
    auto_load.register()
    register_alternative_api_paths()
    
    custom_lib_path = bpy.context.preferences.addons[__package__].preferences.custom_lib_path
    if len(custom_lib_path) > 0:
        import sys
        sys.path.append(custom_lib_path)

def unregister():
    auto_load.unregister()
    unregister_alternative_api_paths()
