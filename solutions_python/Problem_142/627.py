#!/usr/bin/env python3

from math import floor, ceil

def round_it(x):
    if ceil(x) - x == x - floor(x):
        return ceil(x)
    else:
        return round(x)

def slice_word(w):
    if not w:
        raise ValueError(w)
    slices = [(w[0], 1)]
    for letter in w[1:]:
        if letter == slices[-1][0]:
            slices[-1] = (letter, slices[-1][1] + 1)
        else:
            slices.append((letter, 1))
    return slices

T = int(input())
for t in range(1,T+1):
    N = int(input())
    words = []
    answer = None

    word_len = -1
    letters = None
    for _ in range(N):
        words.append(slice_word(input()))
        if word_len == -1:
            word_len = len(words[-1])
        elif len(words[-1]) != word_len:
            answer = "Fegla Won"
            break

        if letters is None:
            letters = ''.join(x[0] for x in words[-1])
        elif letters != ''.join(x[0] for x in words[-1]):
            answer = "Fegla Won"
            break
    else:
        answer = 0
        #print(words)
        for i in range(word_len):
            occ = [word[i][1] for word in words]
            #avg = sum(occ)/N
            def median(l):
                sorted_l = sorted(l)
                length = len(l)
                if length % 2 == 0:
                    return sorted_l[length//2]
                else:
                    return 0.5 * (sorted_l[length//2] + sorted_l[1+length//2])
            avg = median(occ)
            rounded = round_it(avg)
            answer += sum(map(lambda x:abs(x - rounded),
                              filter(lambda x: x!=rounded, occ)))
            #n_diff = len(list(filter(lambda x: x!=rounded, occ)))
            #print("AVG: %d" % avg)
            #print("diff %d" % n_diff)
    print("Case #%d: %s" % (t, answer))
