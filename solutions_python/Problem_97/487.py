import math

def rotate(j):
    #print "In", j
    s = str(j)
    s = s[-1]+s[:-1]
    while s[0] == '0':
        s = s[-1]+s[:-1]
    #print "Out", s
    return int(s)

if __name__ == "__main__":
    T = int(raw_input())
    for i in range(1, T+1):
        A, B = map(int, raw_input().split())
        new = [True]*(B+1)
        next = 1
        ans = 0
        for j in range(A, B+1):
            size = 1
            if new[j]:
                # new[j] = False
                tmp = rotate(j)
                while tmp != j:
                    if tmp >= A and tmp <= B:
                        new[tmp] = False
                        size += 1
                    tmp = rotate(tmp)
            ans += size*(size-1)/2
        print "Case #"+str(i)+": "+str(ans)
