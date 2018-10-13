for j in range(int(raw_input())):
    n=int(raw_input())
    list1 = [0,1,2,3,4,5,6,7,8,9]
    last=0
    early=0
    early1=0
    temp1 = 0
    temp2 =''
    num=0
    if n in list1:
        print "Case #%d: %d"%((j+1),n)
    else:
        flag3 = 0
        flag1 = 0
        flag2 = 0
        while flag3 != 1:
            flag1=0
            flag2=0
            a=[]
            m=str(n)
            a=list(m)
            for i in range(len(a)-1):
                if a[len(a)-(i+1)] >= a[len(a)-(i+2)]:
                    flag1=1
                else:
                    flag2=1
            if (flag1 == 1) and (flag2 == 1):
                flag3=0
            elif flag2 == 1:
                flag3 =0
            else:
                flag3=1                
            if flag3 == 1:
                print "Case #%d: %d"%((j+1),n)
            else:
                n=n-1
            
            
                
                
                
            
