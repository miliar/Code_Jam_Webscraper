def bal(l):
    for j in range(len(l)-2,-1,-1):
        temp = l[j:]
        if sorted(temp) == temp:
            pass
        else:
            if temp[0]!=0:
                xx = temp[0]-1
                temp = [xx] + [9]*(len(temp)-1)
                l = l[:j]+temp
            else:
                v = j-1
                while l[v]!=0:
                    v -= 1
                yy = l[v]-1
                l = l[:v]+ [yy] + [9]*(len(l)-v-1)
    ans = int("".join([str(a) for a in l]))
    return ans

f = [line.rstrip() for line in open('/Users/roshil/Desktop/try.txt')]
out = open('/Users/roshil/Desktop/output','w')
out.truncate()
line = 0
testcases = int(f[line])
line += 1
for j in range(1, testcases+1):
    m = f[line]
    line += 1
    l = [int(k) for k in m]
    ans = bal(l)
    out.write("Case #"+str(j)+": "+str(ans) + "\n")
    #print "case #"+str(j)+": "+str(ans) + "\n"
out.close()
