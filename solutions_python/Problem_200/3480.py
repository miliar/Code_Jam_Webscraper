'''
Created on 8 abr. 2017

@author: Dennys
'''
tidy = ""

def if_tidy(N):
    x = 0
    for i in N:
        if x + 1 <= len(N) - 1:
            if int(i) > int(N[x + 1]):
                return False
        x += 1
    return True

exit_loop = False

def calc_tidy(N):           
    global tidy, exit_loop
    
    if if_tidy(N):
        if N != '0':
            tidy = N + tidy
        exit_loop = True 
        return
    
    ini = 0
    z = 0
    while not exit_loop:
        pos = len(N) - ini - 1
        if not exit_loop:
            if pos - 1 >= 0: 
                z = 0
                for y in range(pos - 1, -1, -1):
                    if not exit_loop:
                        if int(N[pos]) < int(N[y]):
                            tidy = '9' * (z + ini + 1) + tidy
                            N = N[:y + 1]
                            calc_tidy(str(int(N) - 1))
                            break
                        else:
                            z += 1
                    else:
                        return
                ini += 1
            else:
                break
        else:
            return           

if __name__ == '__main__':
    t = int(input())  # read a line with a single integer
    if t >= 1 and t <= 100: 
        for i in range(1, t + 1):
            N = int(input())
            if 10 ** 18 >= N and N >= 1:
                ok = True
            if ok:
                tidy = ""
                exit_loop = False
                calc_tidy(str(N))
                print("Case #{}: {}".format(i, tidy))
                
