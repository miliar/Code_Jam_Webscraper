import fileinput

english =    'abcdefghijklmnopqrstuvwxyz '
googlerese = 'ynficwlbkuomxsevzpdrjgthaq '
code = dict(zip(googlerese, english))

def decode(line):
    englishline = ''
    for ch in line:
        englishline += code[ch]
    return englishline
    
def main():
    for line in fileinput.input():
        if fileinput.isfirstline():
            continue
        englishline = decode(line.rstrip())
        print("Case #{}: {}".format(fileinput.lineno()-1, englishline))

if __name__ == '__main__':
    main()
