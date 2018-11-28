import sys
sys.setrecursionlimit(2000)

def find_max_tidy(n, end):
    for i in range(1, end):
        if int(n[i-1]) > int(n[i]):
            n[i-1] = str(int(n[i-1])-1)
            find_max_tidy(n, i)
            for j in range(i, end):
                n[j] = '9'
                
    return n
        
    

t = int(raw_input())
for i in xrange(1, t + 1):
    n =  raw_input()

    sol_list = find_max_tidy(list(n), len(n))
    sol_str = ''.join(sol_list)
    sol_str = sol_str[1:] if sol_str[0] == '0' else sol_str
    print "Case #{}: {}".format(i, sol_str)
