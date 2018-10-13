f = open('A-small-attempt0.in','r')
arr= f.readlines()
f.close()

f=open('A.out','w')
c=int(arr[0])+1
dicti={
'y' : 'a', 
'n' : 'b',
'f' : 'c', 
'i' : 'd',
'c' : 'e',
'w' : 'f',
'l' : 'g',
'b' : 'h',
'k' : 'i',
'u' : 'j',
'o' : 'k',
'm' : 'l',
'x' : 'm',
's' : 'n',
'e' : 'o',
'v' : 'p',
'z' : 'q',
'p' : 'r',
'd' : 's',
'r' : 't',
'j' : 'u',
'g' : 'v',
't' : 'w',
'h' : 'x',
'a' : 'y',
'q' : 'z'
}
for case in range(1,c):
    f.write("Case #"+str(case)+": ")
    for i in range(0,len(arr[case])):        
        if arr[case][i] in dicti:
            f.write(dicti[arr[case][i]])
        else:
            f.write(arr[case][i])    
f.close()    
