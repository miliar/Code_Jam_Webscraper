f=open("A-large.in","r")
lists=f.readlines()
tests=int(lists[0])
i=1
while i<=tests:
    line=lists[i].rstrip('\n').split(" ")
    j=0
    total = 0
    required = 0
    people = list(line[1])
    line[0] = int(line[0])
    while j<=line[0]:
        if total < j:
            required = required + j - total
            total = j
        total = total + int(people[j])
        j=j+1
    print "Case #%d: %d" %(i,required)
    i=i+1

