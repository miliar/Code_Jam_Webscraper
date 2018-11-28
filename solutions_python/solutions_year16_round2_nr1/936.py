def decode(s):
    dic = {'E':0, 'R':0, 'O':0, 'N':0, 'T':0, 'H':0,'F':0,'U':0,'V':0,'S':0, 'I':0,}
    zero = 0
    one = 0
    two = 0
    three = 0
    four = 0
    five = 0
    six = 0
    seven = 0
    eight = 0
    nine = 0

    for i in s:
        if (i == '\n'):
            break
        if (i == 'Z'):
            zero+=1
            dic['E']-=1
            dic['R']-=1
            dic['O']-=1
        elif (i == 'W'):
            two+=1
            dic['T']-=1
            dic['O']-=1
        elif (i == 'U'):
            four+=1
            dic['F']-=1
            dic['O']-=1
            dic['R']-=1
        elif (i=='X'):
            six +=1
            dic['S']-=1
            dic['I']-=1
        elif (i == 'G'):
            eight+=1
            dic['E']-=1
            dic['I']-=1
            dic['H']-=1
            dic['T']-=1
        else:
            dic[i]+=1


    one = dic['O']
    dic['N']-=one


    three = dic['T']

    five =dic['F']


    seven = dic['S']
    dic['N']-=seven

    nine = dic['N'] / 2

    result = ''

    for i in range(zero):
        result += '0'

    for i in range(one):
        result += '1'

    for i in range(two):
        result += '2'

    for i in range(three):
        result += '3'

    for i in range(four):
        result += '4'

    for i in range(five):
        result += '5'

    for i in range(six):
        result += '6'

    for i in range(seven):
        result += '7'

    for i in range(eight):
        result += '8'

    for i in range(nine):
        result += '9'

    return result

if __name__ == '__main__':

    f = open('test.in', 'r')
    g = open('res.txt', 'w')

    t = int(f.readline())

    for i in range(t):
        prt = "Case #"+str(i+1)+": "
        s = f.readline()
        result = decode(s)
        prt+=result
        g.write(prt)
        print (prt)
    g.close()
