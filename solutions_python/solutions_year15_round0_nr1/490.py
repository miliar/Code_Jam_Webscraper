# -*- coding: utf-8 -*-
        
        
def case(num, Smax, S):
    need = 0
    have = 0
    for index, s in enumerate(S):
        if have >= index:
            have += s
        elif s >= 0:
            need += index - have
            have = index + s
        else:
            if have >= Smax: break
    return need        

def main():
    T = int(raw_input())
    for i in xrange(T):
        Smax, SS = raw_input().split()
        Smax = int(Smax)
        S = [int(j) for j in SS]
        
        Fmin = case(i, Smax, S)
        print "Case #{}: {}".format(i+1, Fmin)

if __name__ == "__main__":
    main()
