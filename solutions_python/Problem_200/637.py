fin = open("B-large.in","rt")

n = int( fin.readline().rstrip('\n') )

def notTidy(s):
    for x in range(len(s)-1):
        if s[x] > s[x+1]:
            for y in range(1,len(s)-x):
                s[x+y] = 9
            s[x] -= 1
            return True
    return False

fout = open("OUTPUT","wt")
for x in range(n):
    s = fin.readline().rstrip('\n')
    print s,
    print ":",
    s = [int(y) for y in list(s)]
    while notTidy(s): continue
    while s[0] == 0: s = s[1:]
    
    st = "Case #" + str(x+1) +": "
    st += "".join([str(z) for z in s])
    print st
    fout.write(st+"\n")
    
    
fout.close()
