import sys



def run():
    d, n = map(int, raw_input().split())
    k = [0] * n
    s = [0] * n
    for i in range(n):
        k[i], s[i] = map(int, raw_input().split())

    max_hours = max([float(d - k[i]) / s[i] for i in range(n)])
    return float(d) / max_hours
    

def main():
    T = input()
    for cas in range(1, T+1):
        print "Case #%d: %.6f" % (cas, run())

if __name__ == '__main__':
    sys.stdin = open("A-large.in", "r")
    sys.stdout = open ("aoutlarge.txt", "w")
    main()
