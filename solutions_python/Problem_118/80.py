res = ["", "0", "1", "2"]
add = ["1", "2"]
CUR = 0

def ispal(n):
    d = []
    while n:
        d.append(n%10)
        n /= 10
    for i in range(len(d)/2):
        if d[i] != d[len(d)-1-i]:
            return False
    return True

def reverse(s):
    res = ""
    for i in s:
        res = i+res
    return res

while CUR < len(res):
    cur = res[CUR]
    CUR += 1
    for i in add:
        toadd = i
        while len(cur)+2*len(toadd) <= 52:
            nums = toadd + cur + reverse(toadd)
            num = int(nums)
            if ispal(num*num) and nums not in res:
                res.append(nums)
            toadd += '0'

nres = [3]
for i in res:
    if i != "" and i != "0":
        nres.append(int(i))

nres.sort()

T = int(raw_input())
for t in range(1,T+1):
    AB = raw_input()
    A = int(AB.split(" ")[0])
    B = int(AB.split(" ")[1])
    RES = 0
    for i in nres:
        if i*i >= A and i*i <= B:
            RES += 1
        elif i*i > B:
            break
    print "Case #"+str(t)+":", RES
