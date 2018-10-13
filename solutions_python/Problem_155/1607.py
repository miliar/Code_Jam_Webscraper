var = raw_input("Enter something: ").split('\n')
text = ""

caseno = 0
for line in var[1:]:
    if line != "":
        caseno += 1
        addpeople = 0
        (maxshy, situ) = line.split(" ")
        #print situ
        maxshy = int(float(maxshy))
        stand = 0
        addall = 0
        for j in range(0,maxshy+1):
            #print("j " + str(j))
            addnow = 0
            if stand < j:
                addnow = (j-stand)
                #print addnow
            stand += (addnow + (int(float(situ[j]))))
            addall += addnow
        newline = "Case #" + str(caseno) + ": " + str(addall)
        text += "%s\n" % newline
print text
