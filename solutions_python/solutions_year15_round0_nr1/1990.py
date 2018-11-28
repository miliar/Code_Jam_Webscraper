__author__ = 'gianlucatursi'


with open("q1_large.txt") as f:
    content = f.readlines()

testcase = content[0]
content = content[1:]
usecase = 1

for line in content:
    smax = line[0:line.find(" ")]
    audience = line[line.find(" ")+1:]
    counter = 0
    friends = 0
    for case in range(0,int(smax)+1, 1):
        counter = counter + int(audience[case])

        if counter <= 0:
            friends += 1
        else:
            counter = counter -1

    print "Case #" + str(usecase) + ": " + str(friends)
    usecase  += 1