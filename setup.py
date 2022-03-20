import sys

from cx_Freeze import *
includefiles = ["man.ico"]
excludes = []
packages = []
base = None
if sys.platform == 'win32':
    base = 'Win32GUI'

shortcut_table=[
    ("DesktopShortcut",   # Shortcut
      "DesktopFolder",     #Directory
     "StudentManagementSystem",   # Name
     "TARGETDIR", #Component
     "[TARGETDIR]\StudentManagementsSystem.exe",  #Target
     None,   #Arguments
     None,   #Description
     None,   #Hotkey
     None,   #Icon
     None,   #IconIndex
     None,   #ShowCmd
     "TARGETDIR",  #WkDir
    )
]

msi_data = {"Shortcut": shortcut_table}

bdist_msi_options = {'data':msi_data}
setup(
    version='0.1',
    description="Student Management System Developed By Shruti Butte",
    author="Shruti Butte",
    name="Student Management System",
    options={'built_exe': {'include_files':includefiles},'bdist_msi':bdist_msi_options,},
    executables=[
        Executable(
            script="StudentManagementsSystem.py",
            base=base,
            icon='man.ico'
        )
    ]
)
