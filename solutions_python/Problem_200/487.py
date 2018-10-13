t = int(raw_input()) 
for i in xrange(1, t + 1):
    numbers = list(raw_input())
    for ii in range(len(numbers) - 1, 0, -1):
        if numbers[ii] < numbers[ii - 1]:
            for j in range(ii, len(numbers)):
                numbers[j] = '9'
            numbers[ii - 1] = str(int(numbers[ii - 1]) - 1)
    result = ""
    if numbers[0] != '0':
        result += numbers[0]
    for ii in range(1, len(numbers)):
        result += numbers[ii]
    print "Case #{}: {}".format(i, result)