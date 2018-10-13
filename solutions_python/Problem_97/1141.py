
def f(A, B):
    assert A <= B
    result = 0
    for v in range(A, B):
        p, q = 10, 1
        while v > p:
            r = v % p
            q = v / p
            t = int(str(r) + str(q))
            ss = set()
            if v < t <= B:
                ss.add(t)
            result += len(ss)
            p, q = 10 * p, 10 * q
                
            
    return result


def main():
    N = int(raw_input())
    for i in range(N):
        line = map(int, raw_input().split(' '))
        print "Case #{0}: {1}".format(i+1, f(*line))


if __name__ == "__main__":
    main()
