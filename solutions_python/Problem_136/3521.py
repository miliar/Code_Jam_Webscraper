import os
import sys
sys.setrecursionlimit(2000)

def cookie(pos,farms,c, f, x, cps, ctb, previous,tctb):
    current = tctb+(x/cps)
    if (current) > previous and farms != 0:
        print 'Case #'+str(pos)+': ' + str(round(previous,7))
        return
    # buy farm
    cost_to_build = c/cps
    cps += f
    farms+=1
    tctb += cost_to_build #total cost to build
    cookie(pos,farms,c,f,x,cps,cost_to_build,current,tctb)

def main(filename):
    with open(filename, 'r+') as f:
        pos = 0
        case_list = []
        cases = []
        try:
            for line in f:
                if pos == 0:
                    num_of_cases = line.strip()
                    pos += 1
                else:
                    c,f,x = line.strip().split(" ")
                    cps = 2
                    tmp = cookie(pos, 0,float(c),float(f),float(x),cps,0,0,0)
                    pos += 1

        except StopIteration:
            pass

if __name__ == "__main__":
    if len(sys.argv) > 1:
        main(sys.argv[1])