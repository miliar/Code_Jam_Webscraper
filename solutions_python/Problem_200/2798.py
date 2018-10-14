t = int(input())
t_i = 1
while t_i<=t:
    n = input()
    digits = list(n)
    #print(digits)
    prev = '0'
    index = 0
    dict = {0:'0'}
    
    for digit in digits:
        if digit>=prev:
            prev = digit
        else:
            #print('defaulter'+digit)
            break
        index+=1
        dict[index] = prev 
        
    if index == len(digits):
        print('Case #'+str(t_i)+': '+n)
        #print('continue k wala')
        t_i+=1
        continue
    else:
        i = 0
        #print('index '+str(index))
        #print(dict)
        #index-=1
        new_n = ''
        while i<=index:
                '''if i==index:
                    new_n = '9'*(len(digits)-1)
                    print('inside')
                    break'''
                if int(dict[index-i])-1>=int(dict[index-i-1]) :
                    tidy_n = digits[:(index-i-1)]
                    #print('i = '+str(i))
                    tidy_n.append(str(int(dict[index])-1))
                    nines = ['9']*(len(digits)-len(tidy_n))
                    tidy_n.extend(nines)
                    if tidy_n[0] == '0':
                        tidy_n = tidy_n[1:]
                    
                    new_n = ''.join(tidy_n)
                    break
                i+=1

        print('Case #'+str(t_i)+': '+new_n)
        
                    
    t_i+=1
