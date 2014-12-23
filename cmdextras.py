"""KHCmdExtras
A small extension for Python's cmd module.
Can function as a boiler plate.
All vanilla features still apply
"""

__author__ = "Keely Hill"
__copyright__ = "Copyright (c) 2014, Keely Hill"
__license__ = "MIT"
__version__ = "0.1.1"
__maintainer__ = "Keely Hill"

import cmd
import sys
import os


class KHCmdExtras(cmd.Cmd):
    def __init__(self):
        cmd.Cmd.__init__(self)
        self.do_clear(None)

    def do_clear(self, line):
        """Clears the terminal window. Reprints the header."""
        import os
        os.system('cls' if os.name == 'nt' else 'clear')
        if self.intro:
            print(self.intro)

    def do_exit(self, line):
        """Exits program"""
        return True

    def do_restart(self, line):
        """Restarts the program. Useful for on the fly code changes."""
        os.execl(sys.executable, *([sys.executable] + sys.argv))
        return True

    def do_re(self, line):
        """Short cut to 'restart' command. See 'help restart'"""
        self.do_restart(line)

    def do_py(self, line):
        """Allows for basic python statements.
        Usage: py [command], ex: py print("Hello")
        """
        try:
            exec(line)
        except Exception, e:
            print(e)

    def do_EOF(self, line):
        return True


class colors:
    HEADER = '\033[35m'  # purple/pink
    OKBLUE = '\033[34m'  # blue
    OKGREEN = '\033[32m'   # green
    WARNING = '\033[33m'  # yellow
    FAIL = '\033[31m'  # red
    BOLD = '\033[1m'
    UNDERLINE = '\033[4m'
    END = '\033[0m'  # always include at end of style
