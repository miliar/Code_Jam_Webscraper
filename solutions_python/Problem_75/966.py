'''
Created on 2011-05-07

@author: jason
'''

def runsim(line):
    words = line.split(" ")
    combonum = int(words[0])
    combos = words[1:1+combonum]
    badnum = int(words[1+combonum])
    bads = words[2+combonum:2+combonum+badnum]
    
    spell = words[-1]
    
    newcombos = []
    for comb in combos:
        newcombos.append((comb[0],comb[1],comb[2]))
        newcombos.append((comb[1],comb[0],comb[2]))
    
    newbads = []
    for bad in bads:
        newbads.append((bad[0],bad[1]))
        newbads.append((bad[1],bad[0]))
    
    letarr = []
    for letter in spell:
        if len(letarr) == 0:
            letarr.append(letter)
            continue
        found = False
        for comb in newcombos:
            if letarr[-1] == comb[0] and letter == comb[1]:
                letarr = letarr[:-1]
                letarr.append(comb[2])
                found = True
                break
        if not found:
            for bad in newbads:
                if letter == bad[0] and letarr.count(bad[1]) > 0:
                    letarr = []
                    found = True
                    break
        if not found:
            letarr.append(letter)
    
    return letarr

def main():
    fi = open("B-large.in", "r")
    fo = open("output", "w")
    
    lines = []
    
    for line in fi:
        lines.append(line)
    
    linecount = 0
    for line in lines[1:]:
        linecount = linecount + 1
        
        linearr = runsim(line)
        
        #print linecount, len(linearr)
        
        stringret = "Case #" + str(linecount) + ": " + "["
        for item in linearr:
            if item != "\n":
                stringret = stringret + item + ", "
        if len(linearr) > 1:
            stringret = stringret[:-2] + "]"
        else:
            stringret = stringret + "]"
        
        fo.write(stringret + "\n")
        
        
    fi.close()
    fo.close()
    
    

if __name__ == '__main__':
    main()
    
    

    
    