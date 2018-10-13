import sys
mapping={
'11':'1',
'1i':'i',
'1j':'j',
'1k':'k',
'i1':'i',
'ii':'-1',
'ij':'k',
'ik':'-j',
'j1':'j',
'ji':'-k',
'jj':'-1',
'jk':'i',
'k1':'k',
'ki':'j',
'kj':'-i',
'kk':'-1',
}

def search(character, input, total='1'):
    for pos,elem in enumerate(input):
        if '-' in total:
            total = "-" + mapping[total[1:]+elem]
            if "--" in total:
                total=total.lstrip("--")
        else:
            total = mapping[total+elem]
            
        if total == character:
            return 1,input[pos+1:]
    return 0,input



def split3(instr, initial='1'):
    while(1):
        ret = search('k', instr, initial)
        #print "split3: ", ret
        if ret[0]==0:
            return "NO"
        if ret[1]=='':
            return "YES"
        instr = ret[1]
        initial='k'
    
def split2(instr, initial='1'):
    while(1):
        ret = search('j', instr, initial)
        #print "split2 :", ret
        if ret[1]=='' or ret[0]==0:
            return "NO"

        ret_k = split3(ret[1], '1')
        if ret_k=='YES' or ret_k=="NO":
            return ret_k
        instr = ret[1]
        initial='j'
    
def split1(instr, initial='1'):
    while(1):
        ret = search('i', instr, initial)
        #print "split1: ", ret
        if ret[0]==0 or ret[1]=='':
            return "NO"
        if ret[0]==1 :
            ret_j=split2(ret[1], '1')
            if ret_j=="YES":
                return ret_j
        instr=ret[1]
        initial = 'i'



def test_case(input):
    return split1(input, '1')
    

if __name__=="__main__":
    fread=open(sys.argv[1],'r')
    total_case=fread.readline().strip()
    for case in range(int(total_case)):
        l,x=fread.readline().strip().split(" ")
        #print l, x
        line=fread.readline().strip()
        #print line
        print "Case #{0}: {1}".format(case+1, test_case(line*int(x)) )
