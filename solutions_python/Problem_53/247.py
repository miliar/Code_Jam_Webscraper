def snapper(n, k):
    return (k+1) & ((1<<n) - 1) == 0

def main():
    labels = ["OFF", "ON"]
    try:
        cases = xrange(1, int(raw_input())+1)
        for case in cases:
            n, k = map(int, raw_input().split())
            print "Case #%d: %s" % (case, labels[snapper(n, k)])
    except ValueError:
        print "INVALID INPUT"

main()
