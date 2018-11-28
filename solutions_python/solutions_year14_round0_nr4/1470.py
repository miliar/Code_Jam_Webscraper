from collections import deque
from copy import deepcopy
class Backwards(float):
    def __lt__(self, other):
        return not float.__le__(self, other)
    def __le__(self, other):
        return not float.__lt__(self, other)
    def __gt__(self, other):
        return not float.__ge__(self, other)
    def __ge__(self, other):
        return not float.__gt__(self, other) 

# TODO: Ensure these work in the case that naomis largest < kens second largest, etc.
def deceitful_war(naomi, ken):
    points = 0
    while len(naomi) != 0:
        if naomi[-1] > ken[-1]:
            #print("Naomi told {0}, Ken Played {1}. Naomi Played {2}.".format(naomi[-1], ken[-1], naomi[-1]))
            points += 1
            naomi.pop()
            ken.pop()
        else:
            told = (ken[-1] + naomi[-1]) / 2
            #print("Naomi told {0}, Ken Played {1}. Naomi Played {2}.".format(told, ken[-1], naomi[0]))
            ken.pop()
            naomi.popleft()
    return points

def war(naomi, ken):
    points = 0
    while len(naomi) != 0:
        message = "LOST"
        if naomi[-1] > ken[-1]:
            message = "WON"
            points += 1
            #print("Ken Played {0}. Naomi Played {1}. {2}".format(ken[0], naomi[-1], message))
            naomi.pop()
            ken.popleft()
        else:
            #print("Ken Played {0}. Naomi Played {1}. {2}".format(ken[-1], naomi[-1], message))
            naomi.pop()
            ken.pop()
    return points

T = int(input())
for t in range(1,T+1):
    N = int(input())
    naomi = deque(sorted([float(x) for x in input().split()]))
    ken = deque(sorted([float(x) for x in input().split()]))
    d = deceitful_war(deepcopy(naomi), deepcopy(ken))
    #print("\n")
    print("Case #{0}: {1} {2}".format(t, d, war(naomi, ken)))
