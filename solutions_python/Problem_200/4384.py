def tidy():
        def verify(number):
                if number//10==0:
                        return 1
                num=number//10
                prevnum=number%10
                while num != 0:
                        if (num%10)>prevnum:
                                break
                        prevnum= num%10
                        num= num//10
                if num==0:
                        return 1
                return 0
        totalTest=int(input())
        numbers=[]
        for i in range(totalTest):
                numbers.append(int(input()))
        result=[]
        for i in range(totalTest):
                n=numbers[i]
                for j in range(0,1001100110011001100110011001100110011001):
                        if (verify(n-j)):
                                result.append(n-j)
                                break
        for i in range(1,totalTest+1):
                print("Case","#"+str(i)+":",result[i-1])
tidy()
