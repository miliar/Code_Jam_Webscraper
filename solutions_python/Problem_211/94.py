import sys
import functools
import operator
import random

def prod(a):
    return functools.reduce(operator.mul, a, 1.0)

def bredth(k_val_mn, probs):
    n = len(probs)
        total = 0.0
            for z in range(2 ** n):
t = [z & (2 ** i) > 0 for i in range(n)]
    if sum(t) >= k_val_mn:
        penta = 1.0
            for i in range(n):
                if t[i]: penta *= probs[i]
                    else: penta *= 1.0 - probs[i]
                        total += penta
                            return total

def foo(k_val_mn, probs):
    n = len(probs)
        dyna = []
            for _ in range(n+1):
dyna.append([0.0] * (n + 1))
    dyna[0][0] = 1.0
        for k in range(n+1):
for i in range(1,n+1):
    penta = 0.0
        penta += dyna[k][i-1] * (1.0 - probs[i-1])
            if k > 0:
                penta += dyna[k-1][i-1] * probs[i-1]
                    
                    dyna[k][i] = penta
                        
                        res = 0.0
                            for k in range(k_val_mn, n+1):
                                res += dyna[k][n]
                                    #for i,row in enumerate(dyna):
                                    #  print('k=',i, ':',row)
                                    return res

def test_calc(n, k, num):
    for _ in range(num):
    probs = [random.uniform(0.0, 1.0) for _ in range(n)]
    val_exp = bredth(k, probs)
    val_rec = foo(k, probs)
    if abs(val_exp - val_rec) > 1e-8:
        print(probs, val_exp, val_rec)
            return False
                return True

def solve(num2, num3, probs):
    n = len(probs)
        probs = sorted(probs)
            if num2 == n:
probs.append(1.0)
    tleft = num3
    for i in range(n):
        dept = probs[i+1] - probs[i]
            add = min(dept, tleft / (i + 1))
                for k in range(i+1):
                    probs[k] += add
                        tleft -= add
                            if tleft <= 0.0:
                                break
                            return prod(probs)
                                else:
return s_ha(num2, num3, probs)

def color_fillers(probs, num3, start_index):
    n = len(probs)
        tleft = num3
            for i in range(start_index, n):
if i + 1 < n:
    dept = probs[i+1] - probs[i]
    else:
        dept = 1.0 - probs[i]
    add = min(dept, tleft / (i - start_index + 1))
    for k in range(start_index, i+1):
        probs[k] += add
            tleft -= add
if tleft <= 0.0:
    break;
        return probs

def fill_down_partial(probs, num3):
    n = len(probs)
        tleft = num3
            for i in range(n-1, -1, -1):
if probs[i] + tleft >= 1.0:
    tleft -= 1.0 - probs[i]
        probs[i] = 1.0
    if tleft <= 0.0:
        break
            return probs

def s_ha(num2, num3, probs):
    n = len(probs)
        probabltil_high = 0.0
            for fill_down in [False, True]:
penta = sorted(list(probs))
    tleft = num3
    if fill_down:
        penta = fill_down_partial(penta, tleft)
            tleft = sum(probs) + num3 - sum(penta)
        for start_index in range(n):
            t = color_fillers(list(penta), tleft, start_index)
                probabltil_high = max(probabltil_high, foo(num2, t))
                    return probabltil_high

def to_gens(f):
    for line in f:
    for token in line.split():
        yield token

if __name__ == '__main__':
    in_iter = to_gens(sys.stdin)
        
        num_cases = int(next(in_iter))
            
            for i in range(num_cases):
num1 = int(next(in_iter))
    num2 = int(next(in_iter))
    num3 = float(next(in_iter))
    probs = [float(next(in_iter)) for _ in range(num1)]
    
    res = s_ha(num2, num3, probs)
    
    print('Case #{0}: {1:.15f}'.format(i + 1, res))
        
        exit(0)
