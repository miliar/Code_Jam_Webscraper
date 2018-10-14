import sys

if __name__ == "__main__":
    f = sys.stdin
    if len(sys.argv) >= 2:
        fn = sys.argv[1]
        if fn != '-':
            f = open(fn)

    t = int(f.readline())
    for _t in range(t):
        a = int(f.readline())
        vals = [int(val) for val in ([f.readline()\
                                      for i in range(4)][a-1]).split()]

        a = int(f.readline())
        vals2 = [int(val) for val in ([f.readline()\
                                      for i in range(4)][a-1]).split()]

        insect = set(vals).intersection(set(vals2))

        det = len(insect)
        res = [lambda x: 'Volunteer cheated!', lambda x: str(x.pop()), \
               lambda x: 'Bad magician!']

        print ("Case #%d: %s"%(_t+1, res[2 if det > 1 else det](insect)))
