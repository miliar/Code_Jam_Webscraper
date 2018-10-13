infile = open('A-large.in','r')
outfile = open('output.txt', 'w')

T = int(infile.readline().strip())
out = ""
for tc in range(T):
    out += "Case #"+str(tc+1)+": "
    
    #solution here
    shystring = infile.readline().strip().split()[1]
    count = 0
    added = 0
    shyness = 0
    for num in shystring:
        num = int(num)
        if num > 0 and shyness > count:
            added += shyness-count
            count = shyness
            print(tc+1,shyness, count, added, num)
        count += num
        shyness += 1
    out += str(added)+"\n"
    
print(out)
outfile.write(out)
    
outfile.close()
infile.close()