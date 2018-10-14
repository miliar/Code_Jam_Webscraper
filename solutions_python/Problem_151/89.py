import collections
import copy
import itertools

MOD = 1000000007

def calc_prefixes(s):
    result = set()
    for i in range(len(s)+1):
        result.add(s[:i])
    return result

def calc_prefixes_ss(ss):
    results = set()
    for s in ss:
        result = calc_prefixes(s)
        results |= result
    return results

def split(S, N, splitted, result):
    if not S:
        result.append(copy.deepcopy(splitted))
        #yield copy.deepcopy(splitted)
        #return

    else:
        for i in range(N):
            splitted[i].append(S[0])
            split(S[1:], N, splitted, result)
            splitted[i].pop()

def lala(S, N):
    #for i in itertools.combinations
    result = []

    splitted = {}
    for i in range(N):
        splitted[i] = collections.deque()
    split(S, N, splitted, result)

    max_nums = -1
    count_max_nums = 0
    #for splitted in split(S, N, splitted, result):
    for splitted in result:
        #print(splitted)
        nums = 0
        for key in splitted:
            nums += len(calc_prefixes_ss(splitted[key]))

        if max_nums < nums:
            max_nums = nums
            count_max_nums = 1
        elif max_nums == nums:
            count_max_nums += 1
        
    return (max_nums, count_max_nums % MOD)


def solve(filename):
    f = open(filename)

    T = int(f.readline().strip())
    for i in range(T):
        line = list(map(int, f.readline().strip().split()))
        M, N = line[0], line[1]
        S = []
        for j in range(M):
            S.append(f.readline().strip())
        X, Y = lala(S, N)


        print("Case #%s: %s %s" % (i+1, X, Y))

if __name__ == "__main__":
    solve("D-small-attempt1.in")
    #solve("i4.txt")
    #print calc_prefixes_ss(["ABCDE", "ABCDF"])
    # print test([3])
    # print test([1, 2, 3])
    # print test([1, 3, 2])
    #print(list(powerset([1,2,3])))
