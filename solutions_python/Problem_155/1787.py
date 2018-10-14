import sys
# Fundamentally, the problem is about a cumulative sum. If the sum of all elements lower than the current one is less than the current shyness, we need to add chosen friends to make it match up.

def main():
    with sys.stdin as f:
        tests = int(f.readline())
        for case in range(tests):
            audience = f.readline().strip().split(' ')
#            print audience
            shynesses = audience[1]
            shy = []
            for people in shynesses:
                shy.append(int(people))
            print "Case #%d: %d" % (case + 1, neededFriends(shy))

def neededFriends(shynesses):
    # Takes a set of people at shyness levels and determines how many friends.
    # Accepts: A list of integers representing a mapping of shyness levels to people.
    # Returns; An integer representing the number of friends needed.
#    print shynesses
    total = 0
    friends = 0
    for shyness in range(len(shynesses)):
        if total < shyness:
            # If the next group of people aren't going to stand up, we need to add friends to make them.
            added = shyness - total
            friends += added
            total += added

        total += shynesses[shyness]
    return friends

if __name__ == "__main__":
    main()
