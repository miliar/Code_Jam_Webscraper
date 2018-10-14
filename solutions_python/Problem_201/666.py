__author__ = 'snv'

def left(N):
    return (N-1)//2

def right(N):
    return N//2

# sys.setrecursionlimit(10001)

# f = open('input.txt','r')
f = open('C-large.in','r')
g = open('output.txt', 'w')
T = int(f.readline())
for j in range(T):
    N_stalls, N_users = f.readline().split()
    N_stalls, N_users = int(N_stalls), int(N_users)
    bin_users = str(bin(N_users))[3:]
    row = len(bin_users)
    quant = (2**row)
    mn = N_stalls // quant -1
    rm = N_users - quant
    extra = N_stalls - quant*(mn+1)
    print('stalls', N_stalls, 'users=', N_users, 'bin', bin_users, 'avg', mn, 'extra = ', extra, 'users_left', rm )
    if rm <= extra:
        mn +=1
    left = (mn-1) //2
    right = mn //2
    ans = str(right) +' ' + str (left)
    ans_string = 'Case #{0}: {1}\n'.format(j+1, ans)
    print(ans_string)
    g.write(ans_string)
f.close()
g.close()

