test_size = int(input())

for test_case in range(test_size):
    
    number = list(str(input()))

    for i in range(1, len(number)):
        if number[i - 1] > number[i]:
            
            for j in range(i, len(number)):
                number[j] = '9'
  
            for j in reversed(range(i)):
                number[j] = str(int(number[j]) - 1)
               
                if j == 0:
                    while number[0] == '0' and len(number) > 1:
                            number = number[1:len(number)]
                else:
                    if number[j] >= number[j - 1]:
                        break
                    else:
                       number[j] = '9'
            break
     

    print('Case #' + str(test_case + 1) + ': ' + "".join(number))
    
    