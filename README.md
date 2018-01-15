# files_finder
Program to recursively find (big) files under a tree/directory

## About
This program is written for finding out the biggest files within a specific folder, as well as a form of showing the approach to accomplish this task in the same way as other tools do (e.g. in a Linux env: find, du, etc).

It uses recursion for the tree traversal part and has custom data strutures capable of just storing the exact ammount of requested results, solving any space possible issues. It aims and uses performance friendly approaches, but it's not guaranteed that it uses the best approach amongst all possible ones.

## How to use it
```
$ python files_finder.py -p '/cygdrive/c/Users/Marcelo/Documents' -n 5
969932800  _replay0.bin
838860800  replay0.bin
81815309   Career Mode.fm
78577001   Career Mode (v02).fm
77802266   Career Mode (v02) (v02).fm

$ python files_finder.py -p '/cygdrive/c/Users/Marcelo/Documents' --number=2 --fullpath --human
925.0MB    /cygdrive/c/Users/Marcelo/Documents/FIFA 17 Demo/Temp/_replay0.bin
800.0MB    /cygdrive/c/Users/Marcelo/Documents/FIFA 16/instance0/replay0.bin
```
## How to use it as a Python module
```
$ python
Python 2.7.14 (default, Oct 31 2017, 21:12:13)
>>> from files_finder import FileQueue
>>> r = FileQueue(5)
>>> r.find('/cygdrive/c/Users/Marcelo/Documents')
>>> r.deque
>>>
deque([<files_finder.File object at 0x6ffffe0bd50>, <files_finder.File object at 0x6ffffe0b410>, <files_finder.File object at 0x6ffffe0b450>, <files_finder.File object at 0x6ffffe0b490>, <files_finder.File object at 0x6ffffe0b510>], maxlen=5)
>>>
>>> [(f.name, f.size) for f in r.deque]
[('Bora (v02) (v02).fm', 77802266), ('Bora (v02).fm', 78577001), ('replay0.bin', 838860800), ('_replay0.bin', 969932800), ('Bora.fm', 81815309)]
```


## Author
Marcelo Marques da Silva Varge (marcelo.varge@gmail.com)

## Credits
`sizeof_fmt` function was taken from [here](https://stackoverflow.com/a/1094933/3918806) and [here](https://web.archive.org/web/20111010015624/http://blogmag.net/blog/read/38/Print_human_readable_file_size).
