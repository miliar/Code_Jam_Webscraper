#!/usr/bin/python

from math import *

f=open('bathrooms_large.in', 'r')
output=open('bathrooms_large.out', 'w')
# f=open('bathrooms_small1.in', 'r')
# output=open('bathrooms_small1.out', 'w')

cases=int(f.readline())

def two_splits(x):
    if x % 2 == 0:
        return x / 2, x / 2 - 1
    else:
        return (x - 1) / 2, (x - 1) / 2

class Bathroom:
    def __init__(self, n):
        self.bathrooms={n: 1}
        self.largest_bathroom=n

    def bathrooms_str(self):
        return repr(self.bathrooms)

    def largest(self):
        return self.largest_bathroom

    def largest_count(self):
        return self.bathrooms[self.largest_bathroom]

    def add(self, x, count):
        if x in self.bathrooms:
            self.bathrooms[x] = self.bathrooms[x] + count
        else:
            self.bathrooms[x] = count

    def split_all_largest(self):
        largest=self.largest_bathroom
        count=self.largest_count()
        bigger, smaller = two_splits(largest)
        del self.bathrooms[largest]
        if bigger == smaller:
            self.add(bigger, count * 2)
        else:
            self.add(bigger,  count)
            self.add(smaller, count)
        self.largest_bathroom=max(self.bathrooms.keys())

def bathrooms(n, k):
    bathroom=Bathroom(n)
    remaining_people = k
    while remaining_people > 0:
        # print "Remaining people: %i" % remaining_people
        # print "Largest bathroom: %i: %i" % (bathroom.largest(), bathroom.largest_count())
        # print "%s" % (bathroom.bathrooms_str())
        # print ""
        largest_count=bathroom.largest_count()
        if remaining_people <= largest_count:
            return two_splits(bathroom.largest())
        else:
            remaining_people -= largest_count
            bathroom.split_all_largest()

for case in range(cases):
    arr=f.readline().replace("\n","").split(' ')
    n=int(arr[0])
    k=int(arr[1])
    # print "n, k: %i, %i" % (n, k)
    value="%i %i" % (bathrooms(n, k))
    # print ""
    # print ""
    # print "Case #%i: %s (%i %i)" % (case+1, value, n, k)
    output.write ("Case #%i: %s\n" % (case+1, value))
