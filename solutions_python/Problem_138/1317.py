#!/usr/bin/env pypy

def solution():
    N = int(raw_input())
    naomi = [float(x) for x in raw_input().split()]
    ken = [float(x) for x in raw_input().split()]

    naomi.sort()
    ken.sort()

    naomi_saved = list(naomi)
    ken_saved = list(ken)
    
    dwar_points = 0
    while len(naomi) > 0:
        naomi_chosen = naomi.pop(0)
        if naomi_chosen > ken[0]:
            # naomi lies that chosen is bigger than all of Ken's
            ken.pop(0)
            dwar_points +=1
        else:
            # naomi lies that chosen is slightly smaller than ken's largest
            # point goes to ken but he spends his largest
            ken.pop()

    naomi = naomi_saved
    ken = ken_saved

    war_points = 0
    while len(naomi) > 0:
         naomi_chosen = naomi.pop()
         if naomi_chosen > ken[-1]:
            war_points += 1
            ken.pop(0)
         else:
            ken.pop()

    return "%s %s" % (dwar_points, war_points) 

T = int(raw_input())

for i in range(T):
    print "Case #%s: %s" % (i+1, solution())

