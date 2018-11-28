import sys

def next(score, my, your):
    my_wood = my[0]
    if my_wood > your[-1]:
        your_wood = your[0]
    else:
        your_wood = min([w for w in your if w >= my_wood])
    if my_wood > your_wood:
        score += 1
    my = my[1:]
    your.remove(your_wood)
    return (score, my, your)

def cheat_next(score, my, your):
    my_wood = my[0]
    if my_wood > your[0]:
        your_wood = your[0]
        your = your[1:]
    else:
        your_wood = your[-1]
        your = your[:-1]
    if my_wood > your_wood:
        score += 1
    my = my[1:]
    return (score, my, your)
    
T = int(sys.stdin.readline())
for i in range(1, T+1):
    n = int(sys.stdin.readline())
    my_save = sorted(map(float, sys.stdin.readline().strip().split(' ')))
    your_save = sorted(map(float, sys.stdin.readline().strip().split(' ')))
    score = 0
    score_cheat = 0
    my = my_save[:]
    your = your_save[:]
    my_cheat = my_save[:]
    your_cheat = your_save[:]
    for step in range(n):
        score, my, your = next(score, my, your)
        score_cheat, my_cheat, your_cheat = cheat_next(score_cheat, my_cheat, your_cheat)
    print "Case #{0}: {1} {2}".format(i, score_cheat, score)
    


