def stalls(nb_stalls, nb_people):
    if nb_stalls == nb_people:
        return '0 0'
    if nb_stalls == nb_people - 1:
        return '0 0'
    stalls = [[0, nb_stalls]]
    for _ in range(nb_people):
        stalls = sorted(stalls, key=lambda x: x[1], reverse=True)
        tmp = stalls[0][1]
        stalls[0][1] = int((tmp - 1) / 2)
        stalls.append([stalls[0][0] + stalls[0][1] + 1, int(tmp / 2)])
    a, b = stalls[0][1], stalls[-1][1]
    a, b = max([a, b]), min([a, b])
    return str(a) + ' ' + str(b)

def main():
    nb_test = int(input())
    for _ in range(nb_test):
        args = [int(_) for _ in input().split()]
        print('Case #' + str(_ + 1) + ': ' + stalls(*args))

if __name__ == '__main__':
    main()