
filename = 'C-small-2-attempt1.in'
outputname = 'output.txt'
file = open(filename, 'r')
first = 0
t = int(file.readline())
output = []
for i in range(t):
    line = file.readline()
    nums = line.split()
    n = int(nums[0])
    k = int(nums[1])
    y = 0
    z = 0
    while k > 1:
        n -= 1
        if n%2!=0:
            if k%2!=0:
                n = int(n/2)
                k -= 1
            else:
                n = int(n/2)+1
        else:
            n = int(n/2)
        k = int(k/2)
    z = int((n-1)/2)
    y = z
    if n%2==0:
        y += 1
    output.append('Case #' + str(i+1) + ': ' + str(y) + ' ' + str(z) + '\n')

file.close()
newfile = open(outputname, 'w')
newfile.writelines(output)
newfile.close()
