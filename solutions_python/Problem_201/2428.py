'''
Created on 8 abr. 2017

@author: Dennys
'''

def calc_stalls(N, K):
    a = []
    less = int(0)
    more = int(0)
    mm = more
    for i in range(1, K + 1):   
        if len(a) == 0:
            if N % 2 == 0:
                less = int(N / 2) - 1
                more = int(N / 2)
            else:
                less = int((N - 1) / 2)
                more = int((N - 1) / 2)
            a.append(less)
            a.append(more)
            mm = more
        else:
            x = 0
            for j in a:
                if j >= max(a):
                    if j % 2 == 0:
                        less = int(j / 2) - 1
                        more = int(j / 2)
                    else:
                        less = int((j - 1) / 2)
                        more = int((j - 1) / 2)
                    if (less == 0 and more == 0):
                        if x + 1 <= len(a) - 1:
                            a = a[:x] + a[x + 1:]
                        else:
                            a = a[:x]
                        return str(more) + ' ' + str(less)
                    elif (less == 0 and more != 0) or (less != 0 and more == 0):
                        a[x] = less + more
                        mm = more
                    else:                                
                        a[x] = less
                        if x + 1 <= len(a) - 1:
                            a = a[:x + 1] + [more] + a[x + 1:]
                        else:
                            mm = more
                            a.append(more)                    
                    break
                x += 1
        #print(a)
    return str(more) + ' ' + str(less)
        
if __name__ == '__main__':
    # input() reads a string with a line of input, stripping the '\n' (newline) at the end.
    # This is all you need for most Google Code Jam problems.
    t = int(input())  # read a line with a single integer
    if t >= 1 and t <= 100:
        for i in range(1, t + 1):
            N, K = [int(s) for s in input().split(" ")]  # read a list of integers, 2 in this case
            if K >= 1and N >= K and 10 ** 18 >= N:
                print("Case #{}: {}".format(i, calc_stalls(N, K)))
                # check out .format's specification for more formatting options
        pass
