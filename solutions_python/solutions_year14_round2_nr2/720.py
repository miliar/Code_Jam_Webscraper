def count_wins(a,b,k):
    k_list = range(k)
    count = 0
    for i in xrange(a):
        for j in xrange(b):
            x = i & j
            if x in k_list:
                count+=1
    return count

def new_lottery_game(filename):
    f = open(filename)
    out = open('new_lottery_game.out', 'w')
    cases = int(f.readline())
    c = 1
    while c <= cases:
        nums = f.readline().replace('\n','').split(' ')
        a = int(nums[0])
        b = int(nums[1])
        k = int(nums[2])
        wins = count_wins(a,b,k)
        out.write('Case #%d: %d\n' % (c, wins))
        c+=1
    f.close()
    out.close()