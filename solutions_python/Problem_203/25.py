import collections

def main():
    for testcase in range(1, int(input()) + 1):
        print(f"Case #{testcase}: {solve()}")

def fill_row(row):
    c = len(row)
    if row == ['?']*c:
        return row
    first_char = None
    curr_char = None
    for i in range(c):
        if row[i] != '?':
            curr_char = row[i]
            if not first_char:
                for j in range(i):
                    row[j] = curr_char
                first_char = True
        else:
            if curr_char:
                row[i] = curr_char
    return row

def display(karta):
    return '\n'.join([''.join(row) for row in karta])

def solve():
    r, c = map(int, input().strip().split())
    karta = [list(input()) for _ in range(r)]

    mytest = False
    for i in range(r):
        if karta[i] != ['?']*c:
            karta[0], karta[i] = karta[i], karta[0]
            mytest = True
            break
    assert mytest
    # fill rows
    karta = [fill_row(row) for row in karta]
    for i in range(1, r):
        if karta[i] == ['?']*c:
            karta[i] = karta[i-1]
    return "\n" + display(karta)


main()
