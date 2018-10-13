import sys


case = open('input.txt', 'r').read()
allLines = case.split('\n')
k = 0

myfile = open('1.txt', 'wt')

for lines in allLines:


    
        numbers = lines.split()
        
        googlers = int(numbers[0])
        suprises = int(numbers[1])
        p = int(numbers[2])

        answers = list()
        i = 0
        while i < googlers:
            ans = []
            max = int(numbers[i + 3]) / 3
            remainder = int(numbers[i + 3]) % 3
            if int(numbers[i + 3]) < p:
                answers.append([0,0])
            elif max >= p:
                answers.append([1,1])
            elif max + 2 < p:
                answers.append([0,0])
            elif max + 1 == p:
                if remainder != 0:
                    ans.append(1)
                else:
                    ans.append(0)
                ans.append(1)
                answers.append(ans)
            elif max + 2 == p:
                ans.append(0)
                if remainder == 2:
                    ans.append(1)
                else:
                    ans.append(0)
                answers.append(ans)
                
            i = i +1
        l = 0
        m = 0
        count = 0
        while count < googlers:
            if answers[count][0] == 1:
                l = l +1
            elif answers[count][1] == 1:
                m = m +1
            count = count + 1
        if m > suprises:
            m = suprises
        
                
        myfile.write("Case #")
        myfile.write( str(k+1))
        myfile.write( ": ")
        myfile.write(str(m + l))
        myfile.write('\n')
        k = k+1

myfile.close()

