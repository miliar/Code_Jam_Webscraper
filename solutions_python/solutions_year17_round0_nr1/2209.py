def flip(state, size, location):
    l = len(state)
    b = ""
    i = 0
    b = "0" * (location - i) + "1" * size + "0" * (l - size - location)
    f = "0" + str(len(b)) + "b"
    return format((int(state, 2) ^ int(b, 2)), f)


def test_possible(init_state, size):
    init_state = init_state.replace("+", "1").replace("-", "0")
    test_state = init_state
    flips = 0
    while test_state.find("0") != -1:
        loc = test_state.find("0")
        if loc + size > len(init_state):
            return "IMPOSSIBLE"
        test_state = flip(test_state, size, loc)
        flips += 1
    return str(flips)


t = int(input())
for i in range(1, t + 1):
    n, m = input().split(" ")
    m = int(m)
    print("Case #" + str(i) + ": " + test_possible(n, m))
