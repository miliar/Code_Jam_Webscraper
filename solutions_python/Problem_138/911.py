

def war(block_n, block_k):
    n_win = 0

    while len(block_n) > 0:
        n = block_n.pop()

        i = 0
        k = block_k[i]

        try:
            while k < n:
                i += 1
                k = block_k[i]
            block_k.remove(k)
        except (ValueError, IndexError):
            block_k = block_k[1:]
            n_win += 1

    return n_win


def dec_war(block_n, block_k):
    n_win = 0

    while len(block_n) > 0:

        if block_k[-1] < block_n[-1]:
            n_win += 1
            block_k = block_k[0:-1]
            block_n = block_n[0:-1]

        else:
            block_k = block_k[0:-1]
            block_n = block_n[1:]

#        print(block_n)
#        print(block_k)
    return n_win
#        n = block_n.pop()
#
#        i = 0
#        k = block_k[i]
#
#        try:
#            while k < n:
#                i += 1
#                k = block_k[i]
#            block_k.remove(k)
#        except (ValueError, IndexError):
#            block_k = block_k[1:]
#            n_win += 1

    return n_win



with open('D-large.in') as f:
    T = int(f.readline())

    for puzzle_count in range(T):
        _ = f.readline()
        block_n = map(float, f.readline().strip().split(' '))
        block_k = map(float, f.readline().strip().split(' '))

        block_n.sort()
        block_k.sort()

        war_ans = war(block_n[:], block_k[:])
        dec_war_ans = dec_war(block_n[:], block_k[:])

        print('Case #%s: %s %s'%(str(puzzle_count + 1), dec_war_ans, war_ans))
