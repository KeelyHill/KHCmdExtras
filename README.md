KHCmdExtras
----------

A small extension for Python's cmd module that can function as a boiler plate.
All vanilla features still apply.

Usage
-----
```python
class Example(cmdextras.KHCmdExtras):
    def do_greet(self, line):
        print("Hello world")

if __name__ == '__main__':
    Example().cmdloop()
```
