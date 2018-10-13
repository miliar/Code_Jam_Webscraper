# python 3.4 !!

#from functools import lru_cache
#@lru_cache(maxsize = None)

num_trials = int(input())

def compute():
    K, L, S = map(int, input().split())
    keyboard = input()
    target = input()

    # process keyboard

    k_len = len(keyboard)
    counts = [0] * 26
    for c in keyboard:
        counts[ord(c)-ord('A')] += 1

    # probability of typing target, plus is it even typeable?

    typeable = True
    prob_once = 1.0
    for c in target:
        if (counts[ord(c)-ord('A')] == 0):
            prob_once = 0.0
            typeable = False
            break;
        else:
            prob_once *= (counts[ord(c)-ord('A')]/k_len)

    #process target

    l = len(target)

    #determine similarity
    count_opt = 0

    if (typeable == True):
        max_sim = 0
        for i in range(l-1, 0, -1):
            #    print(i, " ", target[(l-i):], " ", target[:i])
            if target[(l-i):] == target[:i]:
                max_sim = i
                break
            #print(max_sim)

        #optimal
        count_opt = 0
        pos = l
        while pos <= S:
            count_opt += 1
            pos += (l - max_sim)

    #print (count_opt)


    expected = prob_once * (S - l + 1) # expectation is linear!

    #print(counts)
    #print(prob_once)
    #print(expected)
    return count_opt - expected

for i in range (0, num_trials):
    print("Case #" + str(i+1) + ": " + str(compute()))
