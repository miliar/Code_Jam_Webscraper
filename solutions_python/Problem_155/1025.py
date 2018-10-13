f = open('Input.txt')
lines = f.readlines()
f.close()


output = open('AOutput.txt','w')

i=0
for line in lines:
    if(i!=0):
        s_max = int(line.split()[0])
        shyness_levels = line.split()[1]
        num_standing = 0
        add_people = 0
        print "S max: ",
        print s_max
        print "shyness lvls: ",
        print shyness_levels
        for j in range(s_max+1):
            print "shyness level ", 
            print j
            print "num standing ", 
            print num_standing          
            if(j<=num_standing):
                num_standing = num_standing + int(shyness_levels[j])
            else:
                if(int(shyness_levels[j]) != 0):
                    add_people += j - num_standing #always add standing people
                    num_standing += add_people + int(shyness_levels[j])
        print "add ppl: ",        
        print add_people
        output.write("Case #")
        output.write(str(i))
        output.write(": ")
        output.write(str(add_people))
        output.write("\n")
    i=i+1

output.close() 