from sys import argv
import math


#f = open("ex_D.in")

#f = open("D-small-attempt0.in")
f = open("D-large.in")
cases = int(f.readline())

def War(N, Naomi, Ken):
    count = 0
    Naomi.sort()
    Ken.sort()
    A = Naomi[:]
    B = Ken[:]
    for i in range(int(N[0])):
        a = A.pop()
        if a > B[-1]:
            b = B.pop(0)
            count += 1
            #print "count", count, "a", a, "b", b 
        else:
            b = B.pop()
            #print "a",a, "b",b
    return count
    

for i in range(cases):
    N = map(int, f.readline().split())
    Naomi = map(float, f.readline().split())
    Ken = map(float, f.readline().split())
    war_result = War(N, Naomi, Ken)
    deceitful_war_result = N[0] - War(N, Ken, Naomi)
    print "Case #%d:" %(i+1), deceitful_war_result, war_result
