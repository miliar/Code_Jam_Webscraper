#!/usr/bin/ptyhon3
# -*- coding: Utf-8 -*-


class Quat :
    def __init__(self, sign, val) :
        self.sign = sign
        self.val = val

    def __mul__(self, q) :
        if self.val == q.val :
            return Quat(-1 * self.sign * q.sign, "")
        elif self.val == "" :
            return Quat(self.sign * q.sign, q.val)
        elif q.val == "" :
            return Quat(self.sign * q.sign, self.val)
        elif self.val == 'i' :
            if q.val == 'j' :
                return Quat(self.sign * q.sign, 'k')
            elif q.val == 'k' :
                return Quat(-1 * self.sign * q.sign, 'j')
        elif self.val == 'j' :
            if q.val == 'k' :
                return Quat(self.sign * q.sign, 'i')
            elif q.val == 'i' :
                return Quat(-1 * self.sign * q.sign, 'k')
        elif self.val == 'k' :
            if q.val == 'i' :
                return Quat(self.sign * q.sign, 'j')
            elif q.val == 'j' :
                return Quat(-1 * self.sign * q.sign, 'i')

    def pow(self, n) :
        if self.val == "" :
            return Quat(self.sign ** n, '')
        else :
            if n%2 == 0 :
                return Quat((-1)**(n/2), '')
            else :
                return Quat(self.sign * (-1)**((n-1)/2), self.val)

    def copy(self) :
        return Quat(self.sign, self.val)

    def __eq__(self, q) :
        return self.sign == q.sign and self.val == q.val

    def __str__(self) :
        return ("-" if self.sign == -1 else "")+("1" if self.val == "" else self.val)


def find_i(r, s) :
    rtab = [r.pow(0), r.pow(1), r.pow(2), r.pow(3)]
    best = 4
    bestl = 0
    for i in range(4) :
        if rtab[i] == Quat(1, 'i') :
            best = min(i, best)
    for j in range(len(s)) :
        for i in range(best) :
            rtab[i] = rtab[i] * Quat(1, s[j])
            if rtab[i] == Quat(1, 'i') and i < best :
                best = i
                bestl = j+1
        if best == 0 :
            return best, bestl
    return best, bestl

def find_k(r, s) :
    rtab = [r.pow(0), r.pow(1), r.pow(2), r.pow(3)]
    best = 4
    bestl = 0
    for i in range(4) :
        if rtab[i] == Quat(1, 'k') :
            best = min(i, best)
    for j in range(len(s)-1, -1, -1) :
        for i in range(best) :
            rtab[i] = Quat(1, s[j]) * rtab[i]
            if rtab[i] == Quat(1, 'k') and i < best :
                best = i
                bestl = len(s)-j
        if best == 0 :
            return best, bestl
    return best, bestl

def solve(s, t) :
    reduced = Quat(1, "")
    for c in s :
        reduced = reduced * Quat(1, c)
#    print(reduced)
#    print(reduced.pow(t))
    if reduced.pow(t) != Quat(-1, '') :
        return False
    else :
        n, nl = find_i(reduced, s)
#        print("n, nl = %d, %d" % (n, nl))
        m, ml = find_k(reduced, s)
#        print("m, ml = %d, %d" % (m, ml))
        if max(n,m) == 4 :
            return False
        else :
            l = n + m
            if nl != 0 or ml != 0 :
                l+=1
            if nl + ml > len(s) :
                l+=1
            return l <= t


    
output = list()
for n in range(int(input())) :
    t = int(input().split()[1])
    s = input()
    output.append("Case #%d: %s" % (n+1, "YES" if solve(s, t) else "NO"))
print("\n".join(output))

