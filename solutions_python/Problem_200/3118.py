n = int(raw_input())
cont = 1

while(cont<=n):

    num = raw_input()
    num = list(num)
    tam = len(num)

    for i in range(tam-1):
        cur = tam - i - 1
        if(int(num[cur]) < int(num[cur-1])):
            for j in range(cur, tam):
                num[j] = '9'

            if(num[cur-1] == '0'):
                num[cur-1] = '0'
            else:
                num[cur-1] = str(int(num[cur-1])-1)

    res = ''.join(num)
    res = int(res)

    print "Case #{}: {}".format(cont, res)

    cont+=1
