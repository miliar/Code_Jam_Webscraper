from __future__ import print_function

def calc(offset, coef, C, X):
    getC = offset + C / coef
    getX = offset + X / coef
    return (getC, getX)

if __name__ == '__main__':
    n = int(raw_input())
    for pb_i in xrange(n):
        # Solve problem i
        C, F, X = [float(_) for _ in raw_input().split()]

        coef = 2.
        result = calc(0.,coef,C,X)
        temp = result
        while(temp[1] <= result[1]):
            result = temp
            coef += F
            temp = calc(result[0], coef, C, X)
        
        print("Case #{}: {}".format(pb_i+1, result[1]))
