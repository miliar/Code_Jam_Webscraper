def check(number):
    numstr = str(number)
    blanka = ''
    while numstr and numstr[-1] is '9':
        blanka += '9'
        if len(numstr) != 1:
            numstr = numstr[:-1]
        else:
            return int(blanka)
    number = int(numstr)
    n = numstr[0]
    for i in numstr[1:]:
        if int(i) < int(n):
            rebuilt = str(number - 1) + blanka
            return int(rebuilt)
        n = i
    rebuilt = str(number) + blanka
    return int(rebuilt)


def tidy(number):
    checked = check(number)
    while checked != check(checked):
        checked = check(checked)
    return(checked)


with open('B-large.in.txt') as f, open('b-large-out.txt', 'w') as g:
    n = int(f.readline())
    for i in range(n):
        number = int(f.readline())
        tidied = tidy(number)
        # print('Case #{:}: {}'.format((i + 1), tidied))
        g.write('Case #{:}: {}\n'.format((i + 1), tidied))
