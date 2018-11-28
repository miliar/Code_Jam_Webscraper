

def solve(ponies):
    total, red, orange, yellow, green, blue, violet = ponies
    result = solve2(ponies, 0)
    if result != "IMPOSSIBLE":
        return result
    result = solve2(ponies, 1)
    if result != "IMPOSSIBLE":
        return result
    result = solve2(ponies, 2)
    if result != "IMPOSSIBLE":
        return result
    assert red > yellow + blue or yellow > red + blue or blue > yellow + red
    return "IMPOSSIBLE"

def solve2(ponies, current=""):
    #total, red, orange, yellow, green, blue, violet = ponies
    _, red, _, yellow, _, blue, _ = ponies
    colors = [red, yellow, blue]
    letters = ["R", "Y", "B"]
    result = ""
    while max(colors) > 0:
        sorted_colors = sorted(list(range(3)), key=lambda index: colors[index], reverse=True)
        if current in sorted_colors:
            sorted_colors.remove(current)
        current = sorted_colors[0]
        if colors[current] == 0:
            return "IMPOSSIBLE"
        colors[current] -= 1
        result += letters[current]
    if result[0] == result[-1]:
        return "IMPOSSIBLE"
    return result

def main():
    cases = int(input())
    for case in range(1, cases+1):
        ponies = tuple(int(x) for x in input().rstrip().split(" "))
        print("Case #%d: %s" % (case, solve(ponies)))

if __name__ == '__main__':
    main()
