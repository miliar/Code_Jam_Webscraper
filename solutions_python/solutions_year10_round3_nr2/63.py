'''
Created on 2010-05-23

@author: lawford
'''

import math

def recurse2(a,b, best_l, best_h,c):
    print(str([a,b,best_l, best_h]))
    if a >= best_l and a <= best_h:
        return 0
    split = (a+b)/2
    return 1+recurse(split, b, best_l, best_h,c)

def recurse(a,b, best_l, best_h,c):
    print(str([a,b,best_l, best_h]))
    if a >= best_l and a <= best_h:
        return 0
    split = a + (b-a)/c
    return 1+recurse(split, b, best_l, best_h,c)
    

def alg2(l,p,c):
    print("===")
    cnt = recurse(l,p,p/c, p*c,c)
    return [cnt]

def alg(l,p,c):
    print("===")
    i = 0
    tmp = l
    
#    if l >= p/c:
#        return [0]
    
    tmp = tmp*c
    while tmp < p:
#        print(tmp)
        i = i+1
        tmp = tmp*c
#    if i>0 and (tmp < p):
#        i = i+1
    if i==0:
        return [0]
    print i
    return [int(math.ceil(math.log(i+1, 2)))]

if __name__ == '__main__':
    fname = "B"
#    f = open(fname+".in.txt", "r")
    f = open("/raid/downloads/firefox/"+fname+"-large.in")
    f.readline()
    cnt=1
    fout = open(fname+".out.txt", "w")

    piece1 = f.readline()
    while piece1 != '':
        [l,p,c] = map(int, piece1.split(" "))
        result = alg(l,p,c)
        fout.write("Case #"+str(cnt)+": "+" ".join(map(str, result))+"\n")
        piece1 = f.readline()
        cnt = cnt+1
    fout.close()
    f.close()
