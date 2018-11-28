if __name__ == '__main__':
    f = open('input')
    n = int(f.readline().rstrip())

    for case in range(n):
        values = f.readline().rstrip().split()
        shyness_max = int(values[0])
        audience = values[1]
        audience = [int(x) for x in audience]

        clapping = 0
        invited = 0
        for level, people in enumerate(audience):
            if level > shyness_max: break
            inviting = 0
            if level > clapping:
                inviting += level - clapping
            clapping += inviting + people
            invited += inviting

        print('Case #{0}: {1}'.format(case + 1, invited))
