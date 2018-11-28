def solve(l, x, str):
    character = '1'
    positive = True
    characters_found = 0
    position = 0
    iteration = 0
    while iteration < x:
        # do the multiplication
        #print("multiplying %s%s by %s" % (' ' if positive else '-', character, str[position]))
        product = table[character][str[position]]
        positive ^= (product[0] == '-')
        character = product[1]
        #print("%s%s" % (' ' if positive else '-', character))
        
        # advance the position
        position += 1
        if position == l:
            position = 0
            iteration += 1
        
        # check if new character found
        if positive and ((characters_found == 0 and character == 'i') or (characters_found == 1 and character == 'j')):
            characters_found += 1
            character = '1'
        
    return characters_found == 2 and positive and character == 'k'

table = {
    '1': {
        '1': ' 1',
        'i': ' i',
        'j': ' j',
        'k': ' k',
    },
    'i': {
        '1': ' i',
        'i': '-1',
        'j': ' k',
        'k': '-j',
    },
    'j': {
        '1': ' j',
        'i': '-k',
        'j': '-1',
        'k': ' i',
    },
    'k': {
        '1': ' k',
        'i': ' j',
        'j': '-i',
        'k': '-1',
    },
}

testcase_count = int(input())
for testcase_index in range(testcase_count):
    testcase_data = input().split()
    l = int(testcase_data[0])
    x = int(testcase_data[1])
    str = input()
    solvable = solve(l, x, str)
    print("Case #%d: %s" % (testcase_index + 1, "YES" if solvable else "NO"))
    
