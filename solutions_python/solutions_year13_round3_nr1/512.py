def findNumber(string, n):
    count = 0
    vowels = ['a','e','i','o','u']

    num = n

    while (num <= len(string)):
        for i in range(len(string)-num+1):
            check = string[i:i+num]
            t = 0
            for c in check:
                if t >= n:
                    count += 1
                    break
                if c in vowels:
                    vowel = True
                    t = 0
                else:
                    t += 1
            else:
                if t >= n:
                    count += 1
        num += 1

    return count









FILENAME = "A-small-attempt0"
f = open(FILENAME + '.in', 'r')
T = int(f.readline())
output = []
for i in range(T):
    temp = f.readline().split(' ')
    string = temp[0]
    n = int(temp[1])
   
    output.append("Case #"+str(i+1)+": " + str(findNumber(string, n)))
    print output[i]
    


f.close()
output = '\n'.join(e for e in output)
f = open(FILENAME + '.out', 'w')
f.write(output)
f.close()
