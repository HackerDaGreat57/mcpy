import sys
from cx_Freeze import setup, Executable

includefiles = []
includes = ['tkinter', 'OpenGL', 'openal']
excludes = []
packages = ['OpenGL']

build_exe_options = {"packages": ["OpenGL", "openal"]}

setup(
    name = 'Minecraft Python Edition',
    version = '0.0.0.7',
    description = 'Minecraft Python Edition',
    author = 'Akshat Singh',
    author_email = 'contact.akshatsingh@gmail.com',
    options = {"build_exe": build_exe_options},
    executables = [Executable('mcpy.py')]
)
