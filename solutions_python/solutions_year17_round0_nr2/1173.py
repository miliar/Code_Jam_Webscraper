cases = int(input())
for case in range(1,cases+1):
    n = input()
    number = n
    if len(n) > 1:
        while True:
            found = True
            for i in range(len(number)-1):
                if int(number[i]) > int(number[i+1]):
                    tidy_number = str(int(number[:i+2]) - int(number[i+1]) - 1)
                    tidy_number = tidy_number + '9' * (len(number) - i - 2)
                    found = False
                    number = tidy_number
                    break
            if found:
                break

    print('Case #{}: {}'.format(case, number))
                    
                        
            