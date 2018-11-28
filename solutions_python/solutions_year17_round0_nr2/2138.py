t = int(input().strip()) # num testcases
for c in range(t):
    number = int(input().strip())
    if number < 10: # we just return the number
        print("Case #" + str(c + 1) + ": " + str(number))
    else:
        string = list(str(number))
        index = 1
        while index < len(string):
            if int(string[index]) < int(string[index-1]): # found decreasing order
                for i in range(index,len(string)):
                    string[i] = '9'
                index -= 1
                string[index] = str(int(string[index]) - 1) # decrement first left value
                while index > 0:
                    if int(string[index]) < int(string[index-1]):
                        string[index] = '9'
                        string[index-1] = str(int(string[index-1]) - 1)
                    index -= 1
                break
            index += 1
        print("Case #" + str(c + 1) + ": " + str(int(''.join(string))))
