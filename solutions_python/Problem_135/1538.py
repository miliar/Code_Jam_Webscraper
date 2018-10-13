#!/usr/bin/python

import sys

def solve(r1, c1, r2, c2, outf):
    ans = set(c1[r1-1]).intersection(set(c2[r2-1]))
    s = len(ans)
    if(s == 1):
        outf.write(ans.pop())
    elif(s == 0):
        outf.write("Volunteer cheated!")
    else:
        outf.write("Bad magician!")


def create_cards(f):
    c = []
    c.append(str(f.readline()).split())
    c.append(str(f.readline()).split())
    c.append(str(f.readline()).split())
    c.append(str(f.readline()).split())

    return c

def run():
    infilename = sys.argv[1]
    outfilename = sys.argv[2]
    inf = open(infilename, 'r')
    outf = open(outfilename, 'w')

    data = int(inf.readline())
    cases_num = data

    for i in range(cases_num):
        outf.write("Case #{0}: ".format(i+1))
        r1 = int(inf.readline())
        c1 = create_cards(inf)
        r2 = int(inf.readline())
        c2 = create_cards(inf)
        
        solve(r1, c1, r2, c2, outf)
        outf.write("\n")

    inf.close()
    outf.close()

if __name__ == "__main__":
    run()

    
    

