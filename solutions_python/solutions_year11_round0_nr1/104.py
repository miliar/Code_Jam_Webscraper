

def read_input():
    items = raw_input().split()
    n = int(items[0])
    moves = []
    for i in range(n):
        moves.append((items[1+i*2], int(items[2+i*2])))
    return n, moves

def solve_one(t):
    n, moves = read_input()
    times = [0,0]
    pos = [1,1]
    last_time = 0
    for c,p in moves:
        if c=='O':
            rid = 0
        else:
            rid = 1
        
        d = abs(pos[rid]-p)
        push_time = max(last_time + 1, times[rid] + d + 1)
        pos[rid] = p
        times[rid] = push_time
        last_time = push_time
    print "Case #%d: %d" % (t, last_time)

def main():
    t = int(raw_input())
    for i in range(t):
        solve_one(i+1)

if __name__=='__main__':
    main()
