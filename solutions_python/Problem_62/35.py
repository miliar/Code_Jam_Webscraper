
def intsect(A, B, l):
    cnt =0
    for x in l:
        if A<x[0] and B>x[1]:
            cnt += 1
        if A>x[0] and B<x[1]:
            cnt += 1
    return cnt

if __name__ == "__main__":
    t = int(raw_input())
    for i in range(1, t+1):
        n = int(raw_input())
        l = []
        ans = 0
        for j in range(0, n):
            line = raw_input()
            vl = line.split(" ")
            A = int(vl[0])
            B = int(vl[1])
            ans += intsect(A, B, l)
            l.append((A, B))

        print "Case #" + str(i) + ": " + str(ans)
        
