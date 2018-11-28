def do():
    times = eval(input())
    for i in range(1,times+1):
        print('Case #%d:'%i,end=" ")
        calculate()

def out_flow(block,x,y,d):
    if d == '^':
        dx,dy = -1,0
    elif d == 'v':
        dx,dy = 1,0
    elif d == '<':
        dx,dy = 0,-1
    elif d == '>':
        dx,dy = 0,1
    else:
        return False

    x,y = x+dx,y+dy
    while 0<=x<len(block) and 0<=y<len(block[x]):
        if block[x][y] != '.':
            return False
        x,y = x+dx,y+dy
    return True

def calculate():
    R,C = map(int,input().split())

    block = [input() for i in range(R)]

    direct = "^>v<"

    count = 0

    for i in range(R):
        for j in range(C):
            if out_flow(block,i,j,block[i][j]):
                for d in direct:
                    if block[i][j] != d and not out_flow(block,i,j,d):
                        count += 1
                        break
                else:
                    print("IMPOSSIBLE")
                    return

    print(count)



if __name__ == '__main__':
    do()

