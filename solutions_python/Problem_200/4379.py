result_list = []
c = 0
test = int(input())
n = 0

for loop in range(test):

    n= int(input())
    z = 1
    stringn = list( map( int, str( n ) ) )
    l = len( stringn )
    result = 0
    r=0
    for i in range( 10 ):
        if n == i:
            result = n
    c=0
    for i in range(l-1):
        if stringn[i] > stringn[i+1]:
            c = 1
            break
    
    if c == 1:
        for i in range( l - 1 ):
            if stringn[i]<stringn[i+1]:
                continue
            else:
                if stringn[i] == stringn[i + 1]:
                    r = n - (n - (stringn[0] * pow( 10, l - 1 )))
                    result = r - 1
                    break
                elif (stringn[i] == 1) and (stringn[i+1] == 0):
                    r = n - (n - (stringn[0] * pow(10, l - 1)))
                    result = r - 1
                    break
                else:
                    stringn[i] -= 1
                    for j in range(i+1, l):
                            stringn[j] = 9
                    result = int("".join(map(str, stringn)))
                    break
    else:
        result = n
    result_list.append(result)
    result = 0

for i in range(len(result_list)):
    print("Case #"+str(i+1)+':', result_list[i])

