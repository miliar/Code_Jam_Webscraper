lines = [line.rstrip('\n') for line in open('A-large.in')]
str_temp = ''

T = int(lines[0])

def check(S,K):
    arr = [x for x in S]
    
    max_possible_tries = len(S) - K + 1
    current_tries = 0
    
    for each_try in range(1,max_possible_tries+2):
        try:
            occur = arr.index('-')
        except ValueError:
            return current_tries
        
        #Check if window is above last guy
        if (occur+K) > len(arr):
            return 'IMPOSSIBLE'
        
        for index_window in range(K):
            try:
                current_index = index_window+occur
                if arr[current_index] == '+':
                    arr[current_index] = '-'
                elif arr[current_index] == '-':
                    arr[current_index] = '+'
            except IndexError:
                #THIS SHOULD NEVER HAPPEN
                return 'IMPOSSIBLE'
            
        current_tries+=1
    
    return 'IMPOSSIBLE'


for t in range(1,T+1):
    main_str = lines[t]
    S = main_str.split(' ')[0]
    K = int(main_str.split(' ')[1])
    if t == T:
        str_temp = str_temp+'Case #'+str(t)+': '+str(check(S,K))
    else:
        str_temp = str_temp+'Case #'+str(t)+': '+str(check(S,K))+'\n'
        
print(str_temp)
f = open('out.txt', 'w')
f.write(str_temp)
f.close()