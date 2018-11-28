

t = int(input())
for i in range(1, t+1):
    
    
    row,col = [int(x) for x in input().split()]
    
    print("Case #{}:".format(i))
    
    empty_line = col * '?'
    last_line = col * '?'
    empty_count = 0
    
    for j in range(row):
        line = input()
        
        ch = '?'
        counter = 0
        
        for c in line:
            if c != '?':
                if ch == '?':
#                    line[:counter] = counter * c
                     line = counter * c + line[counter:]
                ch = c
            else:
#                line[counter] = ch
                 line = line[:counter] + ch + line[counter+1:]
                    
            counter = counter + 1
                
                    
        if line != col * '?':
            if last_line == col * '?':
                for _ in range(empty_count + 1):
                    print(line)
            else:
                print(line)
            last_line = line
        else:
            empty_count = empty_count + 1
            if last_line != empty_line:
                print(last_line)