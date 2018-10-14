from math import sqrt, ceil, floor

def check_palindrome(num):
    num = str(num)
    return num == num[::-1]

def palindrome(sm,bg):
    count = 0
    for i in range(sm,bg+1):
        if check_palindrome(i) and check_palindrome(i*i):
            count +=1
    return count

f = open('C-small-attempt0.in', 'r')

output = open('output.txt','w')

T = int(f.readline())

for i in range(1,T+1):
    line = (f.readline().strip('\n')).split(' ')

    sm = ceil(sqrt(int(line[0])))
    bg = floor(sqrt(int(line[1])))

    result = palindrome(sm,bg)

    text = 'Case #'+str(i)+': '+ str(result)

    print(text,file=output)
    #print(text)

f.close()
output.close()
