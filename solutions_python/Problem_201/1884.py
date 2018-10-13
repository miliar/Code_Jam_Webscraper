def determine(n, k):
    lst = [0, n + 1]
    val = None
    mx = None
    mn = None
    pos = None

    for i in range(k):
        val = None
        mx = None
        mn = None
        pos = None

        new_val = None
        new_mx = None
        new_mn = None
        new_pos = None

        for j in range(len(lst) - 1):
            if lst[j] != lst[j + 1]:
                if val == None:
                    val = (lst[j] + lst[j + 1]) // 2
                    pos = j + 1
                    mx = max(lst[j + 1] - val - 1, val - lst[j] - 1)
                    mn = min(lst[j + 1] - val - 1, val - lst[j] - 1)
                else:
                    new_val = (lst[j] + lst[j + 1]) // 2
                    new_pos = j + 1
                    new_mx = max(lst[j + 1] - new_val - 1, new_val - lst[j] - 1)
                    new_mn = min(lst[j + 1] - new_val - 1, new_val - lst[j] - 1)
                    if new_mn > mn:
                        val, pos, mx, mn = new_val, new_pos, new_mx, new_mn
                        #print(val)
                    elif new_mn == mn and new_mx > mx:
                        val, pos, mx, mn = new_val, new_pos, new_mx, new_mn
                        #print(val)
        lst.insert(pos, val)
        #print(val)
    return str(mx), str(mn)

T = int(input())
for i in range(T):
    n, k = map(int, input().split())
    print("Case #" + str(i + 1) + ": " + ' '.join(determine(n, k)))