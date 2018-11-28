def howManyFriends(line):
    peopleWhoHaveClapped = 0
    friendsNeeded = 0

    for shyness in range(len(line)):
        if peopleWhoHaveClapped >= shyness:
            peopleWhoHaveClapped = peopleWhoHaveClapped + int(line[shyness])
        else:            
            friendsNeeded = friendsNeeded + ( shyness - peopleWhoHaveClapped )
            peopleWhoHaveClapped = shyness + int(line[shyness])
            #print friendsNeeded
            #print shyness

    return friendsNeeded

def run():
    with open('A-large.in.txt') as f:
        content = f.readlines()
    #print content
    content = content[1:]
    i = 0
    for line in content:
        i = i + 1
        print "Case #" + str(i) + ": " + str(howManyFriends(line.split()[1]))
    
run()
#print howManyFriends( "111111" )
#print howManyFriends( "09" )
#print howManyFriends( "110011" )
#print howManyFriends( "1" )
            
