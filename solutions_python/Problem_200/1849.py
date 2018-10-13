def find_point(num_str):
    for di in range(len(num_str) - 1):
        if num_str[di] > num_str[di+1]:
           return di
    return 'ok' 
       
t = int(raw_input().strip())
for ti in range(1, t+1):
    n = raw_input().strip()
    if len(n) == 1:
        answer = n
    else:
        point = find_point(n)       
        if point == 'ok':
            answer = n
        elif point == 0:
            answer = str(int(str(int(n[0]) - 1) + ('9' * (len(n) - 1))))
        else:    
            while True:
                answer = str(int(n[:point] + str(int(n[point])-1) + ('9' * (len(n[point+1:])))))
                point = find_point(answer)
                if point == 'ok':
                    break
                       
    print 'Case #' + str(ti) + ': ' + answer