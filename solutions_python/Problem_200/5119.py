
def funcy(x,y):
    for i in range(x, x//2, -1):
        ar2 = []
        ar3 = ""
        if i % 10 != 0:
            k = i
            while k != 0:
                ar2.append(k % 10)
                k = k//10
            del k
            ar2.sort()
            for j in ar2:
                ar3 += str(j)
            if ar3 == str(i):
                print("Case #"+str(y+1) + ': ' + ar3)
                break
b = int(input())
ar4 = []
for m in range(0, b, 1):
    ar4.append(int(input()))

for n in range(0, b, 1):
    funcy(ar4[n], n)
