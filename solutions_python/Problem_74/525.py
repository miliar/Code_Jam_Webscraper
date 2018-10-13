


def parse(text):
    blue = []
    orange = []
    seq = []
    items = text.replace(',','').split()
    for i in xrange(len(items)/2):
        if items[i*2] == 'O':
            seq += 'O'
            orange.append(int(items[i*2+1]))
        elif items[i*2] == 'B':
            seq += 'B'
            blue.append(int(items[i*2+1]))
    return blue, orange, seq

def move(blue, orange, seq):
    orange_pos = blue_pos = 1
    seconds = 0
    lock = False
    while 1:
        seconds += 1
        #print seconds

        if orange:
            #print orange_pos, orange[0]
            if not orange_pos == orange[0]:
                orange_pos += (orange[0] > orange_pos) or -1
                #print "orange moved to button %s" %orange_pos
            else:
                if not lock and seq[0] == 'O':
                    lock = True
                    del orange[0]
                    del seq[0]
                    #print "Orange pushed button %s" %orange_pos
                else:
                    pass
                    #print "Orange stayed at button %s" %orange_pos

        if blue:
            #print blue_pos, blue[0]
            if not blue_pos == blue[0]:
                blue_pos += (blue[0] > blue_pos) or -1
                #print "Blue moved to button %s" %blue_pos
            else:
                if not lock and seq[0] == 'B':
                    lock = True
                    del blue[0]
                    del seq[0]
                    #print "blue pushed button %s" %blue_pos
                else:
                    pass
                    #print "blue stayed at button %s" %blue_pos

        if not blue and not orange:
            return seconds

        lock = False
    return seconds

#print parse("O 2, B 1, B 2, O 4")
#move(*parse("B 2 B 1"))

file = open('A-small-attempt0.in', 'rb')
outfile = open('A-small-attempt0.out', 'wb')
items = file.readline()
for index, line in enumerate(file.readlines()):
    towrite = "Case #%s: %s\n" %( index+1, move(*parse(line[2:])))
    outfile.write(towrite)