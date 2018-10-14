#!/usr/bin/env python
from __future__ import print_function, division

import sys

infile = open(sys.argv[1])
outfiles = (sys.stdout, open(sys.argv[2], 'w'))

winningCombo=['XXXX','XXXT','XXTX', 'XTXX','TXXX','OOOO', 'OOOT','OOTO','OTOO','TOOO']
winX='X won'
winO='O won'
draw='Draw'
incomplete='Game has not completed'

def read_in(infile):
    numLinesIsVariable=False # <<<<<< set this!
    numLinesInEntry=5 # <<<<<< set this!
    data = infile.readline()
    #print ('data0:',data)
    amount = int(data)
    content=[]
    for i in xrange(0,amount):
        if numLinesIsVariable:
            numLinesInEntry=int(infile.readline())
        for j in xrange(0,numLinesInEntry):
            content.append(infile.readline())
        yield content
        content=[]

def do_output(number, output, outfiles):
    for f in outfiles:
        print('Case #%d:' % number, output, file=f)

def main():
    for i, content in enumerate(read_in(infile)):
        do_output(i+1, do_task(content), outfiles)

def chkRes(data):
    #print('chk',data, 'in winningCombo')

    if data in winningCombo and 'X' in data: 
        return winX
    elif data in winningCombo and 'O' in data: 
        return winO
    return ''

def do_task(content):
    # Parse input string
    res=''
    #for i in content:
        #print(i)
    row1=content[0].strip()
    #print('row1',row1)
    res=chkRes(row1)
    #print('row1res:',res)
    if res!='': return res

    row2=content[1].strip()
    #print('row2',row2)
    res=chkRes(row2)
    #print('row2res:',res)
    if res!='': return res

    row3=content[2].strip()
    #print('row3',row3)
    res=chkRes(row3)
    #print('row3res:',res)
    if res!='': return res

    row4=content[3].strip()
    #print('row4',row4)
    res=chkRes(row4)
    #print('row4res:',res)
    if res!='': return res

    ##print('row1',row1)
    ##print('row2',row2)
    #print('row3',row3)
    #print('row4',row4)

    col1=row1[0]+row2[0]+row3[0]+row4[0]
    #print('col1',col1)
    res=chkRes(col1)
    #print('col1res:',res)
    if res!='': return res

    col2=row1[1]+row2[1]+row3[1]+row4[1]
    #print('col2',col2)
    res=chkRes(col2)
    #print('col2res:',res)
    if res!='': return res

    col3=row1[2]+row2[2]+row3[2]+row4[2]
    #print('col3',col3)
    res=chkRes(col3)
    #print('col3res:',res)
    if res!='': return res

    col4=row1[3]+row2[3]+row3[3]+row4[3]
    #print('col4',col4)
    res=chkRes(col4)
    #print('col4res:',res)
    if res!='': return res

    dia1=row1[0]+row2[1]+row3[2]+row4[3]
    #print('dia1',dia1)
    res=chkRes(dia1)
    #print('dia1res:',res)
    if res!='': 
        ##print('have result!')
        return res

    dia2=row1[3]+row2[2]+row3[1]+row4[0]
    #print('dia2',dia2)
    res=chkRes(dia2)
    #print('dia2res:',res)
    if res!='': return res

    if '.' in row1 \
            or '.' in row2 \
            or '.' in row3 \
            or '.' in row4 \
            or '.' in col1 \
            or '.' in col2 \
            or '.' in col3 \
            or '.' in col4 \
            or '.' in dia1 \
            or '.' in dia2 \
            : return incomplete

    return draw

main()
