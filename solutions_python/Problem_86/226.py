import sys
import math
sqrt = math.sqrt

def find_gcd(a, b):
    if (a < b):
        a, b = b, a
    while b != 0:
        a, b = b, a%b
    return a 
def find_lcd(x,y):
    global gcd
    lcd=(x*y)/gcd
    return lcd

def factors(n):  
    fact=[1,n]  
    check=2  
    rootn=sqrt(n)  
    while check<rootn:  
        if n%check==0:  
            fact.append(check)  
            fact.append(n/check)  
        check+=1  
    if rootn==check:  
        fact.append(check)  
        fact.sort()  
    return fact

# find prime factors of a number
def primefactors(x):
    factorlist=[]
    loop=2
    while loop<=x:
        if x%loop==0:
            x/=loop
            factorlist.append(loop)
        else:
            loop+=1
    return set(factorlist)

def TestHarm(x,y):
    if x % y == 0 or y % x == 0:
        return True
    return False
if __name__ == "__main__":
    if len(sys.argv) == 2:
        f = open(sys.argv[1], "r")
        T = int(f.readline().strip())
        for _t in range(T):
            N, L, H = map(int, f.readline().strip().split())
            A = map(int, f.readline().strip().split())

            for i in range(L, H+1):
                find = True
                for a in A:
                    if not TestHarm(i, a):
                        find = False
                        break #try next number
                if find:
                    break
            print "Case #%d: %s" %(_t+1, ["NO", str(i)][find])
                
            
            
        f.close()
