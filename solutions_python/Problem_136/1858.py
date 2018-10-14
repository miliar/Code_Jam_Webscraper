import sys

readline = sys.stdin.readline

def test_case():
    C, F, X = [ float(s) for s in readline().split() ]
    t = 0
    n = 0
    while (X  / (2 + F * n)) > (
        (C / (2 + F * n)) + (X / (2 + F * (n+1)))
    ):
        t += C / (2 + F * n)
        n += 1
    t += (X / (2 + F * n))
    return '%.7f' % t

def main():
    T = int(readline())
    for i in range(1,T+1):
        print("Case #{i}: {result}".format(
            i=i, result=test_case()
        ))

if __name__ == '__main__':
    main()

