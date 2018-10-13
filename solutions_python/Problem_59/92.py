import time

print (time.ctime())

f_in = open('c:/temp/codejam/round1b/A-large.in')
f_out = open('c:/temp/codejam/round1b/A-large.out','w')

T = int(f_in.readline())
for case in range(1,T+1):
    
    N, M = [int(x) for x in f_in.readline().split()]
    
    existing_directories = {():1}
    for i in range(N):
        path = ''.join(f_in.readline().split())
        if path[-1] == '/':
            path = path[:-1]
        path_list = tuple(path.split('/'))[1:]
        for p in range(len(path_list)+1):
            existing_directories [path_list[:p]] = 1

    mkdir_commands = 0

    for i in range(M):
        path = ''.join(f_in.readline().split())
        if path[-1] == '/':
            path = path[:-1]
        path_list = tuple(path.split('/'))[1:]
        p = len(path_list)
        while path_list[:p] not in existing_directories:
            p -= 1
            mkdir_commands += 1
        for p in range(len(path_list)+1):
            existing_directories [path_list[:p]] = 1

    res = mkdir_commands       

    f_out.write('Case #' + str(case) + ': ' + str(res) + '\n')

f_out.close()
f_in.close()

print (time.ctime())


