from itertools import zip_longest
import itertools
import ipdb

def parse(input_file, output_file):
    with open(input_file) as f:
        T = int(f.readline().split()[0])
        out = open(output_file, 'w')
        solu = Solu(12)
        for i in range(T):
            N, R, P, S = map(int, f.readline().split())
            sol = solu.solve(N, R, P, S)
            line = "Case #"+str(i+1)+": "+str(sol)
            print(line)
            out.write(line+'\n')
    return


def trans(d):
    if int(d) == 0:
        return 'P'
    if int(d) == 1:
        return 'R'
    if int(d) == 2:
        return 'S'



def small_solve(N, R, P, S):
    all_perm = itertools.permutations([0]*P+[1]*R+[2]*S)
    for perm in all_perm:
        if check(perm):
            return ''.join(map(trans, perm))
    return 'IMPOSSIBLE'


def check(perm):
    if len(perm) == 1:
        return True
    if not perm:
        raise ValueError
    winners = []
    #firsts = range(len(perm))[0::2]
    firsts = range(0, len(perm), 2)
    seconds = range(1, len(perm), 2)
    for f, s in zip(firsts, seconds):
        if perm[f] == perm[s]:
            return False
        summ = perm[f] + perm[s]
        if summ == 3:
            winners.append(1)
        elif summ == 2:
            winners.append(2)
        elif summ == 1:
            winners.append(0)
        else:
            raise ValueError
    return check(winners)

def get_dist(N):
    ret = []
    for final in range(3):
        counts = [0, 0, 0]
        counts[final] += 1
        rounds = N
        while rounds != 0:
            newcounts = [0, 0, 0]
            newcounts[0] += counts[0]
            newcounts[0] += counts[2]
            newcounts[1] += counts[0]
            newcounts[1] += counts[1]
            newcounts[2] += counts[1]
            newcounts[2] += counts[2]
            rounds -= 1
            counts = newcounts
        ret.append(counts)
    return ret



class Solu(object):
    def __init__(self, N):
        #solve up to N
        self.N = N
        self.res = dict()
        # key is N; next level, key is the surviving
        #self.res[1] = {0:[0, 1], 1:[1, 2], 2:[0, 2]}
        self.res[1] = {0:'01', 1:'12', 2:'02'}

        self.popu()

    def popu(self):
        for n in range(2, self.N+1):
            nsol = {0:None, 1:None, 2:None}
            for surviving in range(3):
                first_dig = int(self.res[1][surviving][0])
                second_dig = int(self.res[1][surviving][1])
                first_sol = self.res[n-1][first_dig]
                second_sol = self.res[n-1][second_dig]
                nsol[surviving] = min(first_sol+second_sol, second_sol+first_sol)

            self.res[n] = nsol


    def solve(self, N, R, P, S):
        dists = get_dist(N)
        if [R, P, S] not in dists:
            return 'IMPOSSIBLE'
        surviving = dists.index([P, R, S])
        ret = self.res[N][surviving]
        return ''.join(map(trans, ret))


dir = "./"

'''
'''
input_file = dir+"A-test.txt"
output_file = dir+"A-test.out.txt"

input_file = dir+"A-small-attempt0.in"
output_file = dir+"A-small-attempt0.txt"

input_file = dir+"A-small-attempt0.in"
output_file = dir+"A-small-attempt0.withLarge.txt"

input_file = dir+"A-large.in"
output_file = dir+"A-large.txt"
'''
'''

parse(input_file, output_file)



