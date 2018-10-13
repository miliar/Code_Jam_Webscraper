#!/usr/bin/python

# Dan Seminara

import fileinput

def main():
    inp = []
    for i,line in enumerate(fileinput.input()):
        if i == 0:
            continue
        inp.append(line.strip())
    tricks = zip(*[iter(inp)]*10)
    for i,trick in enumerate(tricks):
        r1 = int(trick[0])
        b1 = [r.split(' ') for r in trick[1:5]]
        r2 = int(trick[5])
        b2 = [r.split(' ') for r in trick[6:10]]
        inter = set(b1[r1-1]) & set(b2[r2-1])
        if len(inter) == 1:
            print('Case #%d: %s' % (i+1,inter.pop()))
        elif len(inter) > 0:
            print('Case #%d: Bad magician!' % (i+1))
        else:
            print('Case #%d: Volunteer cheated!' % (i+1))
    

if __name__ == '__main__':
    main()