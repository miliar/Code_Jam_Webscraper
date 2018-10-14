import re
foo=open("B-large.in","r")
bar=open("law_op_l.txt","w")
t=int(foo.readline().rstrip())

def check(lawn):
    row_maxes = [max(x) for x in lawn]
    cols = [[lawn[i][j] for i in range(len(lawn))] for j in range(len(lawn[0]))]
    col_maxes = [max(x) for x in cols]
    for i in range(len(lawn)):
        for j in range(len(lawn[i])):
            val = lawn[i][j]
            if val != row_maxes[i] and val != col_maxes[j]:
                return "NO"
    return "YES"
        

def read(foo):
    dims = re.split(" ",foo.readline())
    x,y = int(dims[1]), int(dims[0])    
    lawn = []
    for i in range(y):
        line = foo.readline()
        nums = [int(x.strip()) for x in re.split(" ",line)]
        lawn.append(nums)
    return lawn

n=1
while n<=t:
    
    data = read(foo)
    ans = "Case #%d: %s" % (n, check(data))
    print ans
    ans = ans+'\n'
    bar.write(ans)
    n+=1

foo.close()
bar.close()
