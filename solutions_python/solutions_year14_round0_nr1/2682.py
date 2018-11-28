import fileinput

def process(cards):
    row_1 = int(cards[0])
    row_2 = int(cards[5])

    num1 = [int(x) for x in cards[row_1].split()]
    num2 = [int(x) for x in cards[row_2+5].split()]
    cnt = []
    for x in num1:
        if x in num2:
            cnt.append(x)

    if len(cnt) == 1:
        return cnt[0]
    elif cnt == []:
        return "Volunteer cheated!"
    else:
        return "Bad magician!"






def main():
    fin = fileinput.input()
    T = int(next(fin)) # number of test cases
    for case in range(1, T+1):
        N = 10
        skaters = [next(fin).strip() for _ in range(N)]
        cost = process(skaters)
        print("Case #{}: {}".format(case, cost))


if __name__ == '__main__':
    main()
