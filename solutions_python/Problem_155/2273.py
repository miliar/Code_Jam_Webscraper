f = open("in.txt", "r").readlines()[1:]
upto = 0
ans = []
out = open("out.txt", "w")
for num in f:
    smax,aud = num.strip().split()
    curraud = 0
    toadd = 0
    for i in xrange(int(smax)+1):
        if curraud >= i:
            curraud += int(aud[i])
        else:
            toadd += i - curraud
            curraud += i - curraud + int(aud[i])
    s = "Case #" + str(upto+1) + ": " + str(toadd) + "\n"
    out.write(s)
    upto += 1
out.close()
