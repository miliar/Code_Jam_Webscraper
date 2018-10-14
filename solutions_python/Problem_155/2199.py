cases = int(input())

for i in range(0 , cases):
    test = input().split(" ")
    maxs = int(test[0])
    digits = test[1]
    count = 0
    standing = 0
    for j in range(0, len(digits)):
        if(int(digits[j]) != 0):
            if(standing < j):
                count += j - standing
                standing += (j - standing)
            standing += int(digits[j])

    print("Case #%d: %d" %(i + 1, count))
