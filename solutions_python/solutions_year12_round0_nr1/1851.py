trans = 'yhesocvxduiglbkrztnwjpfmaq'
N = input()
for i in range(N):
    line = raw_input()
    newline = ''
    for c in line:
        newline += trans[ord(c) - ord('a')] if c != ' ' else ' '
    
    print 'Case #%d: %s' % (i+1, newline)
