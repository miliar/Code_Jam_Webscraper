text_file = open("A-small-attempt2.in", "r")
count = 1
numcases = int(text_file.readline())
f = open('output.txt','w')
for count in range (1, numcases+1):
    str = text_file.readline()
    translation = ""
    for letter in str:
        if letter == ' ':
		    translation = translation + ' '
        elif letter == 'a':
            translation = translation + 'y'
        elif letter == 'b':
            translation = translation + 'h'
        elif letter == 'c':
		    translation = translation + 'e'
        elif letter == 'd':
            translation = translation + 's'
        elif letter == 'e':
            translation = translation + 'o'
        elif letter == 'f':
		    translation = translation + 'c'
        elif letter == 'g':
            translation = translation + 'v'
        elif letter == 'h':
            translation = translation + 'x'
        elif letter == 'i':
		    translation = translation + 'd'
        elif letter == 'j':
            translation = translation + 'u'
        elif letter == 'k':
            translation = translation + 'i'
        elif letter == 'l':
		    translation = translation + 'g'
        elif letter == 'm':
            translation = translation + 'l'
        elif letter == 'n':
            translation = translation + 'b'
        elif letter == 'o':
		    translation = translation + 'k'
        elif letter == 'p':
            translation = translation + 'r'
        elif letter == 'q':
            translation = translation + 'z'
        elif letter == 'r':
		    translation = translation + 't'
        elif letter == 's':
            translation = translation + 'n'
        elif letter == 't':
            translation = translation + 'w'
        elif letter == 'u':
		    translation = translation + 'j'
        elif letter == 'v':
            translation = translation + 'p'
        elif letter == 'w':
            translation = translation + 'f'
        elif letter == 'x':
		    translation = translation + 'm'
        elif letter == 'y':
            translation = translation + 'a'
        elif letter == 'z':
            translation = translation + 'q'			
    print >>f, "Case #%d:" % count, translation
    count = count + 1
text_file.close()
