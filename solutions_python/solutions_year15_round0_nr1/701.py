import math
fo = open("A-large.in")
fo2 = open("output2.txt", mode='w')
tests = eval(fo.readline())
output = []
for x in range(1,tests+1):
    str1 = fo.readline().strip("\n")
    str1=str1.split(" ")
    maxShi = eval(str1[0])
    input = str1[1]
    sum = 0
    maxSum = 0

    for shi in range(0,maxShi+1):
        maxSum=max(maxSum, shi-sum)
        sum=sum+eval(input[shi]);
    output.append("Case #"+str(x)+": "+str(maxSum)+"\n")

fo2.writelines(output)
