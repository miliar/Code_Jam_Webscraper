def count_friend():
    people = input().split(' ')[1]
    friend = 0
    unshy_people = int(people[0])
    shyness = 1
    people = people[1:]
    while (people):
        while (people and unshy_people < shyness):
            friend += 1
            unshy_people += 1
        unshy_people += int(people[0])
        shyness += 1
        people = people[1:]
    return friend

loop = int(input())

for i in range(loop):
    print("Case #" + str(i+1) + ": " + str(count_friend()))
