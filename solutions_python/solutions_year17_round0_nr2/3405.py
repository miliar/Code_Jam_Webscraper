from itertools import groupby
import sys

def last_tidy(num) :
    if len(num) == 1 : return num

    #print "in : " + num + ".." + str(len(num))
    l = len(num)
    for i in range(l-1) :
        #print "h" , num[i], ":", num[i+1]
        if not (int(num[i]) <= int(num[i+1])) :
            # hack to go faster
            if(i == 0 and int(num[i]) == 1) :
                return '9'*(l-1)
            mod = str(int(num[0:i+1]) - 1)
            mod = mod + '9'*(l-i-1)
            #print "Mod : " + mod
            return last_tidy(mod)
    return num


w = int(sys.stdin.readline().strip())
i = 1
for line in sys.stdin:
    inp = int(line)
    ans = last_tidy(str(inp))
    print "Case #"+str(i)+": " +  ans
    i+=1

