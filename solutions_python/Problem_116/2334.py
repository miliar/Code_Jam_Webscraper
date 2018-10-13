import math
import re

file_name='A-large.in'

X_win_pattern = ['[X|T][X|T][X|T][X|T]\D\D\D\D\D\D\D\D\D\D\D\D',
                 '\D\D\D\D[X|T][X|T][X|T][X|T]\D\D\D\D\D\D\D\D',
                 '\D\D\D\D\D\D\D\D[X|T][X|T][X|T][X|T]\D\D\D\D',
                 '\D\D\D\D\D\D\D\D\D\D\D\D[X|T][X|T][X|T][X|T]',
                 '[X|T]\D\D\D[X|T]\D\D\D[X|T]\D\D\D[X|T]\D\D\D',
                 '\D[X|T]\D\D\D[X|T]\D\D\D[X|T]\D\D\D[X|T]\D\D',
                 '\D\D[X|T]\D\D\D[X|T]\D\D\D[X|T]\D\D\D[X|T]\D',
                 '\D\D\D[X|T]\D\D\D[X|T]\D\D\D[X|T]\D\D\D[X|T]',
                 '\D\D\D[X|T]\D\D[X|T]\D\D[X|T]\D\D[X|T]\D\D\D',
                 '[X|T]\D\D\D\D[X|T]\D\D\D\D[X|T]\D\D\D\D[X|T]']

O_win_pattern = ['[O|T][O|T][O|T][O|T]\D\D\D\D\D\D\D\D\D\D\D\D',
                 '\D\D\D\D[O|T][O|T][O|T][O|T]\D\D\D\D\D\D\D\D',
                 '\D\D\D\D\D\D\D\D[O|T][O|T][O|T][O|T]\D\D\D\D',
                 '\D\D\D\D\D\D\D\D\D\D\D\D[O|T][O|T][O|T][O|T]',
                 '[O|T]\D\D\D[O|T]\D\D\D[O|T]\D\D\D[O|T]\D\D\D',
                 '\D[O|T]\D\D\D[O|T]\D\D\D[O|T]\D\D\D[O|T]\D\D',
                 '\D\D[O|T]\D\D\D[O|T]\D\D\D[O|T]\D\D\D[O|T]\D',
                 '\D\D\D[O|T]\D\D\D[O|T]\D\D\D[O|T]\D\D\D[O|T]',
                 '\D\D\D[O|T]\D\D[O|T]\D\D[O|T]\D\D[O|T]\D\D\D',
                 '[O|T]\D\D\D\D[O|T]\D\D\D\D[O|T]\D\D\D\D[O|T]']

infile = file(file_name,'r')
no_of_test = infile.readline().strip()
result = ''


print 'I am thinking...'

def win_pattern(game_s, lst):
    for e in lst:
        if re.match(e, game_s):
            return True
    return False


for i in range(1,int(no_of_test)+1):
    game = ''

    for j in range(0,4):
        game = game + infile.readline().strip()
    print game

    if win_pattern(game, X_win_pattern):
        result = result +  'Case #'+str(i)+': X won\n'
    elif win_pattern(game, O_win_pattern):
        result = result +  'Case #'+str(i)+': O won\n'
    elif game.find('.')>=0:
        result = result +  'Case #'+str(i)+': Game has not completed\n'
    else:
        result = result +  'Case #'+str(i)+': Draw\n'

    infile.readline()

infile.close()

print 'Write to file now...'

outfile = file(file_name[:file_name.find('.')]+'.out', 'w')
outfile.write(result)
outfile.close()

print 'Write to file is done.'



            
    
