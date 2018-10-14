t = int(raw_input())  # read a line with a single integer
for index in xrange(1, t + 1):
    solution = 0
    N = int(raw_input())
    list = []

    for digit in str(N):
        list.append(int(digit))

    j = len(list)-1
    while j > 0:
        subtracted = False
        if list[j] < list[j-1] or list[j] < j:
            N = N-((list[j]+1)*pow(10,len(list)-1-j))
            subtracted = True

        if (subtracted):
            list = []
            for digit in str(N):
                list.append(int(digit))

            k = j+1
            while k < len(list):
                list[k] = 9
                k += 1

            magic = lambda nums: int(''.join(str(i) for i in nums))
            N = magic(list)

        j = j-1

        list = []
        for digit in str(N):
            list.append(int(digit))

    print 'Case #{}: {}'.format(index, N)