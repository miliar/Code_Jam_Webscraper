# -*- coding: utf-8 -*-
# <nbformat>3.0</nbformat>

# <codecell>

T = int(input())
#print(T)
for j in range(0,T):
    a1 = int(input())
    arr1 = []
    for i in range(0,4):
        temp = [int(x) for x in input().split(' ')]
        arr1.append(temp)
    a2 = int(input())
    arr2 = []
    for i in range(0,4):
        temp = [int(x) for x in input().split(' ')]
        arr2.append(temp)

    final = set(arr1[a1-1]).intersection( set(arr2[a2-1]) )
    #print(final)
    print('Case #' + str(j+1) + ': ', end="")
    if len(final) == 1:
        print(final.pop())
    elif len(final) > 1:
        print("Bad magician!")
    else:
        print("Volunteer cheated!")
# <codecell>


