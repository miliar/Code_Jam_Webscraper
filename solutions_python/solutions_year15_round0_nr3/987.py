
## NEED TO SUBMIT

file = open('C:/Users/ja13/Desktop/cj2015Files/C-small-attempt0.in','r')
filew = open('C:/Users/ja13/Desktop/cj2015Files/C-small-0-out.txt','w+')

numCases = int(file.readline())
dict = {'ii':'-1','ij':'k','ik':'-j'
            ,'ji':'-k','jj':'-1','jk':'i'
            ,'ki':'j','kj':'-i','kk':'-1'}
for casenum in range(1,numCases+1):
    line = file.readline().replace('\n','')
    val = file.readline().replace('\n','')
    answer = ''
    numberofAlphs = int(line.split()[0])
    multiplier = int(line.split()[1])
    if numberofAlphs < 2:
        answer = 'NO'
    elif numberofAlphs*multiplier < 3:
        answer = 'NO'
    else:
        val = val * multiplier
        reqAlph = 'i'
        if val == 'ijkd932749':
            answer = 'YES'
        else:
            minus = 0
            subres =''
            while val != 'ijk' and len(val)!=0:
                if val[0] == reqAlph and reqAlph!='k':
                    subres=subres + reqAlph
                    val = val[1:]
                    if reqAlph == 'i':
                        reqAlph ='j'
                    elif reqAlph=='j':
                        reqAlph ='k'
                    
                    continue
                elif len(val)==1:
                    val = val
                    break
                else:
                    res = dict.get(val[0]+val[1])
                    if '-' in res:
                        minus = minus + 1
                    res = res.replace('-','')
                    if res =='1':
                        res=''
                    if res == reqAlph and reqAlph!='k':
                        subres = subres + res
                        val = res + val[2:]
                        val = val[1:]
                        if reqAlph == 'i':
                            reqAlph ='j'
                        elif reqAlph=='j':
                            reqAlph ='k'
                    else:
                        val = res + val[2:]
            val = subres + val
            if minus%2 !=0:
                val = '-'+val
            if val == 'ijk':
                answer = 'YES'
            else:
                answer = 'NO'
    filew.writelines('Case #'+str(casenum)+': '+ str(answer)+'\n')
    print('Case #'+str(casenum)+': '+ str(answer)+'\n')

file.close()
filew.flush()
filew.close()