'''
---+--+-
---+-+-+
---++-++
------++
'''

def isdone(pancakes):
    for i in pancakes:
        if i == "-":
            return False
    return True

def flip(pancakes, itr, k):
    for i in range(k):
        if pancakes[itr] == "-":
            pancakes[itr] = "+"
        else:
            pancakes[itr] = "-"
        itr -= 1

T = int(input())
for i in range(1,T+1):
    S = input().split(' ')
    pancakes = list(S[0])
    k = int(S[1])
    itr = len(pancakes)-1
    num_flips = 0
    while itr != 0 or not isdone(pancakes):
        if pancakes[itr] == "+":
            itr -= 1
        elif itr - k + 1 < 0:
            print("Case #{}: IMPOSSIBLE".format(i))
            break
        else:
            flip(pancakes,itr,k)
            num_flips += 1
            itr -= 1
    if isdone(pancakes):
        print("CASE #{}: {}".format(i, num_flips))

        


