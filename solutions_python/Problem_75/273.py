incoming=open('B-large.in','r')
a=int(incoming.readline())
f=open('largeattempt0output.txt','w')
for i in range(1,a+1):
    
    x=incoming.readline().split()
    
    NumberofCombine=int(x[0])
    StoreCombine=x[1:1+NumberofCombine]
    
    NumberofOppose= int(x[1+NumberofCombine])
    StoreOppose= x[NumberofCombine+2:NumberofCombine+2+NumberofOppose]

    Inputsequence=x[-1]

    Result=''
    
    for element in Inputsequence:  # element : input one char and see what happens
       if Result != '':
           Result+=element
           TestMagic = Result[-2:]         # test last two
           MagicTest = TestMagic[::-1]     # reversed
       
           for Magics in StoreCombine:
               if TestMagic in Magics[:2] or MagicTest in Magics[:2]:
                   Result=Result[:-2]+Magics[2]
                   break
           else:
               for Opposes in StoreOppose:
                   if element == Opposes[0]:
                           if Opposes[1] in Result:
                               Result=''
                               break
                   if element == Opposes[1]:
                           if Opposes[0] in Result:
                               Result=''
                               break         
       else:
            Result+=element
    f.write("Case #"+str(i)+": [")
    if Result != '':
        f.write(Result[0])
    for remaining in Result[1:]:
        f.write(', '+remaining)
    f.write(']\n')
f.close()
incoming.close()
