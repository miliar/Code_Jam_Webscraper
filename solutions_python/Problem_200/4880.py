#number=int(input())
file = open('in.txt', 'r')
file2 = open('result.txt','w') 
numberLines=int(file.readline())
for go in range(numberLines):
    number = int(file.readline())
    for n in reversed(range(number+1)):
        digits=list((str(n)))
        flag=0
        #print(digits)
        for i in reversed(range(len(digits))):
            if i != 0:
                if digits[i] < digits[i-1]:
                    flag = 1
                    break
        if flag == 0:
            file2.write("Case #{}: {}\n".format(go+1, n))
            print(n)
            break

 

file.close()
file2.close() 
