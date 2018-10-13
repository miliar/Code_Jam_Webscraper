##def test(a, b):
##    a, b = str(a), str(b)
##    for i in range(1, len(a)):
##        if a[-i:] + a[:-i] == b: return True
##    return False
##
##cnt = 0
##for line in open("test.txt"):
##    a, b = map(int, line.split())
##    if a < b and a >= 1111 and b <= 2222 and test(a, b):
##        cnt += 1
##print(cnt)



infile = "C-large.in"
lines = [l.strip() for l in open(infile)][1:]

fout = open("out.txt", "w")

def test(n, B, nlen, mpow):
    m = n
    nums = []
    for i in range(nlen):
        d = m % 10
        m = d * mpow + m / 10
        if d != 0 and m > n and m <= B:
            #print n, m
            nums.append(m)
    nums.sort()
    cnt = 0
    prev = -1
    for num in nums:
        if num != prev:
            cnt += 1
        prev = num
    return cnt
    
        

caseNum = 0
for line in lines:
    caseNum += 1
    A, B = map(int, line.split())
    print "solving #" + str(caseNum) + ": " + str(A) + ", " + str(B)
    nlen = len(str(A))
    mpow = 1
    for i in range(nlen-1):
        mpow *= 10
    cnt = 0
    for i in range(A, B):
        cnt += test(i, B, nlen, mpow)
    fout.write("Case #" + str(caseNum) + ": " + str(cnt) + "\n")

fout.close()
