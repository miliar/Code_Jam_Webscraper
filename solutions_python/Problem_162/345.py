'''
Created on 11.04.2015

@author: uscheller
'''
import sys



def swap(n):
    return int("".join([x for x in reversed(str(n))]))

def create_map(n):
    known = {1: 1}
    for i in range(2, n + 1):
        known[i] = n
    
    q = [1]
    while q:
        i = q.pop(0)
        count = known[i]
        if i + 1 <= n:
            if known[i + 1] > count + 1:
                q.append(i + 1)
                known[i + 1] = count + 1
        sw = swap(i)
        if sw <= n:
            if known[sw] > count + 1:
                q.append(sw)
                known[sw] = count + 1
    return known
   
def solve(n):
    return create_map(n)[n]         

        

def go_through(data):
    data = data[1:]
    s = ""
    case = 1
    while len(data) > 0:
        N = int(data[0])
        data = data[1:]
        s += "Case #%d: %d\n" % (case, solve(N))
        case += 1
    return s[:-1] # remove newline

if __name__ == '__main__':
    print go_through(open(sys.argv[1]).readlines())