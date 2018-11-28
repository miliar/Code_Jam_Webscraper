N = int(input())
for i in range(N):
    size = list(map(int,input().split()))
    line = []
    for j in range(size[0]):
        line.append(input())
    for n in range(2):
        for li in range(len(line)):
            letter = ''
            for s in range(len(line[li])):
                l = line[li]
                if l[s]=='?':
                    continue
                else:
                    letter = l[s]
                    c = s-1
                    while(c>=0):
                        l = line[li]
                        if l[c]=='?':
                            line[li] = l[0:c] + letter + l[c+1:len(l)]
                            c -= 1
                        else:
                            break
                    c = s+1
                    while(c<len(line[li])):
                        l = line[li]
                        if l[c]=='?':
                            line[li] = l[0:c] + letter + l[c+1:len(l)]
                            c += 1
                        else:
                            break
        line_t = []
        for k2 in range(len(line[li])):
            st = ''
            for k1 in range(len(line)):
                st += line[k1][k2] 
            line_t.append(st)

        line = line_t

    print('Case #'+str(i+1)+':')
    for l in line:
        print(l)


