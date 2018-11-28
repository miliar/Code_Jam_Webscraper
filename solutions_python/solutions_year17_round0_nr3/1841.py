t = int(input())
outputlist = [0]*t
for i in range(t):
    inline = input()
    inline = inline.split()
    n = int(inline[0])
    k = int(inline[1])
    toilet = [1] + [0]*n + [1]

    for kloop in range(k):
        lower = 0
        upper = 0
        dist = upper-lower
        temp = 0
        for j in range(n+1):
            if toilet[j+1] == 1:
                if ((j+1) - temp) > dist:
                    lower = temp
                    upper = j+1
                    dist = upper - lower
                temp = j+1
        mid = (lower+upper)//2
        toilet[mid] = 1
        ls = mid - lower - 1
        rs = upper - mid - 1

    if ls>rs:
        outputlist[i] = 'Case #' + str(i+1) + ': ' + str(ls) + ' ' + str(rs)
    else:
        outputlist[i] = 'Case #' + str(i+1) + ': ' + str(rs) + ' ' + str(ls)

for i in range(t):
    print(outputlist[i])
