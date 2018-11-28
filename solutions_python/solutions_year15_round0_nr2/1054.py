'''
Google Code Jam 2015
Qualification Round
Problem B. Infinite House of Pancakes
'''
if __name__ == '__main__':
    t = int(input())
    for counter in range(1, t+1):
        d = int(input())
        save = [1*int(x) for x in input().split()]
        save.sort(reverse=True)
        #print(save)
        ans = save[0]
        for i in range(save[0], 0, -1):
            temp = i
            for j in range(len(save)):
                temp += (save[j]-1) // i
            #print(ans, temp)
            ans = min(ans, temp)
        print('Case #{}: {}'.format(counter, ans))
