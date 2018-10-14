def stalls(x, y):
    #find factor

    x = int(x)
    y = int(y)

    factor_found = False
    factor = -1
    remainder = 0
    while factor_found == False:
        factor = factor + 1
        if y < pow(2,factor):
            factor_found = True
            remainder = y % pow(2,factor-1)


    factor = factor - 1

    x = x - remainder

    pow_factor = pow(2, factor)*2

    max_num = x / pow_factor

    min_num = (x - pow(2, factor)) / pow_factor


    return str(max_num) + " " + str(min_num)



f = open('bathlarge.in', 'r')
g = open('bathlarge.out', 'w')
content = f.readlines()
numOfCases = int(content[0])
iter = 0
s = ""
for n in content:
    if iter == 0:
        pass
    else:
        list_n = n.split()
        print "Case #"+str(iter)+": "+ str(stalls(list_n[0], list_n[1]))
        s = s + "Case #"+str(iter)+": "+ str(stalls(list_n[0], list_n[1])) + "\n"
    iter = iter + 1
g.write(s)

#print pow_factor



