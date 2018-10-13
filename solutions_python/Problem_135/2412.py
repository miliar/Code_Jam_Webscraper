import sys
sys.stdout = open("out.txt","w")
T = int(input())
for q in range(T):
    a1 = int(input())
    mat1 = [list(map(int, input().split())) for i in range(4)]
    set1 = set(mat1[a1 - 1])
    a2 = int(input())
    mat2 = [list(map(int, input().split())) for i in range(4)]
    set2 = set(mat2[a2 - 1])
    ns = set1 & set2
    if len(ns) == 0:
        ans = "Volunteer cheated!"
    elif len(ns) > 1:
        ans = "Bad magician!"
    else:
        ans = str(list(ns)[0])
    print("Case #%s: %s" % (q + 1, ans))
