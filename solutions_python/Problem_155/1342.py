def nbFriends(shyness):
    friends = 0
    nbUp = 0
    for shynessLevel, nbPersons in enumerate(shyness):
        if nbUp >= shynessLevel:
            nbUp += nbPersons
        else:
            friends += shynessLevel - nbUp
            nbUp = shynessLevel + nbPersons
    return friends

T = int(input(""))
for testCase in range(T):
    Smax, shyness = input("").split()
    Smax = int(Smax)
    shyness = [int(x) for x in shyness]
    print("Case #%d: %d" % (testCase+1, nbFriends(shyness)))
