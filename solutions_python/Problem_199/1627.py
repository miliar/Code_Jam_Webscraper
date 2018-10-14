# @Author: Tushar Jain <tshrjn>
# @Date:   2017-04-09T05:32:21+05:30
# @Filename: flipper.py
# @Last modified by:   tshrjn
# @Last modified time: 2017-04-09T06:22:01+05:30

def flip(l):
    # print(l)
    for idx, i in enumerate(l):
        if i == 0:
            l[idx] = 1
        if i == 1:
            l[idx] = 0
    # print(l)
    return l

def pancakes(s,k):
    counter = 0
    for idx in range(len(s)-k+1):
        if s[idx] == 0: # don't use cake
            s = s[:idx] + flip(s[idx:idx+k]) + s[idx+k:]
            # print(cake, idx, s)
            counter += 1
    # print(set(s), s)
    if set(s) == {1}:
        return counter
    else:
        return "IMPOSSIBLE"


t = int(input())
for i in range(t):
    s,k = input().split()
    k = int(k)
    s = s.replace("-", "0")
    s = s.replace("+", "1")
    s = list(map(int,s))
    ans = pancakes(s,k)
    print("Case #{}: {}".format(i+1 , ans))
