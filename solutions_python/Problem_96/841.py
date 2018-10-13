from root.codejam.Tools import *

#copy sample input and output here
sampleIn = """4
3 1 5 15 13 11
3 0 8 23 22 21
2 1 1 8 0
6 2 8 29 20 8 18 18 21
"""
sampleOut = """Case #1: 3
Case #2: 2
Case #3: 1
Case #4: 3
"""



def solve(ipt):
    line = ipt.nextLine(sep=' ', toInt=True)
    N, S, p = line[:3]
    t_list = line[3:]
    
    counter = 0
    for t in t_list:
        if t > 0 and t >= 3 * p - 2:
            counter += 1
        elif t > 0 and (3 * p - 4) <= t < (3 * p - 2) and S > 0:
            S -= 1
            counter += 1
        elif t == 0 and p == 0:
            counter += 1
    return counter




if __name__ == '__main__':
#for testing
#    submit(solve, sampleIn, None)
#for submit
    submit(solve, 'B-large.in')
        
