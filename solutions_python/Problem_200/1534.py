TC = int(input())
for t in range(TC):
    num = int(input())
    b = 10
    c = 10
    while b <= num:
        while (num%b)//(b//10) < (num%(b*10))//b:
            num -= ((num%c)//(c//10))*(c//10)+c//10
            c*= 10
            #print(num)
        b*=10
    print("Case #",t+1,": ",num, sep="")
