import numpy as np

f = open('large.in', 'r')
T = int(f.readline())
for t in range(1, T + 1):

    # input# {{{
    R, C = [int(s) for s in f.readline().splitlines()[0].split(' ')]

    li = []
    for i in range(R):
        li += f.readline().splitlines()[0]
    arr = np.array(li).reshape(R, C)
    # }}}

    # calc# {{{
    for i in range(R):
        for j in range(C):
            if(arr[i][j] != '?'):
                for k in range(j-1, -1, -1):
                    if(arr[i][k] == '?'):
                        arr[i][k] = arr[i][j]
                    else:
                        break
                for k in range(j+1, C):
                    if(arr[i][k] == '?'):
                        arr[i][k] = arr[i][j]
                    else:
                        break

    for i in range(0, R):
        if(arr[i][0] != '?'):
            for j in range(i-1, -1, -1):
                if(arr[j][0] =='?'):
                    arr[j] = arr[i]
                else:
                    break;
            for j in range(i+1, R):
                if(arr[j][0] =='?'):
                    arr[j] = arr[i]
                else:
                    break;
    # }}}

    g = open('large.out', 'a')
    print("Case #{}:".format(t), file=g)
    for i in range(R):
        for j in range(C):
            print("{}".format(arr[i][j]), end='', file=g)
        print("", end='\n',  file=g)
