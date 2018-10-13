#--- Config Path -------------------------------------
INPUT_PATH='a.in'
OUTPUT_PATH='o.out'
#-----------------------------------------------------
''' Input from File code exists here '''
filereader=open(INPUT_PATH,'r')
def readdata():
    tmpstr=filereader.readline()
    data=tmpstr.split('\n')[0]
    return data
def rbyspace():
    tmpstr=readdata()
    data=tmpstr.split(' ')
    return data
def readerclose():
    filereader.close()

#-----------------------------------------------------
''' output '''
fout=open(OUTPUT_PATH,'w')
    
    
#-----------------------------------------------------
''' Logic starts here '''
testcase=int(rbyspace()[0])
for i in range(0,testcase):
    spsq=rbyspace()
    shyness=int(spsq[0])
    sq=list()
    

   
    for itm in str(spsq[1]):
        sq.append(int(itm))
    
    alreadystand=0
    needed=0
    for c in range(0,len(sq)):
        if(c==0):
            alreadystand=alreadystand+sq[c]
        else:
            if(alreadystand>=c):
                alreadystand=alreadystand+sq[c]
            elif(alreadystand<c and sq[c]!=0):
                needed=needed+c-alreadystand
                alreadystand=alreadystand+sq[c]+needed
   # print(needed)

    fout.write("Case #"+str(i+1)+": "+str(needed)+"\n")
fout.close()
readerclose()
        
    
   

    


''' Logic ends Here '''
#------------------------------------------------------    

