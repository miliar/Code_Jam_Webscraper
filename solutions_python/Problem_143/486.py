
def calc(a,b,k):
    count = 0
    #for i in range(0, k):
    for la in range(0, a):
        for lb in range(0, b):
            if (la & lb) < k:
                count += 1
    return count



#with open('sample2.in') as f:
with open('B-small-attempt0.in') as f:
    T = int(f.readline())

    for puzzle_count in range(T):
        a, b, k = map(int, (f.readline().split(' ')))

        ans = calc(a,b,k)

        print('Case #%s: %s'%(str(puzzle_count + 1), str(ans)))
