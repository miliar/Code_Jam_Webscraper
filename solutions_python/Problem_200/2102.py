for T in range(1, int(raw_input()) + 1):
    N = raw_input()
    length = len(N)
    word = []
    flag = False
    flag_spot = 0
    flag_one_zero = False
    one_zero_spot = 0
    
    for i in range(length):
        if i > 0 and not flag:    
            if int(N[i-1]) > int(N[i]):
                if int(N[i-1]) == 1:
                    flag_one_zero = True
                    one_zero_spot = i
                    break
                else:
                    flag = True
                    flag_spot = i
                    break
        word.append(N[i])
    
    if flag:
        done = False
        j = flag_spot 
        word = list(N)
        while not done:
            if word[j - 1] != word[j - 2]:
                done = True
                break
            if j == 1:
                break
            j -= 1
        word[j -1] = str(int(word[j - 1]) - 1)
        for i in range(j, length, 1):
            word[i] = '9'
        word = int(''.join(word))
    elif flag_one_zero:
        i = one_zero_spot
        word = list(N)
        while i > 0:
            if int(word[i-1]) > 1:
                break    
            i -= 1
        word[i] = str(int(word[i]) - 1)
        for j in range(i + 1, length, 1):
            word[j] = '9'
        word = int(''.join(word))
    else:
        word = int(''.join(word)) 
        
    print('Case #%d: %d'%(T, word))
