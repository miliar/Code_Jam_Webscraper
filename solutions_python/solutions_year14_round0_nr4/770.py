#!/usr/bin/env python
from copy import copy


def solve_war(naomi, ken):
    assert(len(naomi) == len(ken))
    points = 0
    alice = copy(naomi)
    bob = copy(ken)
#    print alice, bob

    for a in sorted(alice):
        # Assuming order of steps doesn't matter
        if a < max(bob):
            # Put in smallest beating
            candidates = filter(lambda x: x > a, bob)
#            print candidates
            move = min(candidates)
        else:
                # Or put in the smallest
            move = min(bob)
            points += 1
        bob.remove(move)
    return points


def bluff_result(alice, bob, moves):
    afterbluff_alice = alice[moves:]
    afterbluff_bob = bob[:len(bob) - moves]
    answer = 0

    assert(len(afterbluff_alice) == len(afterbluff_bob))
    for i in range(len(afterbluff_alice)):
        if afterbluff_alice[i] > afterbluff_bob[i]:
            answer += 1
    return answer


def solve_deciet(naomi, ken):
    alice = list(sorted(copy(naomi)))
    bob = list(sorted(copy(ken)))

    return max([bluff_result(alice, bob, moves)
                for moves in range(len(alice))])

if __name__ == '__main__':
    fin = open('deciet.in')
    TEST_COUNT = int(fin.readline())
    # print TEST_COUNT

    fout = open('deciet.out', 'w')
    for test in range(TEST_COUNT):
        fin.readline()
        alice = map(float, fin.readline().strip().split(' '))
        #print alice[0]
        bob = map(float, fin.readline().strip().split(' '))

        # print alice, bob
        war = solve_war(alice, bob)
        dec_war = solve_deciet(alice, bob)

        answer = 'Case #%d: %d %d' % (test + 1,  dec_war, war)
        print answer
        fout.write(answer + '\n')

    fout.close()
