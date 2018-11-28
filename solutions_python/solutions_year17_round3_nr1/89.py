import sys

def bprint(*things):
    #return  # Disable `bprint` function
    for thing in things:
        print >> sys.stderr, thing,
    print >> sys.stderr, ""


def read_input():
    available, to_pick = map(int, raw_input().split())
    pancakes = []
    for _ in xrange(available):
        radius, height = map(int, raw_input().split())
        face = radius * radius
        side = 2 * radius * height
        pancakes.append((face, side))
    return available, to_pick, pancakes

def calculate(input_args):
    available, k, pancakes = input_args

    pancakes.sort(reverse=True)
    face_areas, side_areas = zip(*pancakes)
    #bprint(pancakes)
    #bprint(face_areas, side_areas)

    areas = []
    for picked_cake_idx in xrange(len(pancakes)):
        face_area = face_areas[picked_cake_idx]
        side_area = side_areas[picked_cake_idx]

        max_side_areas = sorted(
                side_areas[(picked_cake_idx+1):], 
                reverse = True)
        #bprint(">", max_side_areas)
        areas.append(face_area + side_area + sum(max_side_areas[:(k-1)]))
    #bprint("<<")

    return max(areas)

from math import pi
def to_formated_string(result_tokens):
    ans = result_tokens
    return "%.9f" % (ans * pi)

if __name__ == '__main__':
    T = int(raw_input())
    case = 1
    while case <= T:
        input_args = read_input()
        result = calculate(input_args)
        answer = to_formated_string(result)
        print 'Case #%d:' % case, answer
        case += 1

