if __name__ == '__main__':
    for tc in range(int(input())):
        _in = input().split(' ')
        cake, w = list(_in[0]), int(_in[1])
        times = 0
        
        for i in range(len(cake)-w+1):
            if cake[i] == '-':
                times += 1
                for j in range(w):
                    if cake[i+j] == '+':
                        cake[i+j] = '-'
                    else:
                        cake[i+j] = '+'
        
        if '-' in cake:
            print("Case #{0}: {1}".format(tc+1, "IMPOSSIBLE"))
        else:
            print("Case #{0}: {1}".format(tc+1, times))