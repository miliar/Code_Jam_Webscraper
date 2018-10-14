def standing_ovation(audience):
    tot = 0
    req = 0
    for s, n in enumerate(audience):
        if tot >= s:
            tot += n
        else:
            req += s - tot
            tot += n + s - tot
    return req

if __name__ == '__main__':
    cases = int(input())
    for c in range(cases):
        line = input()
        audience = list(map(int, list(line.split()[1])))
        print("Case #{}: {}".format(c+1, standing_ovation(audience)))
