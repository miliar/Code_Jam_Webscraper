__author__ = 'remi'


filename = "A-small-attempt0.in.txt"
amount = 0
row1 = set()
row2 = set()

f = open(filename, 'r')


amount = int(f.readline())

for i in range(1, amount+1):
    n = int(f.readline())
    for j in range(1, 5):
        if j == n:
            row1 = set(map(int, f.readline().split()))
        else:
            f.readline()

    n = int(f.readline())
    for j in range(1, 5):
        if j == n:
            row2 = set(map(int, f.readline().split()))
        else:
            f.readline()

    pos = row1 & row2

    if len(pos) == 0:
        print("Case #"+str(i)+": Volunteer cheated!")
    elif len(pos) == 1:
        print("Case #"+str(i)+": "+str(list(pos)[0]))
    else:
        print("Case #"+str(i)+": Bad magician!")
