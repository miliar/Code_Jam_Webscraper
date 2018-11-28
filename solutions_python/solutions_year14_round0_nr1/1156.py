n = int(input())
for i in range(n):
    row_1 = int(input())
    arrang_1 = [map(int,raw_input().split(' ')) for x in range(4)]
    row_2 = int(input())
    arrang_2 = [map(int,raw_input().split(' ')) for x in range(4)]

    result = [x for x in arrang_1[row_1-1] if x in arrang_2[row_2-1]]
    if len(result) == 0:
        print("Case #"+str(i+1)+": "+"Volunteer cheated!")
    elif len(result) == 1:
        print("Case #"+str(i+1)+": "+str(result[0]))
    else:
        print("Case #"+str(i+1)+": "+"Bad magician!")
