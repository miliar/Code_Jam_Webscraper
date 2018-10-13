
import itertools
from collections import defaultdict

def parse(text):
    return map(lambda x: int(x), text.split())

def find_splits(candies):

    total = 0
    for candy in candies:
        total = total^candy

    if total != 0:
        return "NO"

    #powers = defaultdict(list)
    #biggest = max(candies)
    #max_power = len(bin(biggest))-2
    #for candy in candies:
    #    for i in xrange(max_power):
    #        if 2**i > candy:
    #            break
    #        if 2**i ^ candy < candy:
    #            powers[i].append(candy)

    min_candy = min(candies)
    candies.remove(min_candy)
    return sum(candies)

#print find_splits([3, 5, 6])

file = open('C-large.in', 'rb')
outfile = open('C-large.out', 'wb')
items = file.readline()
for index, line in enumerate(file.readlines()):
    if (index+1) % 2: continue
    #print line
    towrite = "Case #%s: %s\n" %( index/2+1, find_splits(parse(line)))
    outfile.write(towrite)