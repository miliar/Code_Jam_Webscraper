import math

import sys
sys.setrecursionlimit(10000)

class pancake:
    def __init__(self, r, h):
        self.r = r
        self.h = h
        self.surface = math.pi * math.pow(r,2)
        self.sides = 2 * r * h * math.pi
        self.total = self.surface + self.sides


    def __str__(self):
        return 'pancake radius {}  height {} total{}'.format(self.r, self.h,self.total)

class TestCase:

    def __init__(self, t, n, k, pancakes):
        self.t =t
        self.n = n
        self.k =k
        self.pancakes = pancakes
        self.result = f(stack(0,0), k, pancakes)

    def p(self):
        return 'Case #{}: {:0.9}\n'.format(self.t,self.result)





class stack:
    def __init__(self, surface, sides):
        self.surface = surface
        self.sides = sides
        self.total = sides + surface

def add(p1, p2):
    return stack(p1.surface if p1.surface > p2.surface else p2.surface,p1.sides+p2.sides)





def f(s, k, pancakes):
    if (k == 0):
        return s.total
    idx=-1
    maxs=s
    for i in range(0,len(pancakes)):
        p = pancakes[i]
        ts = add(s, p)
        if (ts.total > maxs.total):
            idx=i
            maxs = ts

    pancakes.pop(idx)
    return f(maxs, k-1, pancakes)







#print '{:0.6f} '.format(conv(2525,[ Horse(2400,5)]))
#print '{:0.6f} '.format(conv(300,[ Horse(120,60), Horse(60,90)]))
#print '{:0.6f} '.format(conv(100,[ Horse(80,100), Horse(70,10)]))
#print '{:0.9f} '.format(conv(2,1,[ pancake(100,20), pancake(200,10)]))
#print '{:0.9f} '.format(conv(2,2,[ pancake(100,20), pancake(200,10)]))

#print '{:0.9f} '.format(f(stack(0,0),1,[ pancake(100,20), pancake(200,10)]))
#print '{:0.9f} '.format(f(stack(0,0),2,[ pancake(100,20), pancake(200,10)]))


inFile = 'A-large.in'
outFile = inFile.replace('.in', '.out')

inf = open(inFile, 'r')
outf = open(outFile, 'w')

data = inf.readlines()
noTests = int(data[0])
i=1
h = 0
pancakes = []
for d in data[1:]:
    row = d.split(' ')
    if h ==0:
        n = int(row[0])
        k = int(row[1])
        h = n
    else:
        pancakes.append(pancake(int(row[0]), int(row[1])))
        h=h-1
        if h==0:
            tc = TestCase(i, n, k, pancakes)
            outf.write(tc.p())
            i=i+1
            pancakes=[]

outf.close()
inf.close()
