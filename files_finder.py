import os
from collections import deque

class Finder(object):

    def find(self, path):
        for f in os.listdir(path):
            p = os.path.join(path, f)
            try:
                if os.path.isfile(p):
                    f = p if self.fullpath else f
                    self.add(File(f, os.stat(p).st_size))
                elif os.path.isdir(p):
                    self.find(p)
            except OSError:
                # is this needed?
                pass


class Result(Finder):

    def __init__(self, size, fullpath=False, human_read=False):
        self.size = size
        self.fullpath = fullpath
        self.human_read = human_read
        self.deque = deque(maxlen=size)
        self.deque.append(File('', 0))

    def add(self, file):
        if file.size >= min([f.size for f in self.deque]):
            self.sort()
            self.deque.append(file)

    def sort(self):
        self.deque = deque(sorted(self.deque, key=lambda x: x.size), maxlen=self.size)

    def output(self):
        for f in sorted(r.deque, key=lambda x: x.size, reverse=True):
            if self.human_read:
                f.size = sizeof_fmt(f.size)
            print("{0:<10} {1}".format(f.size, f.name))


class File(object):

    def __init__(self, name, size):
        self.name = name
        self.size = size


def sizeof_fmt(num, suffix='B'):
    for unit in ['','K','M','G','T','P','E','Z']:
        if abs(num) < 1024.0:
            return "%3.1f%s%s" % (num, unit, suffix)
        num /= 1024.0
    return "%.1f%s%s" % (num, 'Y', suffix)

if __name__ == "__main__":
    from helper import parse
    args = parse()
    r = Result(args.number, fullpath=args.fullpath, human_read=args.human)
    r.find(args.path)
    r.output()
