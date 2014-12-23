KHCmdExtras
----------

A small extension for Python's cmd module that can function as a boiler plate.
All vanilla features still apply. Also includes a color class for printing to the terminal with colors.

Usage
-----
```python
class Example(cmdextras.KHCmdExtras):
    def do_greet(self, line):
        print(colors.OKBLUE + "Hello world" + colors.END)

if __name__ == '__main__':
    Example().cmdloop()
```
