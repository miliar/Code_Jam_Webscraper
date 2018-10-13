t = int(input())

for i in range(t):
    listy = input()
    running_total = 0
    friends = 0

    smax, people = listy.split(" ")

    for j in range(len(people)):
        if running_total >= j:
            running_total += int(people[j])

        else:
            new_friends = (j - running_total)
            friends += new_friends
            running_total += int(people[j])
            running_total += new_friends


    print("Case #" + str(i + 1) + ":", friends)