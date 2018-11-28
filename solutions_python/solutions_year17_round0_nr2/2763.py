T = int(raw_input())

for x in range(T):
    print "Case #{0}:".format(x+1),
    t = raw_input()
    if ''.join(sorted(t)) == t:
        print t
    else:
        for i in range(1,len(t)):
            if t[i] < t[i-1]:
                j = i-1
                while j!=0 and not t[j] > t[j-1]:
                    j-=1
                print int(t[:j] + str(int(t[j]) - 1) + '9'*(len(t) - j - 1))
                break
