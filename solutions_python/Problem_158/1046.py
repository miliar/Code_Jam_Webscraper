from parse import *

def main():
    cases = int(input())
    for case in range(cases):
        r = parse('{x} {r} {c}', input())
        if placement_is_possible(int(r['x']), int(r['r']), int(r['c'])):
            winner = 'GABRIEL'
        else:
            winner = 'RICHARD'
        print('Case #{}: {}'.format(case+1, winner))

def placement_is_possible(x, r, c):

    # if is big enough to make a hole
    if x > 6:
        return False

    # if number of tiles makes it impossible
    if not (r*c)%x is 0:
        return False

    # if line could be made that cannot fit
    if x > max(r, c):
        return False

    # if l shape can be made that is always wider than the smaller dimension
    if x%2 is 1:
        l_shape_size = (x + 1)/2
    else:
        l_shape_size = x/2

    if l_shape_size > min(r, c):
        return False

    # if a bar can be made across and there are enough tiles to cover

    if x > min(r, c):
        remaining = x - min(r, c)

        if remaining + 1 > min(r, c):
            for size in range(1, remaining):
                placeble = False
                tiles = min(r, c)*(max(r, c)-2) - size
                while tiles > 0:
                    if tiles%x is 0:
                        placeble = True

                    tiles -= min(r, c)

                if not placeble:
                    return False

    return True

if __name__ == '__main__':
    main()
