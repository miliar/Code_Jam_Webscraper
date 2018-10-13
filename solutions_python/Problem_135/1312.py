t = int(input())

for ttt in range(t):
    print("Case #%d:" % (ttt+1), end=" ")
    l = int(input())
    L = []
    for i in range(4):
        L.append(input().split(" "))
    m = int(input())
    M = []
    for i in range(4):
        M.append(input().split(" "))
    W = list(set(L[l-1]) & set(M[m-1]))
    if len(W)==1:
        print(W[0])
    elif len(W)==0:
        print("Volunteer cheated!")
    else:
        print("Bad magician!")