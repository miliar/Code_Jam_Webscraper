def init():
    t = int(input())

    if t >= 1 and t <= 100:
        for i in range(1, t + 1):
            s, k = [str(m) for m in input().split(" ")]
            k = int(k)

            if k >= 2 and k <= len(s):
                result = 0  # veces que se necesita rotar el panqueque
                index = 0
                while index < len(s):
                    if s[index] is not "+":
                        if index + k <= len(s):
                            flipedPancakes = flip(s[index:index + k])
                            s = s[:index] + flipedPancakes + s[index + k:]
                            result += 1
                        else:
                            break
                    index += 1

                if evaluatePancakes(s):
                    print("Case #{}: {}".format(i, result))
                else:
                    print("Case #{}: IMPOSSIBLE".format(i))
            else:
                print("Case #{}: IMPOSSIBLE".format(i))


def flip(pancakes):
    newPancakes = []
    for pancake in pancakes:
        if pancake == '+':
            pancake = '-'
            newPancakes.append(pancake)
        else:
            pancake = '+'
            newPancakes.append(pancake)
    return ''.join(newPancakes)

def evaluatePancakes(pancakes):
    i = 0
    result = True
    while i < len(pancakes):
        if pancakes[i] is not "+":
            result = False
            break
        i += 1
    return result


init()
