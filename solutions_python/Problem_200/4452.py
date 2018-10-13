amount = int(input())
for i in range(amount):
    number = input()
    l = [int(x) for x in list(number)]
    len_l = len(l)
    for j in range(len_l-1):
        index = len_l - 1 - j
        if l[index] < l[index-1]:
            k = index
            while k<len(l) and l[k] != 9:
                l[k] = 9
                k+=1
            l[index-1] -= 1
    print("Case #{x}: {y}".format(x=i+1, y="".join([str(x) for x in l]).lstrip("0")))
