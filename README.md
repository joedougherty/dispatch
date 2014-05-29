## Dispatch Table Example ##

Short example of how to implement a [Dispatch Table](http://en.wikipedia.org/wiki/Dispatch_table) for simple interactive CLI tools. 
Could be used as the foundation of a simple text-based CLI game.

## OS-Specific Note ##
This relies *heavily* on Python's readline module to provide session-based command history and tab completion.
I have *only* tested on Red Hat Enterprise Linux Server release 5.9 (Tikanga).
The [readline documentation](https://pypi.python.org/pypi/readline) suggests this can work on Mac OS X (using editline), but I have not tested.
