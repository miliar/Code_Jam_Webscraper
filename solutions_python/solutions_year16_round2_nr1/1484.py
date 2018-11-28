import re


def check_for_numbers(unumber, n):
    zero = one = two = three = four = five = six = seven = eight = nine = 0
    string_six = len(re.findall('[SIX]', unumber))/3
    for x in range(0, string_six):
        if 'S' in unumber and 'I' in unumber and 'X' in unumber:
            unumber = unumber.replace('S','',1).replace('I','',1).replace('X','',1)
            six += 1
    string_four = len(re.findall('[FOUR]', unumber))/4
    for x in range(0, string_four):
        if 'F' in unumber and 'O' in unumber and 'U' in unumber and 'R' in unumber:
            unumber = unumber.replace('F','',1).replace('O','',1).replace('U','',1).replace('R','',1)
            four += 1
    string_eight = len(re.findall('[EIGHT]', unumber))/5
    for x in range(0, string_eight):
        if 'E' in unumber and 'I' in unumber and 'G' in unumber and 'H' in unumber and 'T' in unumber:
            unumber = unumber.replace('E','',1).replace('I','',1).replace('G','',1).replace('H','',1).replace('T','',1)
            eight += 1
    string_seven = len(re.findall('[SEVEN]', unumber))/5
    for x in range(0, string_seven):
        if 'S' in unumber and 'E' in unumber and 'V' in unumber and 'N' in unumber:
            unumber = unumber.replace('S','',1).replace('E','',1).replace('V','',1).replace('E','',1).replace('N','',1)
            seven += 1
    string_two = len(re.findall('[TWO]', unumber))/3
    for x in range(0, string_two):
        if 'T' in unumber and 'W' in unumber and 'O' in unumber:
            unumber = unumber.replace('T','',1).replace('W','',1).replace('O','',1)
            two += 1
    string_three = len(re.findall('[THREE]', unumber))/5
    for x in range(0, string_three):
        if 'T' in unumber and 'H' in unumber and 'R' in unumber and 'E' in unumber:
            unumber = unumber.replace('T','',1).replace('H','',1).replace('R','',1).replace('E','',1).replace('E','',1)
            three += 1
    string_five = len(re.findall('[FIVE]', unumber))/4
    for x in range(0, string_five):
        if 'F' in unumber and 'I' in unumber and 'V' in unumber and 'E' in unumber:
            unumber = unumber.replace('F','',1).replace('I','',1).replace('V','',1).replace('E','',1)
            five += 1
    string_zero = len(re.findall('[ZERO]', unumber))/4
    for x in range(0, string_zero):
        if 'Z' in unumber and 'E' in unumber and 'R' in unumber and 'O' in unumber:
            unumber = unumber.replace('Z','',1).replace('E','',1).replace('R','',1).replace('O','',1)
            zero += 1
    string_nine = len(re.findall('[NINE]', unumber))/4
    for x in range(0, string_nine):
        if 'N' in unumber and 'I' in unumber and 'E' in unumber:
            unumber = unumber.replace('N','',1).replace('I','',1).replace('N','',1).replace('E','',1)
            nine += 1
    string_one = len(re.findall('[ONE]', unumber))/3
    for x in range(0, string_one):
        if 'O' in unumber and 'N' in unumber and 'E' in unumber:
            unumber = unumber.replace('O','',1).replace('N','',1).replace('E','',1)
            one += 1
    number = ""
    for i in range(0, zero): number += "0"
    for i in range(0, one): number += "1"
    for i in range(0, two): number += "2"
    for i in range(0, three): number += "3"
    for i in range(0, four): number += "4"
    for i in range(0, five): number += "5"
    for i in range(0, six): number += "6"
    for i in range(0, seven): number += "7"
    for i in range(0, eight): number += "8"
    for i in range(0, nine): number += "9"

    print "Case #%d: %s" % (n, number)


t = int(raw_input().strip())

for x in range(1,t+1):
    n = raw_input().strip()
    check_for_numbers(n, x)
