test_cases = int(raw_input())

for t  in range(test_cases):
    max_, audience = raw_input().split()
    currPeople = 0
    neededPeople = 0
    for i in range(int(max_) + 1):
        if currPeople < i:
            neededPeople += i-currPeople
            currPeople += i-currPeople
        currPeople += int(audience[i])
    print "Case #" + str(t+1) + ": " + str(neededPeople)
