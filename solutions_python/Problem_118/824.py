# coding: utf8

def scan():
    while True:
        for w in input().split():
            yield w

words = scan()

def scans(num=-1):
    return (next(words) for i in range(num)) if num >= 0 else next(words)

def scani(num=-1):
    return (int(value) for value in scans(num)) if num >= 0 else int(scans())

def scanf(num=-1):
    return (float(value) for value in scans(num)) if num >= 0 else float(scans())

#------------------------------------------------------------------------------
import math

for case in range(1, scani() + 1):
    a, b = scani(2)
    sa = math.sqrt(a)
    sa = int(sa) if sa % 1 == 0 else int(sa) + 1
    sb = int(math.sqrt(b))
    def fairs(head, tail):
        l = len(str(head))
        is_odd = (l % 2)
        hl = l // 2 + 1 if is_odd else l // 2
        hv = max(int(head**(-10*(l-hl))), 1)
        carry = 10
        while True:
            v = hv
            sv = hv // 10 if is_odd else hv
            while sv > 0:
                v = v * 10 + sv % 10
                sv = sv // 10
            if v > tail: break
            if v >= head: yield v
            hv += 1
            if hv % carry == 0:
                if is_odd: hv = hv // 10
                else: carry = carry * 10
                is_odd = not is_odd
            
    def is_fair(value):
        text = str(value)
        l = len(text)
        for i in range(l // 2):
            if text[i] != text[l - i - 1]: return False
        return True

    res = 0
    for v in fairs(sa, sb):
        if is_fair(v * v):
            res += 1
    print("Case #{0}: {1}".format(case, res))
