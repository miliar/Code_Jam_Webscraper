import sys

T = int(sys.stdin.readline())

for _ in range(T):
    out = "Case #%d: " % (_ + 1)
    N, L, H = [ int (c) for c in sys.stdin.readline().split(' ')]
    other = [ int (c) for c in sys.stdin.readline().split(' ') ]
    for __ in range(L , H + 1):
        for o in other:
            if o % __ == 0 or __ % o == 0:
                pass
            else:
                break
        else:
            out += str(__)
            print out
            break
    else:
        out += 'NO'
        print out
