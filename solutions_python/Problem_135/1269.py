infile=open('A-small-attempt1.in','r')
lines=infile.readlines()
infile.close()
outfile=open('ans1.txt','w')
test=int(lines[0])
for i in range(test):
    text = "Case #" + str(i+1) + ": "
    cases = lines[1+10*i:11+10*i]
    ans = (set(cases[int(cases[0])].strip().split(' ')) & set(cases[int(cases[5])+5].strip().split(' ')))
    
    outfile.write(text)
    if len(ans) == 1:
        outfile.write(str(list(ans)[0]))
    elif len(ans) == 0:
        outfile.write("Volunteer cheated!")
    else:
        outfile.write("Bad magician!")
    outfile.write("\n")
outfile.close()

print("done")
