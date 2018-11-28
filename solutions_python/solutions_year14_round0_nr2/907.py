
input_file = open('B-large.in','r')
input_data = ''.join(input_file.readlines())
input_file.close()

lines = input_data.split('\n')
no_of_test_cases = int(lines[0])
f=open("out.txt",'w')
for i in range (1,no_of_test_cases+1):
    inp = lines[i].split(' ')
    C,F,X = float(inp[0]),float(inp[1]),float(inp[2])
    prod_rate = 2.0
    opt_time = 0.0
    while (C/prod_rate + X/(prod_rate+F)) < (X/prod_rate):
        opt_time+=C/prod_rate
        prod_rate+=F
    opt_time+=X/prod_rate
    #print "# %.7f"%opt_time
    f.write("Case #%d: %.7f\n"%(i,opt_time))
f.close()


