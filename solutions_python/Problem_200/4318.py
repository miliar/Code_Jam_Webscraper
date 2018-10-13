def tatiana():
        def check(n):
                if n//10==0:
                        return 1
                num=n//10
                prevnum=n%10
                while num != 0:
                        if (num%10)>prevnum:
                                break
                        prevnum= num%10
                        num= num//10
                if num==0:
                        return 1
                return 0
        test=int(input())
        numbers=[]
        for i in range(test):
                numbers.append(int(input()))
        res=[]
        for i in range(test):
                n=numbers[i]
                for j in range(0,1001100110011001100110011001100110011001):
                        if (check(n-j)):
                                res.append(n-j)
                                break
        for i in range(1,test+1):
                print("Case","#"+str(i)+":",res[i-1])
tatiana()    
