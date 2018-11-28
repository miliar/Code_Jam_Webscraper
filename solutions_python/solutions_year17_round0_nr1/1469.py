def flip(pile, k):
    # check case 0 pancake in pile
    if len(pile) == 0:
        return 0
    # check case 1 pancake in pile
    if len(pile) == 1:
        if pile[0] == '+':
            return 0
        elif k == 1:
            return 1
        else:
            return "IMPOSSIBLE"
    count = 0
    left = -1
    while True:
        # starting from left, find 1st '-' pancake (n)
        n = left
        for i in xrange(max(0, left), len(pile)):
            if pile[i] == '-':
                n = i
                break
        if n == left:
            return count
        # flip k pancakes [n, n+k[
        if n + k > len(pile):
            for i in xrange(n, len(pile)):
                if pile[i] == '-':
                    return "IMPOSSIBLE"
            return count
        else:
            count = count + 1
            for i in xrange(n, n + k):
                if pile[i] == '-':
                    pile[i] = '+'
                else:
                    pile[i] = '-'
  
t = int(raw_input().strip())

for i in xrange(1, t + 1):
    pile, k = raw_input().strip().split(' ')
    pile = list(pile)
    k = int(k)
    print "Case #{}: {}".format(i, flip(pile, k))
