input_file=open("C:\Users\Lipman\Desktop\input.txt","r")
output_file=open("C:\Users\Lipman\Desktop\output.txt","w")
cases=int(input_file.readline()[:-1])
for i in xrange(cases):
    curr_case=input_file.readline()
    curr_case=curr_case[curr_case.find(" ")+1:-1]
    if len(curr_case)==0:
       output_file.write("Case #{0}: 0\n".format(i+1))
    stands=0
    friends=0
    for shy_level in xrange(len(curr_case)):
        if shy_level>stands:
            friends+=shy_level-stands
            stands+=shy_level-stands
        stands+=int(curr_case[shy_level])
    output_file.write("Case #{0}: {1}\n".format(i+1,friends))
input_file.close()
output_file.close()
