
def get_answer(n):

    sz = len(n)
    n = [int(i) for i in n]

    for i in range(sz-2, -1, -1):
        if n[i] > n[i+1]:
            n[i] -= 1
            n[i+1] = 9

    nine = False
    answer = []
    st = 0
    while st < sz and n[st] == 0:
        st += 1
    for i in range(st, sz):
        if n[i] == 9 or nine:
            nine = True
            answer.append('9')
        else:
            answer.append(str(n[i]))
    return ''.join(answer)

t = int(input())
for i in range(1, t + 1):
    n = input()
    answer = get_answer(n)
    print("Case #{}: {}".format(i, answer))

