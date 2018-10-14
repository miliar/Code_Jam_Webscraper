dic = {'+': '-', '-': '+'}


def recur(st, k):
    # import ipdb
    # ipdb.set_trace()
    if all(l == '+' for l in st):
        return 0
    i0 = st.index('-')
    i1 = len(st) - st[::-1].index('-') - 1
    sub_s = st[i0:i1 + 1]
    if len(sub_s) < k:
        return None
    elif len(sub_s) == k:
        if all(a == '-' for a in sub_s):
            return 1
        else:
            return None
    else:
        r = recur(flip(sub_s, k), k)
        return 2 + r if r is not None else None


def flip(st, k):
    st = [dic[a] for a in st[0:k]] + st[k:]
    st = st[0:len(st) - k] + [dic[a] for a in st[-k:]]
    return st


def main():
    with open('data.txt') as f:
        T = f.readline()
        case = 0
        for line in f:
            case += 1
            s, k = line.split(' ')
            s = [l for l in s]
            k = int(k.strip())
            result = recur(s, k)
            print('Case #' + str(case) + ': ' +
                  (str(result) if result is not None else 'IMPOSSIBLE'))


main()
