# reads the number of test cases 
t = int(input())  


def findtidy(s):
    """    Returns max tidy string that is not greater than s
    """
    i = 0
    while i < len(s)-1:
        if s[i+1] < s[i]:
            break
        i+=1
    if i < len(s) - 1:
        while i > 0:
            if s[i-1] != s[i]:
                break
            i-=1
        snew = list(s)
        snew[i] = str(int(snew[i]) - 1)
        for k in range(i+1,len(s)):
            snew[k]='9'
        if int(snew[i]) == 0:
            snew = snew[1:]
        return str.join("",snew)
    else:
        return s



for i in range(1, t+1):
    n = str(input())
    print("Case #{}: {}".format(i,findtidy(n)))
    



