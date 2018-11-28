def tidy (number):
    a = ''
    b = ''
    if(len(number) == 1):
        return number
    for i in range(1,len(number)):
        if(int(number[i])< int(number[i-1])):
            for j in range((len(number)-i)):
                b += '9'
            #print b
            a = number[:i]
            a = str(int(a)-1)
            c = tidy(a)
            if c == '0':
                return b
            return c+b
    return number
size = int(raw_input())
for x in range(size):
    temp = raw_input()
    print "Case #"+str(x+1)+": "+tidy(temp)
