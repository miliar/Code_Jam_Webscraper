import math
def is_palindrome(number):
    string = str(number)

    length = len(string)
    if(length == 1):
        return True
    elif(length%2 == 0):
        length = length/2
    else:
        length = (length-1)/2
    length = int(length)
    f_string = string[0:length]
    r_string = string[:-length-1:-1]
    
    if(f_string == r_string):
        return True
    else:
        return False


file = open('C-small-attempt0.in', 'r')

data = file.read()

file.close()

data = data.strip('\n')
data = data.split('\n')

numCases = data[0]

data.pop(0)

result = ''
index = 1

for case in data:
    answer = 0
    case = case.split(' ')
    for i in range(int(case[0]), int(case[1])+1):
        if(is_palindrome(i)):
            root = math.sqrt(i)
            if(root%1 == 0 and root >= 1 and is_palindrome(int(root))):
                answer += 1
                
                
            

    result += 'Case #'+str(index)+': '+str(answer)+'\n'
    index += 1

result = result.strip('\n')
print(result)

f = open('C-small-attempt0.out','w')
f.write(result)
f.close()

    
