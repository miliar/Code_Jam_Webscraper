def req_stand(shy):
    stand = 0
    req = 0
    for s, n in enumerate(shy):
        if(stand >= s):
            stand = stand + n
        else:
            if(n != 0):
                req = req + (s - stand)
                stand = stand + req + n
    return req

infile = open("/home/himanshu/projects/codejam/stand.txt", 'r')
outfile = open("/home/himanshu/projects/codejam/stand-out.txt", 'w')
t = infile.readline()
for n in range(int(t)):
    i = infile.readline()
    i = i.replace("\n", '')
    i = i.split(' ')
    i = [int(j) for j in i[1]]
    outfile.write("Case #{}: {}\n".format(n+1, req_stand(i)))
