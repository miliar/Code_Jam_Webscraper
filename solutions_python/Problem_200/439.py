# -*- coding:utf8

# Python3
# zhuny@kaist.ac.kr


import time
import sys


class Timer:
    def __init__(self,name):
        self.name = name
        self.start = 0.0

    def __enter__(self):
        self.start = time.time()

    def __exit__(self,ty,va,tr):
        print (self.name,time.time()-self.start)


class CodeJam:
    def __init__(self,stdio):
        self.stdio = stdio
        n = self.get_number()
        with Timer("CodeJam Time :"):
            for i in range(1,n+1):
                self.print_it("Case #{0}:",i)
                self.do()

    def show(self,*argv):
        n = len(argv)
        L = ["{%s}"%i for i in range(n)]
        self.print_ln(" ".join(L), *argv)

    def print_it(self,string="",*argv,**kwargs):
        end = kwargs.pop('end', " ")
        string = str(string)
        self.stdio.write(string.format(*argv,**kwargs), end=end)

    def print_ln(self,string="",*argv,**kwargs):
        self.print_it(string, end="\n", *argv, **kwargs)

    def get_line(self):
        return self.stdio.readline().strip()

    def get_line_func(self,func):
        return func(self.get_line())

    def get_number(self):
        return self.get_line_func(int)

    def get_line_func_split(self,func):
        return self.get_line_func(
            lambda l,f=func:[f(l_) for l_ in l.split()])

    def get_numbers(self):
        return self.get_line_func_split(int)

    def get_float(self):
        return self.get_line_func(float)

    def get_floats(self):
        return self.get_line_func_split(float)

    def do(self):
        self.print_it("\n")


class SysIO:
    def write(self,*argv,**kwargs):
        print (*argv,**kwargs)

    def readline(self):
        return input()


class StdIO(SysIO):
    stdin = None
    stdout = None

    def __init__(self,name):
        self.stdin = open(name, encoding="utf8")

        if name.endswith(".in"):
            name = name[:-3]
        name += ".out"
        self.stdout = open(name,'w',encoding="utf8")

    def __del__(self):
        if self.stdin:
            self.stdin.close()
        if self.stdout:
            self.stdout.close()

    def readline(self):
        return self.stdin.readline().rstrip()

    def write(self,*argv,**kwargs):
        SysIO.write(self,*argv,**kwargs)
        print (file=self.stdout, *argv,**kwargs)




