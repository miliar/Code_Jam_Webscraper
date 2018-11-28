for j in range(int(raw_input())):
    n=int(raw_input())
    array= [0,1,2,3,4,5,6,7,8,9]
    if n in array:
        print "Case #%d: %d"%((j+1),n)
    else:
        a3 = 0
        a1 = 0
        a2 = 0
        while a3 != 1:
            a1=0
            a2=0
            a=[]
            m=str(n)
            a=list(m)
            for i in range(len(a)-1):
                if a[len(a)-(i+1)] >= a[len(a)-(i+2)]:
                    a1=1
                else:
                    a2=1
            if (a1 == 1) and (a2 == 1):
                a3=0
            elif a2 == 1:
                a3 =0
            else:
                a3=1                
            if a3 == 1:
                print "Case #%d: %d"%((j+1),n)
            else:
                n=n-1
            
            
                
                
                
            
