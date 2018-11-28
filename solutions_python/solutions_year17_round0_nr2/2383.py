import sys
writeln=lambda x:sys.stdout.write(str(x)+"\n")
write=lambda x:sys.stdout.write(x)
ubs,lbs = [9],[1]
for i in range(20):
    u = ubs[-1]; l = lbs[-1]
    ubs.append(9 + u*10); lbs.append(1+l*10)

def inbound(num, jari):
    if jari == 1:
        return False, num
    if ubs[jari-2] < num < lbs[jari-1]:

        return False, ubs[jari-2]
    else:
        return True, num

def solve(num, jari):
    nArr = []
    q = num
    while True:
        q,r=divmod(q, 10)
        nArr.append(r)
        if not q:
            break
    nArr.reverse()
    firstInvalid = -1
    for i in range(jari-1):        
        if nArr[i] > nArr[i+1]:
            firstInvalid = i
            break
    if firstInvalid == -1:
        return num
    
    for i in range(firstInvalid + 1, jari):
        nArr[i] = 9
    nArr[firstInvalid] -= 1
    cur = firstInvalid
    while cur:        
        if nArr[cur-1] > nArr[cur]:
            nArr[cur-1] -= 1
            nArr[cur] = 9
        else:
            break
        cur -= 1
    tnum = 0
    for i in range(jari):
        tnum = 10*tnum + nArr[i]
    return tnum

sys.stdout = open('output.txt', 'w')
with open('B-large.in') as f:
    T = int(f.readline().rstrip());
    for t in range(T):
        N = int(f.readline())
        jarisu = 1
        q = N
        while q and q >= 10:
            q = q // 10; jarisu += 1
        cont, res = inbound(N, jarisu)    
        if not cont:
            answer = res
            write("Case #%d: %s\n" % (t+1, str(answer)))
            continue

        answer = solve(N, jarisu)

        write("Case #%d: %s\n" % (t+1, str(answer)))