def case(smax,s):
    invite = 0
    people = 0
    for i in range(smax+1):
        k = int(s[i])
        if k != 0 and people < i:
            invite += (i-people)
            people += (i-people)
        people += k
    return str(invite)

def main():
    n = int(raw_input())
    for i in xrange(n):
        smax,s = raw_input().split()
        smax = int(smax)
        print "Case #"+str(i+1)+": " + case(smax,s)

if __name__ == '__main__':
    main()