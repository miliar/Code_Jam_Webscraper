#!/usr/bin/python
# coding: UTF-8

def checkElf(P, Q):
    if P > Q:
        return "impossible"
    elif P==Q and P!=1:
        return "impossible"
    elif P==Q and P==1:
        return "0"
    else:
        if P == 0:
            return "impossible"
        elif Q%2 == 1:
            return "impossible"
        else:
            gcd_pq = gcd(P,Q)
            P = P/gcd_pq
            Q = Q/gcd_pq
            # print Q
            if check2(Q):
                generation = 0
                while True:
                    Q = Q / 2
                    generation+=1
                    if P/Q>=1:
                        return str(generation)
            else:
                return "impossible"


def gcd(a,b):
    if b == 0: return a
    return gcd(b, a % b)


def check2(Q):
    for n in range(40):
        # print 2**n
        if 2**n == Q:
            return True
        elif 2**n > Q:
            return False



# txtfile = open('A-small-attempt0.in').read()
txtfile = open('A-large.in').read()
# txtfile = open('test_a.txt').read()
cases = txtfile.split('\n')

case_num = int(cases[0])

obj = open("a_large_ans.txt", "w")

# print gcd(3, 4)

for a in range(case_num):
    temp = cases[1+a].split('/')
    # print 'Case #'+str(a+1)+': '+checkElf(int(temp[0]), int(temp[1]))
    print >>obj, 'Case #'+str(a+1)+': '+checkElf(int(temp[0]), int(temp[1]))
