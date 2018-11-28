def check_mkdirs(l, dic, mkds):
    if l:
        if l[0] not in dic:
            dic[l[0]] = dict()
            mkds[0] += 1

        check_mkdirs(l[1:], dic[l[0]], mkds)
    else:
        return 

#def add_existing(l, dic):
#    if l:
        

f = open('A-large.in', 'r+')
o = open('Result.out', 'w+')
cases = int(f.readline())
case_num = 1

while(cases != 0):
    config = f.readline().split()
    exist = int(config[0])
    create = int(config[1])

    dic = dict()

    for i in range(0, exist):
        mkds = [0]
        dir_exist = f.readline().split("\n")
        delen = len(dir_exist)
        if dir_exist[delen - 1] == '':
            dir_exist = dir_exist[0:delen - 1]
        dir_exist = dir_exist[0].split("/")[1:]
        check_mkdirs(dir_exist, dic, mkds)        
        
    total_mkds = 0
    for j in range(0, create):
        mkds = [0]
        dir_create = f.readline().split("\n")
        dclen = len(dir_create)
        if dir_create[dclen - 1] == '':
            dir_create = dir_create[0:dclen - 1]
        dir_create = dir_create[0].split("/")[1:]

        check_mkdirs(dir_create, dic, mkds)
        total_mkds += mkds[0]
    
    print total_mkds

    o.write("Case #" + str(case_num) + ": " + str(total_mkds) + "\n")
                    
    cases -= 1
    case_num += 1

f.close()    
o.close()
