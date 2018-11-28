def cost(c,f,r,x):
    return 

def timeit(c,f,x):
    farms = 0
    investment = 0
    r = 2.0
    ans = cost = x/(r+f*farms)
    # keep investing as long as it reduces the time to reach x 
    while ans >= cost:
        # consider the cost of building one more farm
        investment += c/(r+f*farms)
        # build the farm
        farms += 1
        # calculate the alternative cost
        cost = investment + x/(r+f*farms)
        if ans > cost:
            ans = cost

    return ans

if __name__ == '__main__':
    T = int(input())
    for case in range(T):
        C,F,X = [float(x) for x in input().split()]
        ans = timeit(C,F,X)
        print('Case #{}: {:.7f}'.format(case+1, ans))
