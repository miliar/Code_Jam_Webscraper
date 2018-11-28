src1 = "ejp mysljylc kd kxveddknmc re jsicpdrysi rbcpc ypc rtcsra dkh wyfrepkym veddknkmkrkcd de kr kd eoya kw aej tysr re ujdr lkgc jvzq"

src2 = "our language is impossible to understand there are twenty six factorial possibilities so it is okay if you want to just give upqz"

table={}
f=open('pa.out', 'w')
i=open('A-small-attempt2.in','r')
for char in range(len(src1)):
    table [src1[char]]=src2[char]

times = i.readline()
for t in range(int(times)):
    input1 = i.readline()
    f.write ("Case #" + str(t+1) + ": "),
    print ("Case #" + str(t+1) + ": "),
    output =""
    for char in range(len(input1)):
         if(input1[char]=='\n'):
             output += '\n'
         else: 
             output += table[input1[char]]
    f.write(output)
    print (output)

