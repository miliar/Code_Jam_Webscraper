#Round 1b 2017 Problem a

def main():
    t = int(raw_input())
    for i in xrange(1, t+1):
        d,n = [int(s) for s in raw_input().split(" ")]
        table = []
        for j in xrange(n):
            table.append([int(s) for s in raw_input().split(" ")])
        print "Case #{}: {}".format(i, horse(d,n,table))

def horse(d,n,table):
    horse = []
    for i in xrange(n):
        horse.append((d-table[i][0])/float(table[i][1]))
    return d/max(horse)


def input():
    t = int(raw_input())
    for i in xrange(1, t+1):
        n = int(raw_input())
        print "Case #{}:".format(i)
        for j in xrange(n):
            print raw_input()

if __name__ == '__main__':
    main()
