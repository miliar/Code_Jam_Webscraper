in_data = open('B-large.in').readlines()
T=in_data[0]
in_data=in_data[1:]
outfile = open('result', 'w')
case_no = 0

for line in in_data:
    case_no += 1
    res = 0
    line = line.strip()
    line = line.split()
    line = [int(x) for x in line]
    N = line[0]
    S = line[1]
    p = line[2]
    line = line[3:]
    for i in line:
        if i%3 == 0:
            if i/3 >= p:
                res += 1
                continue
            else:
                if S >0 and i!=0 and i/3+1 >=p:
                    S-=1
                    res +=1
                    continue
        if i%3 == 1:
            if i/3 + 1 >=p:
                res +=1
                continue
        if i%3 ==2:
            if i/3+1 >=p:
                res +=1
                continue
            else:
                if S>0 and i/3+2>=p:
                    S-=1
                    res +=1
                    continue
    out = 'Case #' + str(case_no) + ': ' + str(res) + '\n'
    outfile.write(out)

outfile.close()


# END