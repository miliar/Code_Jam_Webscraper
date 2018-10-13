import re

raw = open('C-small-attempt0.in').read().split('\n')

a1 = filter(lambda s:len(s), map(lambda s:s.strip(), raw))
a1 = a1[1:]

if len(a1) == 0:
    exit();
    
seeds = 'welcome to code jam'

def find(str, seeds):
    start = 0
    count = 0
    if len(str)<=1:
        return 1 if seeds == str else 0
    if len(seeds) == 1:
        return str.count(seeds)
    
    pos = str.find(seeds[0])
    while pos >=0:
        count += find(str[pos:],seeds[1:])
        pos = str.find(seeds[0],pos+1)

    return count

b = open('xx.out','w')

count = 1
for tmp in a1:
    s = "Case #%d: %04d\n" % (count, find(tmp, seeds))
    b.write(s)
    count += 1
