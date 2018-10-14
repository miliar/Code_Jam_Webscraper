import collections

def main():
    fileName = 'A-large.in'
    fl = open(fileName)
    wfName = 'res' + fileName
    wf = open(wfName, 'w')
    f = fl.readline()
    f = int(f)
    res = []
    for i in range(f):
        print str(i) + 'th Test case' 
        st = []
        mat1 = []
        incomp = False
        for j in range(4) :
            line = fl.readline().rstrip()
            if '.' in line :
                incomp = True
            mat1.append(line)
        fmat = []
        mat = map(list, zip(*mat1))
        fmat = mat1 + mat
        ls = []
        ls1 = []
        for i in range(4) :
            ls.append(mat1[i][i])
            ls1.append(mat1[i][3-i])
        fmat.append(ls)
        fmat.append(ls1)
        resFound = False
        x = 0
        o = 0
        for line in fmat :
            line = ''.join(line)
            cl = collections.Counter(line)
            print cl
            if cl['X'] + cl['T'] == 4 :
                x = x + 1
                res.append('X won')
                resFound = True
                break
            elif cl['O'] + cl['T'] == 4 :
                o = o + 1
                res.append('O won')
                resFound = True
                break
        if not resFound :
            if incomp :
                res.append('Game has not completed')
            else :
                res.append('Draw')
        bl = fl.readline()
    i = 0
    for lin in res :
      print lin
      wf.write('Case  #' + str(i+1)+': ' + res[i]+ '\n' )
      i = i + 1
    wf.close()
      
    
                
if __name__ == "__main__" :
    main()