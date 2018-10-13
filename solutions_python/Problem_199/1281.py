def flipper(string, k):
    string_list = list(string)
    count = 0
    for i in range(len(string_list) - k + 1):
        if string_list[i] == '+':
            continue
        count += 1
        for j in range(i, i + k):
            string_list[j] = flip(string_list[j])
    if '-' in string_list:
        return 'IMPOSSIBLE'
    else:
        return count


def flip(char):
    if char == '+':
        return '-'
    else:
        return '+'


if __name__ == '__main__':
    T = int(input())
    for t in range(T):
        S, K = input().split()
        print("Case #{x}: {y}".format(x=t + 1, y=flipper(S, int(K))))