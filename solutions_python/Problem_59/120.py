def calc(disk,mk):
    names = {}
    
    for line in disk:
        dirs = line.split('/')
        l = ''
        for i in range(1,len(dirs)):
            l = l + '/' + dirs[i]
            names[l] = True
    del disk
    
    c = 0
    
    for line in mk:
        if line in names:
            continue
        else:
            names[line] = True
            c = c + 1
        
        dirs = line.split('/')
        x = len(line)
        for i in range(len(dirs)-1,0,-1):
            x = x - len(dirs[i]) - 1
            if x <= 0:
                break
            l = line[:x]

            if l in names:
                break
            else:
                names[l] = True
                c = c + 1


    return str(c) + '\n'
    

f = open('A-large.in')
fw = open('result.out','w+')

n = int(f.readline())

for i in range(1,n+1):
    fw.write('Case #')
    fw.write(str(i))
    fw.write(': ')
    line = f.readline().replace('\n','')
    datas = line.split(' ')
    m = int(datas[0])
    n = int(datas[1])
    disk = ['' for i in range(m)]
    mk   = ['' for i in range(n)]

    for i in range(m):
        disk[i] = f.readline().replace('\n','')
    for i in range(n):
        mk[i] = f.readline().replace('\n','')

    l = calc(disk,mk)
    
    fw.write(l)

f.close()
fw.close()
