import sys

def solve(args):
    opos = 1
    bpos = 1
    ofree = 0
    bfree = 0
    n = int(args[0])
    turns = 0
    for i in range(n):
        tp = int(args[i*2+2])
        if args[i*2+1] == 'O':
            turn = abs(tp - opos) + 1 - ofree
            if turn < 1:
                turn = 1
            bfree += turn
            ofree = 0
            opos = tp
        elif args[i*2+1] == 'B':
            turn = abs(tp - bpos) + 1 - bfree
            if turn < 1:
                turn = 1
            ofree += turn
            bfree = 0
            bpos = tp
        else:
            assert False
        turns += turn
    return turns
            
             

def main():
    f = open(sys.argv[1])
    n = int(f.next())
    for i in range(n):
        args = [a.strip() for a in f.next().split(' ')]
        r = solve(args)
        print "Case #%d: %d" % (i+1, r)


if __name__ == '__main__':
    main()
    