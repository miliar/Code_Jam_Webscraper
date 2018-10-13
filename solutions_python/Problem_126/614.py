##Consonants
##Michael Feliciano
#College of Charleston
# Small solution


files = ["A-small-attempt0.in","A-large.in"]
content = file(files[0])

cases = int(content.readline())

filename = "output.txt"
File = open(filename,'w')

vowels = ['a','e','i','o','u']

for i in range(cases):
    solution = 0
    count = 0
    word,nVal = map(str,content.readline().split())
    
    for j in range(len(word)):
        count = 0
        current = word[j::]

        for k in range(j,len(current)+j+1):
            substring = word[j:k]
            count = 0
            for l in range(len(substring)):
                if(substring[l] in vowels):
                    count = 0
                else:
                    count+=1
                    if(count >= int(nVal)):
                        solution+=1
                        break

    File.write("Case #%d: %s" % (i+1,solution ) + "\n")
    
File.close()

