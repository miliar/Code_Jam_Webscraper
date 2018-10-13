## Written by Nivvedan S
## Google Codejam


INPUT_FILE_NAME="b.in"
## OUTPUT_FILE_NAME="b.out"
IN = open(INPUT_FILE_NAME, "r")
## OUT = open(OUTPUT_FILE_NAME, "w")

par_input=IN.readlines()

T=int(par_input[0].strip())
par_input=par_input[1:]

elem_list=["Q","W","E","R","A","S","D","F"]

count=0
for line in par_input:
    to_parse=line.strip().split()

    comb={}
    opp={}

    C=int(to_parse[0])
    to_parse=to_parse[1:]
    for i in range(C):
        paired=to_parse[0]
        comb[paired[0:2]]=paired[2]
        comb[paired[1]+paired[0]]=paired[2]
        to_parse=to_parse[1:]

    D=int(to_parse[0])
    to_parse=to_parse[1:]
    for i in range(D):
        enemy=to_parse[0]
        opp[enemy[0]]=enemy[1]
        opp[enemy[1]]=enemy[0]
        to_parse=to_parse[1:]

    no_of_elements=int(to_parse[0])
    to_parse=to_parse[1:]

    elements=[]

    elem_str=to_parse[0]

    while(not (elem_str=="")):
        elements.append(elem_str[0])
        if (len(elements)>1):
            new=comb.get(elements[-2]+elements[-1],0)
            if  not new==0:
                if len(elements)==2:
                    elements=[new]
                else:
                    elements=elements[0:len(elements)-2]
                    elements.append(new)

            new=opp.get(elements[-1],0)
            if not new==0:
                if not elements.count(new)==0:
                    elements=[]
        elem_str=elem_str[1:]
        
    
    count=count+1
    output="Case #"+str(count)+": ["
    for i in elements:
        output=output+i+", "
    if len(elements)==0:
        output=output+"]"
    else:
        output=output[0:len(output)-2]+"]"
    print output
    
