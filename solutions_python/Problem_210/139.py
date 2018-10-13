from  math import pi

f = open('ans.txt', 'w')

c = int(input())
for i in range(1,c+1):
    c, j = map(int, input().split())
    if (c == 1 and j == 0) or (j == 1 and c == 0):
        a, b = map(int, input().split())
        f.write(f"Case #{i}: 2\n")
    elif c == 2 or j == 2:
        a, b = map(int, input().split())
        a2, b2 = map(int, input().split())
        if (0 < b2 +1440 - a <= 720) or (0 < b+1440-a2 <= 720)or (0 < b2-a <= 720) or (0 < b-a2 <= 720):
            f.write(f"Case #{i}: 2\n")
        else:
            f.write(f"Case #{i}: 4\n")

    else:
        a, b = map(int, input().split())
        a2, b2 = map(int, input().split())
        f.write(f"Case #{i}: 2\n")
f.close()