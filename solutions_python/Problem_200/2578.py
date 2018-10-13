def clean(x):
    #trim leading 0's
    
    return "".join(map(str,x)).lstrip('0')
    
def solve(y):
    x=list(y.rstrip())
    if len(x) == 1:
        return str(x[0])
    lead_big = 0
    for i in range(1,len(x)):
        if x[i-1] > x[i]:
            x[lead_big] = str(int(x[lead_big]) - 1)
            for j in range(lead_big+1, len(x)):
                x[j] = 9
            return clean(x)

        elif x[i] > x[i-1]:
            lead_big = i
    return clean(x)

with open("B-large.in") as f:
    T = int(f.readline().rstrip())
    data = f.readlines()
    ans = map(solve,data)
    for i in range(len(ans)):
        print "CASE #%d: %s" % (i+1,ans[i])