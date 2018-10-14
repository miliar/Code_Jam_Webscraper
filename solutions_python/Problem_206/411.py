from fractions import Fraction

if __name__=='__main__':
    arr = input()
    T = int(arr)
    for x in range(T):
        arr = input().split(' ')
        D = int(arr[0])
        N = int(arr[1])
        ans = Fraction(-1,1)
        for i in range(N):
            arr = input().split(' ')
            K = int(arr[0])
            S = int(arr[1])
            if ans < 0:
                ans = Fraction(D-K,S)
            else:
                ans = max(ans,Fraction(D-K,S))
        tm = Fraction(D,1)/ans
        print("Case #"+str(x+1)+": "+str(round(tm.__float__(),6)))
    
        
    
