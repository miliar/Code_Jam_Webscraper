def get_nvalue(X, Y):
    if( X > 0):
        n1= 'W'
        n2= 'E'
    else:
        n1='E'
        n2='W'

    if( Y > 0):
        m1= 'S'
        m2= 'N'
    else:
        m1= 'N'
        m2= 'S'

    x = 0
    y = 0
    result = ''

    X= abs(X)
    Y= abs(Y)

    while x != X:
        result = result + n1+n2
        x = x+1

    while y != Y:
        result = result + m1+m2
        y = y+1

    return result


#f = open('A-large.in', 'r')
f = open('B-small-attempt0.in', 'r')

#f = open('practice.txt', 'r')

output = open('output.txt','w')

T = int(f.readline())

#print(T)

for i in range(1,T+1):
    line1 = f.readline().rstrip().split()
    #motes = [int(x) for x in f.readline().rstrip().split()]

    X = int(line1[0])
    Y = int(line1[1])


    result = get_nvalue(X,Y)

    text = 'Case #'+str(i)+': '+ result

    print(text,file=output)
    print(text)

    #print()

f.close()
output.close()

#print(lines)
