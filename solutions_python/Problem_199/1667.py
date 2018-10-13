def calculate(s, k):
    count = 0
    for i in range(0, len(s) - k + 1):
        if (s[i] == False):
            count = count + 1
            for j in range(0,k):
                if (s[i+j] == False):
                    s[i+j] = True
                else:
                    s[i+j] = False         
    return count   

f = open('data.txt', 'r')
array = f.readlines()

for i in range(0,len(array)):
     array[i] = array[i].strip()

testNum = int(array[0])
array.pop(0)

for i in range(0, testNum):
    innerArray = array[i].split(" ")
    s = list(innerArray[0])
    k = int(innerArray[1])

    for j in range(0, len(s)):
        if (s[j] == '+'):
            s[j] = True
        else:
            s[j] = False

    result = calculate(s, k)
    for j in range(0, len(s)):
        if (s[j] == False):
            result = "IMPOSSIBLE"
    
    print("Case #" + str(i+1) + ": " + str(result))
    


