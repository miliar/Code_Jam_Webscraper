def input():
    with open('a.in') as file:
        tests_count = int(file.readline().strip())
        for i in xrange(tests_count):
            vines_count = int(file.readline().strip())
            vines = []
            for j in xrange(vines_count):
                vine = tuple(int(n) for n in file.readline().strip().split())
                vines.append(vine)
            distance = int(file.readline().strip())
            yield vines, distance

def output(answers):
    with open('a.out', 'w') as file:
        for i, answer in enumerate(answers):
            file.write('Case #%s: %s\n' % (i + 1, answer))

class Vine(object):
    def __init__(self, distance, length):
        self.distance = distance
        self.length = length
        self.required_length = 1000000000
        self.useful = True


def check((vines, global_distance)):
    #vines.append((distance, 0))
    vines.reverse()
    vines = [Vine(d, l) for d, l in vines]

    #required_vine = Vine(distance, 0)

    for i, vine in enumerate(vines):
        for j in xrange(i):
            next_vine = vines[j]
            if next_vine.useful:
                distance = next_vine.distance - vine.distance
                if vine.length >= distance >= next_vine.required_length:
                    vine.required_length = min(vine.required_length, distance)
        if vine.length >= global_distance - vine.distance:
            vine.required_length = min(vine.required_length, global_distance - vine.distance)
        if vine.required_length > vine.length:
            vine.useful = False

    return vines[-1].useful and vines[-1].required_length <= vines[-1].distance

def main():
    possibilites = (('NO', 'YES')[check(vines)] for vines in input())
    output(possibilites)

if __name__ == '__main__':
    main()