
BLANK = '-'
HAPPY = '+'

def allSameFaces(pancakes):
    init_face = pancakes[0]
    for face in pancakes[1:]:
        if init_face != face:
            return False
    return True

def allHappyFaces(same_face_pancakes):
    return same_face_pancakes[0] == '+'

def fp(total_pancakes, pancakes, flipper):
    total_flip = 0
    p_index = 0
    while p_index < total_pancakes:
        if pancakes[p_index] == BLANK:
            if p_index + flipper > total_pancakes:
                break
            for i in range(p_index, p_index+flipper):
                if pancakes[i] == HAPPY:
                    pancakes[i] = BLANK
                else:
                    pancakes[i] = HAPPY
            total_flip += 1
        p_index += 1
    for i in pancakes:
        if i == BLANK:
            return 'IMPOSSIBLE'
    return total_flip

def pancakeFlipper(pancakes, flipper):
    total_pancakes = len(pancakes)
    if allSameFaces(pancakes):
        if allHappyFaces(pancakes):
            return 0
        elif (total_pancakes % flipper) == 0:
            return int(total_pancakes / flipper)
        else:
            return 'IMPOSSIBLE'
    elif total_pancakes == flipper:
        return 'IMPOSSIBLE'
    return fp(total_pancakes, pancakes, flipper)


if __name__ == '__main__':
    t = int(input())
    for i in range(1, t + 1):
        pancakes, flipper = input().split(' ')
        print("Case #{}: {}".format(i, pancakeFlipper(list(pancakes), int(flipper))))
