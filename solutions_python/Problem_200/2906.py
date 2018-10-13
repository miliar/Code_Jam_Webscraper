case = 0
def minus(n):
    """iter = len(n)-1
    while(iter > 0):
        if(int(n[iter])>0):
            n = n[:iter] + str(int(n[iter])-1) + n[iter+1:]
            break
        else:
            pass"""

    if len(n)<1:
        return n
    if int(n[-1])>0:
        n = n[:len(n)-1] + str(int(n[-1])-1)
    else:
        n = minus(n[:len(n)-1]) + "9"

    if n[0] == "0":
        n = n[1:]

    return n

def sub(n):
    if len(n)<2:
        return n
    iter = 0
    index = len(n)
    while iter<len(n)-1:
        if n[iter]<=n[iter+1]:
            iter += 1
        else:
            index = iter + 1
            break
    if index == len(n):
        return n
    ret = sub(minus(n[:index]))
    for i in range(len(n)-index):
        ret += "9"

    return ret
    

for tc in range(int(raw_input())):
    n = raw_input()
    n = sub(n)
    case += 1
    print "Case #"+str(case)+": "+n
        
