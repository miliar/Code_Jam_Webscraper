import copy
import collections as c
from functools import reduce
import functools

def main():
    T = int(input())

    for T in range(T):
        N = int(input())
        print("Case #{}: {}".format(T+1, solve(N)))
        
def solve(N):
    words = tuple(input() for i in range(N))
    result = lolwut(words, 0)
    if result > 999999999:
        return "Fegla Won"
    else:
        return result

@functools.lru_cache(maxsize=None)
def lolwut(words, cost):
#    if len(list(filter(lambda x: x is part, words))) == len(words):
    if len(list(filter(lambda x: len(x) is 0, words))):
        first = words[0]
        if len(list(filter(lambda x: x is first, words))) == len(words):
            return cost
        else:
            return 99999999999
    else:
        least_cost = 9999999999
        max_len = len(max(words, key=len))

        first = words[0][0]
        first_flag = len(list(filter(lambda x: x[0] is first, words))) == len(words)

        for i, word in enumerate(words):
            # Delete case
            if len(word) > 1 and word[1] is word[0]:
                #print("Bef: ",words)
                l = list(words)
                l[i] = l[i][1:]
                deleted = tuple(l)
                #print("After: ",deleted)
                least_cost = min(least_cost, lolwut(deleted, cost + 1))

            if first_flag:
                #print("Bef:", words)
                insert = tuple(words[ni][1:] if ni is not i else word for ni in range(len(words)))
                #print("Af:", insert)
                least_cost = min(least_cost, lolwut(insert, cost + 1))
        
        # Do nothing case
        if first_flag:
            nothing = tuple(word[1:] for word in words)
            least_cost = min(least_cost, lolwut(nothing, cost))
        return least_cost

def alleq(l):
    first_word = l[0]
    for word in l:
        if word != first_word:
            return False
    return True

if __name__ == '__main__':
    main()






