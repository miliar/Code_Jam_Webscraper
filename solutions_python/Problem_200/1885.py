

case = 1

n = eval(input())
while (n > 0):
    num_str = input()
    num = int(num_str)

    isTidy = False
    n_old = num_str[-1]
    i = len(num_str)
    while(not isTidy):
        isTidy = True
        for c in reversed(num_str):
            if (int(c) > int(n_old)):
                isTidy = False
                # print(num_str[i:])
                sub = int(num_str[i:])-1
                if (sub <= 0):
                    sub = 1
                num = num - sub
                num_str = str(num)
                i = len(num_str)
                n_old = num_str[-1]
                break
            n_old = c
            i = i - 1

    print("Case #" + str(case) + ": " + num_str)
    n = n - 1
    case = case + 1
