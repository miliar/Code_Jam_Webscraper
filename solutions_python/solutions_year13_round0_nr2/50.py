from string import *
from operator import mul
from math import *

 
def ncr(n, r):
    r = min(r, n-r)
    if r == 0: return 1
    if r < 0: return 0
    num = reduce(mul, xrange(n, n-r, -1))
    denom = reduce(mul, xrange(1, r+1))
    return num/denom

def memoize(f):
    cache= {}
    def memf(*x):
        if x not in cache:
            cache[x] = f(*x)
        return cache[x]
    return memf

def bin_search(function, search_result, search_from, search_to, precision, *args):
        W = search_to - search_from
        step =  W / 4.0
        initial = W / 2.0 + search_from
        s = function(initial, *args)
        
        while abs(step) > precision:
            if s > search_result and step > 0:
                step = - step / 2
            if s < search_result and step < 0:
                step = - step / 2
            initial = initial + step
            s = function(initial, *args)
        return initial

def square_matrix_multiply(a, b):
    s = len(a)
    r = []
    
    for x in range(s):
        r.append([0] * s)
        for y in range(s):
            for t in range(s):
                r[x][y] += (a[x][t] * b[t][y])
                r[x][y] = r[x][y]
    
    return r 

def fastpower(m, x, p):
    """return a**b % q"""
    val = x
    mult = x
    p -= 1
    
    while p > 0:
        odd = p & 1 # bitwise and
        if odd == 1:
            val = m(val, mult)
            p -= 1
        if p == 0:
            break
        mult = m(mult, mult)
        p = p >> 1 # bitwise divide by 2
    return val

def feq(a, b):
    return fabs(a-b) < 1e-8

def next_permutation(L):
    B = len(L) - 1
    while L[B] <= L[B-1]:
        B = B - 1
        if (B == 0):
            return sorted(L)
    
    b = B
    for x in range(B, len(L)):
        if L[b] > L[x] and L[x] > L[B-1]:
            b = x
    
    (L[b], L[B - 1]) = (L[B - 1], L[b])
    L = L[:B] + sorted(L[B:])
    return L

def semi_circle_segment(x0, x1, R):
    def integral(x, R):
        h = R - x
        return (R**2*acos((R-h)/R) - (R-h)*sqrt(2*R*h-h**2))/2
    
    return - integral(x1, R) + integral(x0, R)

   


class File:
    def __init__(self, filename, mode):
        self.handle = open(filename, mode)
        self.cursor = 0
        self.mode = mode
        if mode == "r":
            self.lines = self.handle.readlines()
    
    def __del__(self):
        self.handle.close()
        
    def readint(self):
        a = int(self.lines[self.cursor])
        self.cursor += 1
        return a

    def readints(self):
        ints = self.lines[self.cursor]
        ints = strip(ints, "\n")
        ints = strip(ints, " ")
        ints = ints.split(" ")
        for a in range(len(ints)):
            ints[a] = int(ints[a])
        self.cursor += 1
        return ints

    def readfloats(self):
        ints = self.lines[self.cursor]
        ints = strip(ints, "\n")
        ints = ints.split(" ")
        for a in range(len(ints)):
            ints[a] = float(ints[a])
        self.cursor += 1
        return ints

    def readstring(self):
        a = self.lines[self.cursor]
        a = strip(a, "\n")
        self.cursor += 1
        return a
    
    def readstrings(self):
        a = self.lines[self.cursor]
        a = strip(a, "\n")
        a = a.split(" ")
        self.cursor += 1
        return a
    
    def write(self, line):
        self.handle.write(line)
        return

    def writeint(self, number):
        self.handle.write(str(number))
        return
        
    def writefloat(self, fl, after):
        self.handle.write(("%." + str(after) + "f") % fl)
        return
        
    def nextline(self):
        self.handle.write("\n")
        return
        
        
    """Matrix = numpy.array(Matrix, dtype = numpy.int64)"""
    
    
class UnionFind:
    def __init__(self):
        '''\
Create an empty union find data structure.'''
        self.num_weights = {}
        self.parent_pointers = {}
        self.num_to_objects = {}
        self.objects_to_num = {}
    def insert_objects(self, objects):
        '''\
Insert a sequence of objects into the structure.  All must be Python hashable.'''
        for object in objects:
            self.find(object);
    def find(self, object):
        '''\
Find the root of the set that an object is in.
If the object was not known, will make it known, and it becomes its own set.
Object must be Python hashable.'''
        if not object in self.objects_to_num:
            obj_num = len(self.objects_to_num)
            self.num_weights[obj_num] = 1
            self.objects_to_num[object] = obj_num
            self.num_to_objects[obj_num] = object
            self.parent_pointers[obj_num] = obj_num
            return object
        stk = [self.objects_to_num[object]]
        par = self.parent_pointers[stk[-1]]
        while par != stk[-1]:
            stk.append(par)
            par = self.parent_pointers[par]
        for i in stk:
            self.parent_pointers[i] = par
        return self.num_to_objects[par]
    def union(self, object1, object2):
        '''\
Combine the sets that contain the two objects given.
Both objects must be Python hashable.
If either or both objects are unknown, will make them known, and combine them.'''
        o1p = self.find(object1)
        o2p = self.find(object2)
        if o1p != o2p:
            on1 = self.objects_to_num[o1p]
            on2 = self.objects_to_num[o2p]
            w1 = self.num_weights[on1]
            w2 = self.num_weights[on2]
            if w1 < w2:
                o1p, o2p, on1, on2, w1, w2 = o2p, o1p, on2, on1, w2, w1
            self.num_weights[on1] = w1+w2
            del self.num_weights[on2]
            self.parent_pointers[on2] = on1
