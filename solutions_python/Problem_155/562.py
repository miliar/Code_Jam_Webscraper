x = open('C:\google\Large_Standing.out.txt','w+')

with open('C:\google\Large_Standing.txt', 'r+') as t:
    number_cases = int (t.readline())
    
    for i in range(number_cases):
        max_shy, crowd = t.readline().split(' ')
        crowd = list(crowd)[:-1]
        current_standing = 0
        number_frnds = 0
        
        for j, k in enumerate(crowd):
            if current_standing >= j:
                current_standing += int(k)
            else:
                number_frnds += (j - current_standing)
                current_standing += (int(k) + (j - current_standing))

        x.write('Case #' + str(i+1) + ': ' + str(number_frnds) + '\n')
        
x.close()
