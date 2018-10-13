def eng_to_goog(goog_string):
    eng_string = ''
    for char in goog_string:
        if char == ' ':
            eng_string += ' '
        elif char == 'a':
            eng_string += 'y'
        elif char == 'b':
            eng_string += 'h'
        elif char == 'c':
            eng_string += 'e'
        elif char == 'd':
            eng_string += 's'
        elif char == 'e':
            eng_string += 'o'
        elif char == 'f':
            eng_string += 'c'
        elif char == 'g':
            eng_string += 'v'
        elif char == 'h':
            eng_string += 'x'
        elif char == 'i':
            eng_string += 'd'
        elif char == 'j':
            eng_string += 'u'
        elif char == 'k':
            eng_string += 'i'
        elif char == 'l':
            eng_string += 'g'
        elif char == 'm':
            eng_string += 'l'
        elif char == 'n':
            eng_string += 'b'
        elif char == 'o':
            eng_string += 'k'
        elif char == 'p':
            eng_string += 'r'
        elif char == 'q':
            eng_string += 'z'
        elif char == 'r':
            eng_string += 't'
        elif char == 's':
            eng_string += 'n'
        elif char == 't':
            eng_string += 'w'
        elif char == 'u':
            eng_string += 'j'
        elif char == 'v':
            eng_string += 'p'
        elif char == 'w':
            eng_string += 'f'
        elif char == 'x':
            eng_string += 'm'
        elif char == 'y':
            eng_string += 'a'
        elif char == 'z':
            eng_string += 'q'

    return eng_string

def main():
    in_dat = open('A-small-attempt0.in', 'r')
    in_lines = in_dat.readlines()[1:]
    i = 1
    for line in in_lines:
        english = eng_to_goog(line)
        print "Case #"+str(i)+": "+english
        i += 1
if __name__ == "__main__":
    main()
