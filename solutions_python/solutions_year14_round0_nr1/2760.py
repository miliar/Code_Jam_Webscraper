def one_values(line):
    if line[len(line)-1]=='\n':
            line=line[:-1]
    
    return float(line)
    
def matrix_values(line):
    row=[]
    if line[len(line)-1]=='\n':
            line=line[:-1]
    line=line.split(' ')
    
    for i in line:
        row.append(float(i))
    
    #print row
    return row
    
def get_result(rowA,rowB):

    result=[]
    for i in rowA:
        if i in rowB:
            result.append(i)
            
    return result

def main():

    input=open(r'C:\Users\Nuria\Desktop\CodeJam\ProblemaA\A-small-attempt0.in','r')
    output=open('C:\Users\Nuria\Desktop\CodeJam\ProblemaA\outputA.txt','w')
    
    line_ = input.readline()
   
    cases = int(line_)
    
    for i in range(cases):
        matrixA=[]
        optionA=int(one_values(input.readline()))
        for j in range(4):
            matrixA.append(matrix_values(input.readline()))
        optionB=int(one_values(input.readline()))
        
        matrixB=[]
        for j in range(4):
            matrixB.append(matrix_values(input.readline()))
        
        #print matrixA , matrixB
        
        #print matrixA[optionA-1]
        #print matrixB[optionB-1]
        
        result=get_result(matrixA[optionA-1],matrixB[optionB-1])
        
        if len(result)==1:
            line='Case #%d: %d\n'%(i+1,result[0])
            #output.write('Case #%d: %d'%(result[0])
            #print 'Ok'
        elif len(result)>1:
            line='Case #%d: Bad magician!\n'%(i+1)
        else:
            line='Case #%d: Volunteer cheated!\n'%(i+1)
        
        output.write(line)
        
        #print 'RESULTAT'
        #print result
        
    input.close()
    output.close()
    

if __name__ == "__main__":
    main()