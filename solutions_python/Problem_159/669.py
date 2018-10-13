from copy import copy

def method1(li):
    li2=copy(li)
    li2.insert(0,0)
    return sum([max(0,a-b) for (a,b) in zip(li2,li)])
    
def method2(li):
    li2=copy(li)
    li2.insert(0,0)
    diffs=[max(0,a-b) for (a,b) in zip(li2,li)]
    speed=max(diffs)
    def ate(a):
        if a<=speed: return a
        else: return speed
    return sum([min(a,speed) for a in li[:-1]])

if __name__=='__main__':
    cases=int(input())
    for i in range(1,cases+1):
        input()
        li=[int(e) for e in input().split()]
        a=method1(li)
        b=method2(li)
        print("Case #"+str(i)+": "+str(a)+" "+str(b))
        
