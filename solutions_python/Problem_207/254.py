f = open('ans2.txt', 'w')
T = int(input())
for i in range(1,T+1):
    N, R, O, Y, G, B, V = list(map(int, input().split()))
    if R > N//2 or Y > N//2 or B > N//2:
        ans = "IMPOSSIBLE"
    else:
        if R >= Y and R >= B:
            temp = ["R", '', '']*R
            for j in range(Y):
                temp[j*3+1] = "Y"
            for j in range(Y, R):
                temp[j*3+2] = "B"
            u = 0
            B-=(R-Y)
            while B != 0:
                if temp[u] == '':
                    temp[u] = "B"
                    B-=1
                u+=1
        elif Y >= R and Y >= B:
            temp = ["Y", '', '']*Y
            for j in range(R):
                temp[j*3+1] = "R"
            for j in range(R, Y):
                temp[j*3+2] = "B"
            u = 0
            B-=(Y-R)
            while B != 0:
                if temp[u] == '':
                    temp[u] = "B"
                    B-=1
                u+=1
        elif B >= Y and B >= R:
            temp = ["B", '', '']*B
            for j in range(Y):
                temp[j*3+1] = "Y"
            for j in range(Y, B):
                temp[j*3+2] = "R"
            u = 0
            R-=(B-Y)
            while R != 0:
                if temp[u] == '':
                    temp[u] = "R"
                    R-=1
                u+=1
        ans = "".join(temp)
        print(i, temp)
    f.write(f"Case #{i}: {ans}\n")