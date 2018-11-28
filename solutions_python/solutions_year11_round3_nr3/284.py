'''
2
3 2 100
3 5 7
4 8 16
1 20 5 2
'''

for _ in range(1, int(raw_input())+1):
    j = [int(__) for __ in raw_input().split()]    
    o = [int(__) for __ in raw_input().split()]
    
    flag = 1
    for i in range(j[1], j[2]+1):
        c = 0
        for y in o:
            if i < y:
                if y%i == 0:
                    c+=1
            else:
                if i%y == 0:
                    c+=1
        if c == j[0]:
            flag = 0
            print 'Case #'+str(_)+':', i
            break
    
    if flag:
        print 'Case #'+str(_)+': NO'