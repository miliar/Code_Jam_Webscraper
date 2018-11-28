f=open("input.txt","r")
t = int(f.readline())

fo=open("output.txt","w")
print t

def solve(s,num):
    tmp = []
    for c in num:
        tmp.append(int(c))
    #print tmp
    t = tmp[0]
    ans = 0
    for i in range(1,len(tmp)):
        if i > t and tmp[i] != 0:
            ans += i-t
            #print i, tmp[i], t, ans
            t += i-t
        t += tmp[i]
    return ans

s =[]
for i in range(0,t):
    l = f.readline()
    s = l.split()[0]
    num = l.split()[1]
    ans = solve(s, num)
    print "Case #"+str(i+1)+": "+str(ans)
    fo.writelines("Case #"+str(i+1)+": "+str(ans)+"\n")

f.close()
fo.close()



