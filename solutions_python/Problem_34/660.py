import os,itertools,re

indir="input"
inputs=os.listdir(indir)
outdir="output"


    
def parse_input(file):
    F=open(file)
    lines=F.readlines()

    (L,D,N)=itertools.imap(int,lines[0].strip().split(None))
    speclines=lines[1:D+1]
    cases=lines[D+1:][0:N]
    specs=[]
    for specline in speclines:
        specs.append(parse_spec(specline))
    
    return (L,D,N,specs,cases)

def parse_spec(spec):
    spec=spec.strip('\n')
    chars=list(spec)
    return chars

    


def parse_case(case):
    exp="\([a-z]+\)|[a-z]"
    p = re.compile(exp)
    matches=re.findall(p,case)
    caseList=[]
    Tree={}
    for match in matches:
        letterlist=list(match.lstrip("(").rstrip(")"))
        caseList.append(letterlist)

    return caseList


def test_case(caseList,specs,L):
    T=0
    for spec in specs:
        fail=False
        for i in range(L):
            if spec[i] not in caseList[i]:
                fail=True
                break
        if fail==False:
            T+=1
    return T

for input in inputs:
    (L,D,N,specs,cases)=parse_input(indir+"/"+input)
    output=input.replace(".in",".out")
    OF=open(output,'w')
    for C in range(N):
        caseList=parse_case(cases[C])
        count=test_case(caseList,specs,L)
        outline="Case #%d: %d"%(C+1,count)
        print outline
        OF.write(outline+'\n')
    OF.close()
    

