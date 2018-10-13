



input = open('input.txt', 'r')
output = open('output.txt', 'w')

num_of_test = int(input.readline().rstrip())

for i in range(1, num_of_test+1):
    nums = []
    for j in range(0,2):
        instance = []
        row = int(input.readline().rstrip())
        for k in range(1,5):
            line = input.readline().rstrip().split(' ')
            if k == row:
                for n in line:
                    instance.append(int(n))
                nums.append(instance)
    counter = 0
    res = 0
    for e in nums[0]:
        if e in nums[1]:
            print(e)
            counter += 1
            res = e
    if counter == 0:
        output.write('Case #%d: Volunteer cheated!\n' % i)
    elif counter == 1:
        output.write('Case #%d: %d\n' %(i, res))
    else:
        output.write('Case #%d: Bad magician!\n' % i)

