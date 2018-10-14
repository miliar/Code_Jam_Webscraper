from bisect import bisect
import random


def solution(n, kens, naomis):
    
    # naomi_choice(naomis)
    # score1 = ken_best_strat(n, kens, naomis)
    war_score =  ken_strat(n, list(kens), list(naomis))
    deceitful_score = naomi_strat(n, list(kens), list(naomis))
    # print sc1, sc2
    # for i in xrange(n):
    #     print naomis[i], kens1[i], kens2[i] 
    # print
    # print
    return ' '.join(map(str,(deceitful_score, war_score)))

def naomi_strat(n, kens, naomis):
    kens.sort()
    naomis.sort()
    score = 0
    # naomi wants to be certain that she score the maximum points
    # to do so, it lures kens into using its biggest blocks against her smallest one
    # and his smallest blocks against her smallest but slightly bigger one
    for i in xrange(n):
        if kens[0] > naomis[0]:
            # naomis cannot win this round, she plays her smallest block
            naomis.pop(0)
            # kens has been lured into playing his biggest block
            kens.pop()
        else:
            # namois plays her smallest block while telling kens it's a huge block.
            naomis.pop(0)
            # ken doesn't have any bigger block so he plays his smallest block
            kens.pop(0)
            score += 1
    return score

def ken_strat(n, kens, naomis):
    score = 0
    kens.sort()
    for c in naomis:
        # Ken will always get the smallest number bigger than naomi's choice   
        # if no such number exists, return the smallest number in the array
        found = bisect(kens, c)
        if found == len(kens):
            score += 1
            found = 0
        kens.pop(found)
    return score

# def ken_best_strat(n, kens, naomis):
#     import itertools
#     best = []
#     best_score = n
#     for trial in itertools.permutations(kens):
#         sc = score(n, trial, naomis)
#         if sc < best_score:
#             best_score = sc
#             best = [trial]
#         if sc == best_score:
#             best.append(trial)
#     return best_score


def naomi_choice(naomis):
    random.shuffle(naomis)

def score(n, kens, naomis):
    score = 0
    for i in xrange(n):
        if naomis[i] > kens[i]:
            score += 1
    return score

    




if __name__ == '__main__':
    with open('test.txt') as in_stream:
        with open('result.txt', 'w') as out_stream:
            t = int(in_stream.readline())
            for c in xrange(t):
                n = int(in_stream.readline())
                naomi = map(float, in_stream.readline().strip().split(' '))
                ken = map(float, in_stream.readline().strip().split(' '))
                result = solution(n, ken, naomi)
                out_stream.write("Case #{}: {}\n".format(c+1, result))
                print c

    # with open('test.txt', 'w') as stream:
    #     stream.write('50\n')
    #     import random
    #     for _ in xrange(50):
    #         kens = set()
    #         naomis = set()
    #         n = random.randint(1, 999)
    #         while len(kens) < n:
    #             next = random.random()
    #             if next not in kens and next not in naomis:
    #                 kens.add(next)
    #         while len(naomis) < n:
    #             next = random.random()
    #             if next not in kens and next not in naomis:
    #                 naomis.add(next)
    #         stream.write('{}\n'.format(n))
    #         stream.write('{}\n'.format(' '.join(str(x) for x in naomis)))
    #         stream.write('{}\n'.format(' '.join(str(x) for x in kens)))






