import sys

def convert(strlist):
    return [int(x) for x in strlist]

def ovation(ine, num):
    maxShyness, audience = ine.split(" ")

    audience = convert(audience)
    #print maxShyness, audience

    invitees = 0
    totalClapping = 0
    index = 0

    for personCount in audience:
        if index == maxShyness:
            break # we're at the end
        #print "index", index, "totalClapping", totalClapping, "people", personCount
        if totalClapping + personCount <= index:
            invitees += 1
            totalClapping += 1

        totalClapping += personCount
        #print "total:", totalClapping, "invitees:",invitees, "personCount", personCount
        index+=1
    
    return "Case #" + str(num) + ": " + str(invitees)

def correct(ine, out, num):
    result = ovation(ine, num)
    print result, "expected:", out

    return result == out

def main():
    data = sys.stdin.readlines()
    #data = test.split('\n')
    count = int(data[0].strip())
    i = 1
    for line in data[1:]:
        #print line.strip(), ovation(line.strip(),i).split(":")[1]
        print ovation(line.strip(),i)
        i+=1

main()
