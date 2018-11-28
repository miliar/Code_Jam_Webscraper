def model(l,n):
    l = list(str(l))
    k = 0
    j = k+n


    c = 0
    while len(set(l)) != 1 or '-' in l:

        if '+' not in l[k:j]:
            if len(l[k:j]) == n:
                for i in xrange(k,k+len(l[k:j])):

                    if l[i] == '+':
                        l[i] = '-'
                    elif l[i] == '-' :
                        l[i] = '+'
                c += 1
                k = j
                j = k+n

            else :
                return "IMPOSSIBLE"

        elif l[k] == '+':

            k += 1
            j += 1

        else :
            if len(l[k:j]) == n:

                for i in xrange(k, k + len(l[k:j])):
                    if l[i] == '+':
                        l[i] = '-'
                    elif l[i] == '-':
                        l[i] = '+'
                c += 1


            else :
                return "IMPOSSIBLE"
    return c




with open("/home/gifty/PycharmProjects/GKJ/A-large.txt") as f:
    n = int(f.readline())
    lines = f.readlines()
    i = 1
    for line in lines:
        a,b = map(str, line.strip().split())

        x = model(a,int(b))
        print "Case  #%s:"%(i),x
        i += 1
