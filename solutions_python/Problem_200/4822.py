def largestTidy(number):
    number = [int(d) for d in str(number)]
    if (len(number) == 1):
        return number[0]
    else:
        var = 9
        for i in range(len(number)-1, 0, -1):
            last = number[i]
            second_last = number[i-1]
            if(last < second_last):
                number[i] = 9
                number[i-1] = int(number[i-1]) - 1
                for j in range(i, len(number)-1):
                    if(number[j] > number[j+1]):
                        number[j+1] = number[j]
        return (int(''.join(map(str, number))))

tc = int(input())
for etc in range(tc):
    number = int(input())
    print ("Case #" + str(etc + 1) + ": " + str(largestTidy(number)))
