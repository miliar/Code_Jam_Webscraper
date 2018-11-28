__author__ = 'fcueto'

file_in = 'A-small-attempt1.in'
#file_in = 'magician1.txt'
fid_in = open(file_in, 'r')
fid_out = open('magician_out.txt','w')

N_cases = int(fid_in.readline().strip())

for case in range(0, N_cases) :

    row1 = int(fid_in.readline().strip())

    for j in range(1,5) :
        tmp = fid_in.readline()
        if j==row1 :
            a = set(tmp.split())

    row2 = int(fid_in.readline().strip())

    for j in range(1,5) :
        tmp = fid_in.readline()
        if j==row2 :
            b = set(tmp.split())


    c = a.intersection(b)
    numc = len(c)

    if numc==0:
        answer = 'Volunteer cheated!'
    elif numc == 1:
        answer = c.pop()
    else :
        answer = 'Bad magician!'

    line = "Case #%i: %s\n" % (case+1, answer)
    print(line)
    fid_out.write(line)

fid_in.close()
fid_out.close()