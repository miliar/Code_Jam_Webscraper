g = open('great.txt','w+')
 
with open('A-large.in', 'r+') as f:
    num = int(f.readline())
   
    for i in range(num):
        shy, crowd = f.readline().split(' ')
        crowd = list(crowd)[:-1]
        board = 0
        num_friends = 0
       
        for j, k in enumerate(crowd):
            if board >= j:
                board += int(k)
            else:
                num_friends += (j - board)
                board += (int(k) + (j - board))
 
        g.write('Case #' + str(i+1) + ': ' + str(num_friends) + '\n')
       
g.close()
