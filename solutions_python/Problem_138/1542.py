file_name = "D-large"
raw_input = open(file_name+".in","r").read().split("\n")
test_cases = int(raw_input[0])
test_length = 3
output = ""

for i in range(test_cases):
    input = raw_input[i*test_length+1:i*test_length+test_length+1]
    N = int(input[0])
    Na_list = sorted([float(x) for x in input[1].split(" ")])
    Kn_list = sorted([float(x) for x in input[2].split(" ")])
    j=N-1
    k=N-1
    d_count=0
    count = 0
    for t in xrange(N):
        if Na_list[j]>Kn_list[N-t-1]:
            count+=1
            j-=1

        if Na_list[N-t-1]<Kn_list[k]:
            d_count+=1
            k-=1
    output+= "Case #%s: %s %s\n" % (i+1,count,N-d_count)
f = open(file_name+".out", "w")
f.write(output)




