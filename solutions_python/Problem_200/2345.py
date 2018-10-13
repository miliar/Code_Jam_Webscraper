cases = int(input())
out_file = open('output2.txt', 'w')

for test in range(cases):
    number = input()

    if not len(number) == 1:
        for i in range(len(number)):
            if i+1 < len(number) and number[i] > number[i+1]:
                if number[i] == '1':
                    number = (len(number)-1) * '9'
                else:
                    number = number[:i] + str(int(number[i])-1) + (len(number[i+1:]) * '9')

                i = 0
    out_file.write('Case #' + str(test+1) + ': ' + number + '\n')
    

out_file.close()
