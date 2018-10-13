filename = "B-large.in"

nums=[]

def get_input(filename):
    with open(filename) as f:
        lines = f.readlines()
        for line in lines[1:] :
            line = line.split()
            nums.append(line[0])

def solve(num):
    num = [int(i) for i in list(str(num))]
    i = 0
    while i < len(num) - 1:
        if num[i] > num[i+1]:
            num[i] = num[i]-1
            for j in range(i+1,len(num)):
                num[j] = 9
            if i > 0 and num[i] < num[i-1]:
                i = i -1
        else:
            i+=1
    if num[0] == 0:
        return ''.join([str(i) for i in num[1:]])
    return ''.join([str(i) for i in num])

def solve2(num):
    num = [int(i) for i in list(str(num))]
    num = ''.join([str(i) for i in num])
    num = int(num)




get_input(filename)


for i in range(0,len(nums)):
    print("Case #", i+1 , ": ", solve(nums[i]), sep="")
