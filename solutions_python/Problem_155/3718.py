def how_many_guests(max_shyness, audience):
    max_shyness = int(max_shyness)
    audience = [int(digit) for digit in list(audience)]
    extra_guests = 0
    clapping = audience[0]
    for i in range(1, len(audience)):
        if audience[i] > 0 and i > clapping:
            extra_guests += i - clapping
            clapping += extra_guests
        clapping += audience[i]
    return extra_guests


if __name__ == '__main__':
    tests = int(raw_input())
    for t in range(tests):
        line = raw_input()
        max_shyness, audience = line.split(' ')
        extra_guests = how_many_guests(max_shyness, audience)
        print 'Case #%s: %s' % (t + 1, extra_guests)
