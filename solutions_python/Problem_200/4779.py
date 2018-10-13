# n = 10, 11, 110, 4597625, 4589625, 4587625
#n = 1110
test_cases = raw_input()
for x in range(int(test_cases)):
    n = int(raw_input())
    length = len(str(n))

    tidy = 0
    curr_max = 0
    zero_found = False
    one_found = False

    for i in range(length):
        next_digit = int(str(n)[i])
        if next_digit == 0:
            zero_found = True
        elif next_digit == 1:
            one_found = True
        elif next_digit != 0 or next_digit != 1:
            zero_found = False
            one_found = False
            break
        
    if one_found and zero_found:
        residual = len(str(n))-len(str(tidy))
        tidy += 10**(residual)-1

    else:
        for i in range(length):
            next_digit = int(str(n)[i])
            if curr_max <= next_digit:
                curr_max = next_digit
                tidy *= 10
                tidy += next_digit
            else:
                tidy -= 1
                counter = 0
                while (int(str(tidy)[len(str(tidy))-counter-2]) > int(str(tidy)[len(str(tidy))-counter-1]) ):
                    tidy -= 10**(counter+1)
                    counter += 1

                if counter > 0:
                    tidy %= 10**counter
                residual = len(str(n))-len(str(tidy))

                tidy *= 10**(residual)
                tidy += 10**(residual)-1
                break
    print 'Case #' + str(x+1) + ': ' + str(tidy)
    #(counter+2) < len(str(tidy)) and 
