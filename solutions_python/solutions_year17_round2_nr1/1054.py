def calculate():
    D, N = map(int, input().split(" "))
    datamap = []

    def get_time(data):
        dist, speed = data
        dist = D - dist
        return dist / speed

    for i in range(N):
        datamap.append(tuple(map(int, input().split(' '))))

    datamap = list(map(get_time, datamap))
    return D / max(datamap)


if __name__ == '__main__':
    T = int(input())
    for i in range(T):
        result = calculate()
        print("Case #%d: %.6f" % (i + 1, result))
