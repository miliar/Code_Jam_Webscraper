def nod(a, b):
    if a < b:
        return nod(b, a)
    if a == b or b == 0:
        return a
    return nod(b, a%b)

input = open('input.txt', 'r')
output = open('output.txt', 'w')
read = input.readlines();
t = int(read[0])
for x in range(t):
    inp = read[x+1].rstrip('\n')
    #print(inp)
    inp = inp.split()
    #print(inp)
    n = int(inp[0])
    nums = []
    for i in range(n):
        nums.append(int(inp[i+1]))
    nums.sort()
    num = nums[1] - nums[0]
    #print (num)
    for i in range(n - 2):
        num = nod(num, nums[2+i] - nums[0])
        #print (num)
    if nums[0]%num == 0:
        num = 0
    else:
        num = num - nums[0]%num
    output.write("Case #" + str(x+1) + ": " + str(num) +"\n")        


input.close()
output.close()



