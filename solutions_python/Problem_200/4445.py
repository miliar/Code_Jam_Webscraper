def solve(x):
    safe = 0
    for i in range(len(x)):
        if i < len(x)-1 and int(x[i+1])-int(x[i]) > 0:
            safe = safe+1
        if i < len(x)-1 and int(x[i+1])-int(x[i]) < 0:
            break
    #print i, len(x)
    if i == len(x)-1: # last one was tidy
        return x
    left = str(int(x[:safe+1])-1)
    right = '9'*len(x[safe+1:])
    return str(int(left+right))

n = input()
for i in range(n):
    print "Case #" + str(i+1) + ": " + solve(str(input()))

