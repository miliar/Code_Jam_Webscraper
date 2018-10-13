def solve():
    result = 0
    standing = 0
    smax_shynessstr = raw_input().split()
    shyness_array = map(int,list(smax_shynessstr[1]))
    for i in xrange(len(shyness_array)):
        invitees = max(0, i-standing)
        result += invitees
        standing += shyness_array[i] + invitees
    return result

def main():
    T = int(raw_input())
    for i in xrange(1,T+1):
        ans = solve()
        print "Case #%d: %d" % (i, ans)

if __name__ == "__main__":
    main()
