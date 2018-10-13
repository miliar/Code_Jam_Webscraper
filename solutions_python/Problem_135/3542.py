fin = open("input.in", "r")
fout = open("output.txt", "w")
t = int(fin.readline().strip())
a = []
n = 0
for i in range(1, t + 1):
    n = int(fin.readline().strip())
    for j in range(1, 5):
        a = list(map(int, fin.readline().split()))
        if j == n:
            now = set(a)
    n = int(fin.readline().strip())
    for j in range(1, 5):
        a = list(map(int, fin.readline().split()))
        if j == n:
            now &= set(a)  
    print("Case #", i, ":", sep = '', end = ' ', file = fout)
    if len(now) == 1:
        print(list(now)[0], file = fout)
    elif len(now) == 0:
        print("Volunteer cheated!", file = fout)
    else:
        print("Bad magician!", file = fout)
fout.close()
    