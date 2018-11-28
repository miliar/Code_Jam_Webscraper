import sys


T = int(input())
for testno in xrange(1, T + 1):
    data = sys.stdin.readline().split()[1:]
    moves = zip(data[0::2], map(int, data[1::2]))

    p = { 'O': 1, 'B': 1 }

    answer = 0

    def go(fr, to):
        if fr == to:
            return fr
        return fr + 1 if fr < to else fr - 1

    for moveno, move in enumerate(moves):
        #print move

        def next(letter):
            for next_move in moves[moveno:]:
                if next_move[0] == letter:
                    return next_move[1]
            else:
                return p[letter]

        n = { 'O': next('O'), 'B': next('B') }

        #print p
        #print n

        def finished():
            return p[move[0]] == move[1]

        while True:
            answer += 1
            last = finished()
            for letter in ('O', 'B'):
                p[letter] = go(p[letter], n[letter])
            if last:
                break

    print 'Case #{0}: {1}'.format(testno, answer)
