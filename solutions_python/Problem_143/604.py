__author__ = 'nguyensontung1404'

def toBin(n):
    return int(bin(n)[2:])

def toDec(n):
    return int(str(n), 2)

def find_winning(a, b):
    return int(a & b)

if __name__ == "__main__":
    import sys
    sys.stdin = open("B-small-attempt0.in")
    sys.stdout = open("out.txt", "w")
    for case in range(1, int(sys.stdin.readline())+1):
        _str = sys.stdin.readline()
        A, B, K = map(int, _str.split(" "))
        count = 0
        for x in range(A):
            for y in range(B):
                if int(x&y) in range(K):
                    count += 1
        print "Case #%d: %d" % (case, count)