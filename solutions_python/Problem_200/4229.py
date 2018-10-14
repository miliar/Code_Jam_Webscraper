t = int(input())
numbers = []
for i in range(1, t + 1):
  numbers.append(int(input()))

for i, n in enumerate(numbers):
    number_int = n
    if n > 0 and n < 10:
        print("Case #{}: {}".format(i+1, number_int))
        continue
    while number_int > 0:
        number = str(n)
        if number[-1] != '0':
            pos = number.find('0')
            if pos != -1:
                number = (number[:pos] + '0' * len(number[pos:]))
        if number[0] == 1:
            number = '9' * (len(number) -1)
            print("Case #{}: {}".format(i+1, number_int))
            break
        last = int(number[-1])

        for j in range(len(number)-1, 0, -1):
            new_last = int(number[j-1])
            if new_last > last:
                number = list(number)
                number[j-1] =  str(new_last-1)
                if j+1 < len(number) and int(number[j]) < 9 and int(number[j+1]) < 9:
                    pos = j
                    if pos != -1:
                        for x in range(pos, len(number)):
                            number[x] = '9'
                number[j] = '9'
                number = ''.join(number)
                number_int = int(number)
                last = new_last-1
                if j == 1 or j == 0:
                    number_int = str(number_int).replace('0', '9')
                    print("Case #{}: {}".format(i+1, number_int))
                    break
            else:
                if j == 1 or j==0:
                    print("Case #{}: {}".format(i+1, number_int))
                    break
                else:
                    last = new_last
        break
