# file = open('B-small-attempt0.in','r')
# out = open('output.txt','a')
N = int(input())
# N = int(file.readline())
# nums = file.readlines()
for e in range(N):
    num=int(input())
    # num=int(nums[e])
    print(num)
    last_num = int(str(num)[len(str(num))-1])
    str_num = str(num)
    numbers = [int(x) for x in str_num]
    l = len(numbers)
    str_sum = ''
    for i in range(len(str(num))-1):
        a = numbers[l-i-1]
        b = numbers[l-i-2]
        if a >= b :
            continue
        elif a < b :
            numbers[l-i-2]-=1
            for k in range(i+1):
                numbers[l-i-1+k]=9
    for i in numbers:
        str_sum+=str(i)
	print("Case #{}: {}".format(str(e+1), str(int(str_sum))))
#     out.write('Case #'+str(e+1)+': '+str(int(str_sum))+'\n')
# out.close()
# file.close()
