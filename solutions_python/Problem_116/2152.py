'''
Created on Apr 13, 2013

@author: vimuthfernando
'''

f = open("A-large.in",'r')
fout = open("output.txt",'w')
cases = int(f.readline())

def getColumns(lines):
    return [lines[0][i]+lines[1][i]+lines[2][i]+lines[3][i] for i in xrange(4)]

def getDiags(lines):
    return [''.join([lines[i][i] for i in xrange(4)]),''.join([lines[i][3-i] for i in xrange(4)])]


for i in xrange(cases):
    inputs = [f.readline()[:-1] for j in xrange(4)]
    lines = inputs+ getColumns(inputs)+getDiags(inputs)
    
    if 'XXXX' in lines or 'XXXT' in lines or 'TXXX' in lines or 'XTXX' in lines or 'XXTX' in lines:
        fout.write('Case #%d: X won\n' % int(i+1))
    elif 'OOOO' in lines or 'OOOT' in lines or 'TOOO' in lines or 'OTOO' in lines or 'OOTO' in lines:
        fout.write('Case #%d: O won\n' % int(i+1))
    elif '.' in ''.join(lines):
        fout.write('Case #%d: Game has not completed\n' % int(i+1))
    else :
        fout.write('Case #%d: Draw\n' % int(i+1))
    
    f.readline()
    
fout.close()