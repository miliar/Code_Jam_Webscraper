#! /usr/bin/env python

def solve() :
    input = raw_input().split()
    C = int(input[0])
    del input[0]
    
    base = []
    for i in range(C):
        base.append(input[0])
        del input[0]

    D = int(input[0])
    del input[0]
    oppose = []
    for i in range(D):
        oppose.append(input[0])
        del input[0]

    E = input[1]
    
    ans = []
    for el in E:
        ans.append(el)
        
        for b in base:
            if len(ans) >= 2:
                if ((ans[-1] == b[0] and ans[-2] == b[1]) or
                    (ans[-1] == b[1] and ans[-2] == b[0])):
                    ans[-2:] = b[2]

        for d in oppose:
            if len(ans) >= 2:
                if ans.count(d[0]) > 0 and ans.count(d[1]) > 0:
                    ans = []
    temp = str(ans).replace("'",'')
    return temp
    

def main() :
    T = int(raw_input())
    for tno in range(T):
        res = solve()
        print "Case #" + str(tno + 1)+ ": " + str(res)
        
if __name__ == '__main__':
    main()
