from sys import argv
import math
import itertools
import numpy

def read(f):
    return next(f).strip("\n")
    
def read_singles(f):
    # returns chars of a word
    # or digits of an int
    return list(read(f))
    
def read_int(f, b=10):
    return int(read(f), b)
 
def read_float(f):
    return float(read(f))
 
def read_digits(f, b=10):
    return [int(n, b) for n in read_singles(f)]

#---------------------------------------------

def read_strs(f, s=" "):
    return read(f).split(s)
    
def read_ints(f, b=10, s=" "):
    return [int(n, b) for n in read_strs(f, s)]

def read_floats(f, s=" "):
    return [float(n) for n in read_strs(f, s)]
               
#---------------------------------------------

def read_lines(f, n, reader=read_ints, *args, **kwargs):
    ret = []
    for i in range(n):
        ret.append(reader(f, *args, **kwargs))
    return ret

#---------------------------------------------

def run(data):
    r, t = data
    #return 1 +   (t/pi - 2*r - 1) / 4
    # diff is uneven**2-even**2
    #return (-r/2 -3/4 + (r**2/4 + 3*r/4 + 9/16 + t/(2*pi))**0.5)*(49/16)
    
    # "naive" solution for small:
    i = 0
    print t
    while t>=0:
        t -= (2*r + 1 + 4*i)
        print t
        i += 1
    return i-1

#---------------------------------------------

def read_case(f):
    global pi
    pi = 3.14159265359
    return read_ints(f)

def write_case(f, i, sol):
    f.writelines("Case #%d: %s\n" % (i+1, sol))

#---------------------------------------------

def main():
    f = open(argv[1])
    f2 = open(argv[2], "wt")
    for i in range(read_int(f)):
        write_case(f2, i, run(read_case(f)))
    f.close()
    f2.close()
        

if __name__ == "__main__":
    main()
