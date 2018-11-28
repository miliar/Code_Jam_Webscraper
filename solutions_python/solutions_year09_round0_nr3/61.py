wtcj = "welcome to code jam"

memo = []

orig_string = ""

def recurse(wtcj_place, string_place):
    if memo[wtcj_place][string_place] != -1:
        return memo[wtcj_place][string_place]
        
    tmp = recurse(wtcj_place, string_place+1)
    
    if orig_string[string_place] == wtcj[wtcj_place]:
        tmp += recurse(wtcj_place+1, string_place+1)
        
    memo[wtcj_place][string_place] = tmp % 10000
    
    return tmp % 10000

N = int(raw_input())

for t in range(N):
    orig_string = raw_input()
    memo = [[-1 for i in range(len(orig_string)+1)] for i in range(len(wtcj)+1)]

    for i in range(len(wtcj)+1):
        memo[i][len(orig_string)] = 0

    for i in range(len(orig_string)+1):
        memo[len(wtcj)][i] = 1
    
    ans = recurse(0, 0)
    
    print "Case #" + str(t+1) + ":", 
    if ans < 1:
        print "0"*4
    elif ans < 10:
        print "0"*3 + str(ans)
    elif ans < 100:
        print "0"*2 + str(ans)
    elif ans < 1000:
        print "0"*1 + str(ans)
    else:
        print ans