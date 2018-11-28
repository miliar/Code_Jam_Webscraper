import sys


def process_case(R, k, N, g):
    gsum = N*[0]
    gnext = N*[0]
    for i in xrange(N):
        s = 0
        j = i
        done = False
        while not done:
            next_s = s + g[j]
            if next_s > k:
                done = True
            else:
                s = next_s
                j = (j + 1) % N
                if j == i:
                    done = True
        gsum[i] = s
        gnext[i] = j

    money = 0
    first_in_line = 0
    for i in xrange(R):
        money = money + gsum[first_in_line]
        first_in_line = gnext[first_in_line]

    return money
    

def main():
    nbCases = int(sys.stdin.readline())
    for i in xrange(nbCases):
        numbers = map(int, sys.stdin.readline().split())
        R = numbers[0]
        k = numbers[1]
        N = numbers[2]
        g = map(int, sys.stdin.readline().split())
        
        print "Case #%d: %d" % ((i + 1), process_case(R, k, N, g))


if __name__ == "__main__":
    main()
