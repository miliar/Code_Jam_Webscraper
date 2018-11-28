#!/usr/bin/python


def transform(alien_number, source_language, target_language):

    source_base = len(source_language)
    target_base = len(target_language)

    i = 0
    x = 0
    for c in reversed(list(alien_number)):
        x += source_language.find(c) * source_base ** i
        i += 1

    i = 0
    r = x
    while (r >= 1):
        r /= target_base
        i += 1

    number = ''
    for p in range(i - 1, -1, -1):
        number += target_language[(x // target_base ** p)]
        x %= target_base ** p

    return number

input_file = open('A-large.in')
output_file = open('output', 'w')

N = int(input_file.readline())



for n in range(N):
    target_language = '0123456789'
    alien_number = input_file.readline().rstrip("\n")
    anlist = list(alien_number)

    sllist = ['A', 'B']
    if len(anlist) == 1:
        sllist[1] = anlist[0]
    else:
        sllist[1] = anlist[0]
        for c in anlist:
            if c not in sllist:
                sllist[0] = c
                break

    if len(anlist) >= 2:
        for c in anlist[2:len(anlist)]:
            if c not in sllist:
                sllist.append(c)

    source_language = ''.join(sllist)


    number = transform(alien_number, source_language, target_language)

    print "Case #" + str(n + 1) + ":", number
    output_file.write("Case #" + str(n + 1) + ": " + number + "\n")

input_file.close()
output_file.close()
