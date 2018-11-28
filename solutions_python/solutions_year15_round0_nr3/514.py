def solve(f):
    yes = "YES"
    no = "NO"

    mul = {
        'i': {
            'i': '-1',
            'j': 'k',
            'k': '-j',
            '1': 'i',
            '-1': '-i',
            '-i': '1',
            '-j': '-k',
            '-k': 'j'
        },
        'j': {
            'i': '-k',
            'j': '-1',
            'k': 'i',
            '1': 'j',
            '-1': '-j',
            '-i': 'k',
            '-j': '1',
            '-k': '-1'
        },
        'k': {
            'i': 'j',
            'j': '-i',
            'k': '-1',
            '1': 'k',
            '-1': '-k',
            '-i': '-j',
            '-j': 'i',
            '-k': '1'
        },
        '1': {
            'i': 'i',
            'j': 'j',
            'k': 'k',
            '1': '1',
            '-1': '-1',
            '-i': '-i',
            '-j': '-j',
            '-k': '-k'
        },
        '-1': {
            'i': '-i',
            'j': '-j',
            'k': '-k',
            '1': '-1',
            '-1': '1',
            '-i': 'i',
            '-j': 'j',
            '-k': 'k'
        },
        '-i': {
            'i': '1',
            'j': '-k',
            'k': 'j',
            '1': '-i',
            '-1': 'i',
            '-i': '-1',
            '-j': 'k',
            '-k': '-j'
        },
        '-j': {
            'i': 'k',
            'j': '1',
            'k': '-i',
            '1': '-j',
            '-1': 'j',
            '-i': '-k',
            '-j': '-1',
            '-k': 'i'
        },
        '-k': {
            'i': '-j',
            'j': 'i',
            'k': '1',
            '1': '-k',
            '-1': 'k',
            '-i': 'j',
            '-j': '-i',
            '-k': '-1'
        }
    }

    line = f.readline().split(" ")
    l = int(line[0])
    x = int(line[1])

    arr = f.readline().split()[0]

    if x % 4 == 0:
        return no

    total_parsed = 0
    parsed = 0
    max_parse_required = 4 * l
    reduced = '1'

    index = 0
    # parse i
    while (parsed < max_parse_required and total_parsed < l * x) and reduced != 'i':
        parsed += 1
        total_parsed += 1
        reduced = mul[reduced][arr[index]]
        index = (index + 1) % l

    if reduced is not 'i':
        return no

    reduced = '1'
    parsed = 0

    # parse j
    while (parsed < max_parse_required and total_parsed < l * x) and reduced != 'j':
        parsed += 1
        total_parsed += 1
        reduced = mul[reduced][arr[index]]
        index = (index + 1) % l

    if reduced is not 'j':
        return no

    reduced = '1'
    parsed = 0

    # parse k
    while (parsed < max_parse_required and total_parsed < l * x) and reduced != 'k':
        parsed += 1
        total_parsed += 1
        reduced = mul[reduced][arr[index]]
        index = (index + 1) % l

    if reduced is not 'k':
        return no

    reduced = '1'
    parsed = 0
    max_parse_required = (l * x - total_parsed) % (4 * l)

    # get to 1
    while parsed < max_parse_required and total_parsed < l * x:
        parsed += 1
        total_parsed += 1
        reduced = mul[reduced][arr[index]]
        index = (index + 1) % l

    if reduced is not '1':
        return no

    return yes
