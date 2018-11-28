import sys

if __name__ == "__main__":
    T = int(sys.stdin.readline().strip())
    case_no = 0
    while T > 0:
        case_no += 1
        c, s = sys.stdin.readline().strip().split(' ')
        c = int(c)
        s = list(map(int, s))
        clapping = 0
        to_add = 0
        for i in range(len(s)):
            if s[i] > 0 and i > clapping:
                to_add += i - clapping
                clapping = i
            clapping += s[i]
        T -= 1
        print("Case #{}: {}".format(case_no, to_add))
