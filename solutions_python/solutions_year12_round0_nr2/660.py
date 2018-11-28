import sys

def solve(s, p, scores):
    count = 0
    for score in scores:
        a = score // 3
        score -= 3*a
        if score == 0:
            if a >= p:
                count += 1
            elif s > 0 and a+1 >= p and a != 10 and a != 0:
                s -= 1
                count += 1
        elif score == 1:
            if a+1 >= p:
                count += 1
        else: # score == 2
            if a+1 >= p:
                count += 1
            elif s > 0 and a+2 >= p and a+2 <= 10:
                s -= 1
                count += 1
    return count

def main():
    f = open(sys.argv[1])
    T = int(f.readline())
    
    for t in range(1, T+1):
        data = [int(c) for c in f.readline().split()]
        s, p = data[1:3]
        res = solve(s, p, data[3:])
        print "Case #%d: %d" % (t, res)

if __name__ == "__main__":
    main()