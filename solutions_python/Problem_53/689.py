#!/usr/bin/env python
'''
Created on 08 Mei 2010

@author: firman
'''
hexDict = {
    '0':'0000', '1':'0001', '2':'0010', '3':'0011', '4':'0100', '5':'0101',
    '6':'0110', '7':'0111', '8':'1000', '9':'1001', 'a':'1010', 'b':'1011',
    'c':'1100', 'd':'1101', 'e':'1110', 'f':'1111', 'L':''}
def dec2bin(n):

    return ''.join([hexDict[hstr] for hstr in hex(n)[2:]])
if __name__ == '__main__':
    
    
    f = open("./A-large.in","r")
    fout = open("./A-large.out", "w")
    T = int(f.readline());
    
    for i in range(1,T+1) :
        line = f.readline().split(" ")
        bin = dec2bin(int(line[1]))[-int(line[0]):]
        
        end = '1'
        
        if (len(bin)<int(line[0] )) : end = "0"
           
        else :
            for b in bin :
                if b == '0' :
                    end = '0' 
                    break 
            
        fout.write("Case #%s: %s\n"% (i,"ON" if (end == '1') else "OFF"))


    fout.close
    
    pass

