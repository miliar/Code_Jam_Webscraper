import re,sys,operator as op

#'welcome to code jam'
teststr='welcome to code jam' #19 chars (incl. space ie. ' ')
uniqarr=list(set([i for i in teststr])) #11 unique chars
modnum=10000
posns={}

def getpos(line):
    global posns
    posns={}
    for letter in uniqarr:
        posns[letter]=[]

    for idx in range(len(line)):
        if(line[idx]in posns.keys()) : posns[line[idx]].append(idx)

def count():
    '''back 'tricking' ;) '''
    for elem in posns.values():
        if(len(elem)==0):return '0000'
    prev_counts=[]
    initarr_len=len(posns[teststr[-1]])
    for x in range(initarr_len): prev_counts.append(1)
    
    curr_counts=[]
    for i in range(1,len(teststr)):
        #print  prev_counts
        idx=-1*(i+1)
        temp1=posns[teststr[idx]]
        temp2=posns[teststr[idx+1]]
        startidx=0
        
        while(startidx<len(temp2) and temp1[0]>temp2[startidx]):startidx+=1
        curr_counts.append(sum(prev_counts[startidx:])%modnum)
        cumsum=curr_counts[0]
        for p in temp1[1:]:
            while(startidx<len(temp2) and p>temp2[startidx] ):
                cumsum = (cumsum -prev_counts[startidx])%modnum
                startidx+=1
            if(startidx>=len(temp2)):curr_counts.append(0)
            else:curr_counts.append(cumsum)
        prev_counts=curr_counts
        curr_counts=[]
        
    return str(sum(prev_counts)%modnum).zfill(4)

def process_data(filename,fout):
    f=open(filename)
    fw=open(fout,'w')
    lineno=0
    cases=0
    startline=0
    endline=0
    curr_case=0
    for line in f:
        line=line.strip('\n')
        lineno+=1
        if(lineno==1):
            cases=int(line.strip())
            startline=lineno+1
            endline=lineno+cases
            continue
        if(lineno>=startline and lineno<=endline):
           curr_case+=1
           print curr_case
           getpos(line)
           fw.write(('Case #%d: %s\n')%(curr_case,count()))
           fw.flush()
    f.close()
    fw.close()
    
