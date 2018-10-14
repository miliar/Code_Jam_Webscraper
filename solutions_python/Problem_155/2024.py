
fle = open("output.txt","w")
T = int(raw_input())
for z in range(1,T+1):
    A, b = raw_input().split()
    A = int(A)
    B = []
    for i in b:
        B.append(int(i))
    guest = 0
    g = 0
    C = 0
    w = 0
    while w < len(B):
        if w == 0:
            C = B[w]
        else:
            for i in range(B[w]):
                if C >= w:
                    C = C+1
                else:
                    g = w - C
                    guest = guest + g
                    C = C+g+1 
        w = w + 1
    ans = "Case #%i: %i" %(z, guest)
    fle.write(ans+"\n")
fle.close()