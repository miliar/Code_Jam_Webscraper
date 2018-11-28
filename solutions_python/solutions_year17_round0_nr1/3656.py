def result(s, flip):
    l = []
    for el in s:
        l.append(el)
    count = 0
    for i in range(0, len(l)):
        if l[i] == "-":
            try:
                for j in range(i, flip + i):
                    if l[j] == "+":
                        l[j] = "-"
                    else:
                        l[j] = "+"
            except IndexError:
                return "IMPOSSIBLE"

            count += 1
    return (count)

row_count = 0
number = int(input())
with open("a_big.txt", "w") as w:
    for i in range(number):
        s, flip = input().split()
        func_out = result(s, int(flip))
        w.write("Case #{}: {} \n".format(i+1, func_out))


