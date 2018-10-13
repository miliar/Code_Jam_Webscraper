from copy import copy

__author__ = 'danolsen'

with open('input/d-large.txt') as fin:
    cases = int(fin.readline())

    with open('output/d-large.txt', 'w') as out:
        for i in range(1, cases + 1):
            num_blocks = int(fin.readline())
            naomi_weights = fin.readline().split()
            ken_weights = fin.readline().split()

            naomi_weights = [float(x) for x in naomi_weights]
            ken_weights = [float(x) for x in ken_weights]

            naomi_original_weights = copy(naomi_weights)
            ken_original_weights = copy(ken_weights)

            naomi_weights.sort()
            ken_weights.sort()

            naomi_original_weights.sort()
            ken_original_weights.sort()

            n_score1 = 0
            k_score1 = 0

            for j in range(0, num_blocks):

                if naomi_weights[-1] > ken_weights[-1]:
                    k_played = ken_weights[-1]
                    for n in naomi_weights:
                        n_played = n
                        if n > k_played:
                            break

                else:
                    n_played = naomi_weights[0]
                    k_played = ken_weights[-1]

                if n_played > k_played:
                    n_score1 += 1
                else:
                    k_score1 += 1

                naomi_weights.remove(n_played)
                ken_weights.remove(k_played)

            naomi_weights = copy(naomi_original_weights)
            ken_weights = copy(ken_original_weights)

            n_score2 = 0
            k_score2 = 0

            curr_diff = 0
            for j in range(0, num_blocks):
                n_played = naomi_weights[-1]

                if n_played > ken_weights[-1]:
                    k_played = ken_weights[0]
                else:
                    k_played = ken_weights[-1]
                    for k in ken_weights:
                        k_played = k
                        if k > n_played:
                            break

                if n_played > k_played:
                    n_score2 += 1
                else:
                    k_score2 += 1

                naomi_weights.remove(n_played)
                ken_weights.remove(k_played)

            print 'Case #%d: %d %d' % (i, n_score1, n_score2)
            out.write('Case #%d: %d %d\n' % (i, n_score1, n_score2))

