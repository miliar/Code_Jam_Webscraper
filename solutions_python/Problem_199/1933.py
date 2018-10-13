def flipPancakes(n, m):
    count = 0
    if m > len(n):
        return -1
    
    my_list = [n]
    
    while True:
        x = n.find('-', 0, len(n) - m + 1)
        
        if x != -1:
            count += 1
            for i in range(x, x+m):
                if n[i] == '+':
                    n = n[:i] + '-' + n[i+1:]
                else:
                    n = n[:i] + '+' + n[i+1:]

        

        if(n in my_list):
            break
        my_list.append(n)
        
        y = n[::-1].find('-', 0, len(n) - m + 1)
        if y != -1:
            count += 1
            for i in range(y, y+m):
                j = len(n)-i-1
                if n[j] == '+':
                    n = n[:j] + '-' + n[j+1:]
                else:
                    n = n[:j] + '+' + n[j+1:]
        
        if(n in my_list):
            break
        my_list.append(n)                    
        
        if n == len(n) * '+':
            break
        
        
    #print(my_list)
    if n == len(n) * '+':
        return count
    else:
        return -1


t = int(input())  # read a line with a single integer
for i in range(1, t + 1):
    n, m = [str(s) for s in input().split(" ")]  # read a list of integers, 2 in this case
    m = int(m)
    answer = flipPancakes(n, m)
    if answer == -1:
        answer = "IMPOSSIBLE"

    print("Case #{}: {}".format(i, answer))
