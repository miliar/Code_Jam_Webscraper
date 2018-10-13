import sys

def main():
    T = int(sys.stdin.readline())
    for t in range(1, T+1):
        Smax, couting = sys.stdin.readline().split()
        Smax = int(Smax)
        couting = [int(c) for c in couting]
        friends = 0
        audiences = [0] * len(couting)
        for i in range(1, len(couting)):
            audiences[i] = audiences[i-1] + couting[i-1]
            friends += max(0, i - audiences[i] - friends)
        # print audiences
        # print range(len(audiences))
        print "Case #%d:" % t, friends

if __name__ == "__main__":
    main()
