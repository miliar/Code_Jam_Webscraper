# input = open("small.in")
# output = open("small.out", "w")
# input = open("A-small-attempt1.in")
# output = open("A-small-practice.out", "w")
input = open("A-large.in")
output = open("A-large.out", "w")

number_of_cases = int(input.readline())

for case in range(1, number_of_cases+1):
    max_level, string = input.readline().strip().split(" ")
    list_of_people = list(map(int, list(str(string))))

    number_of_friends = 0
    number_of_standup_people = 0

    for index, i in enumerate(list_of_people):
        new_friends = 0
        if (index > number_of_standup_people and i != 0):
            new_friends = index - number_of_standup_people
            number_of_friends += new_friends
        number_of_standup_people += i + new_friends

    print("Case #{}: {}".format(case, number_of_friends), file=output)
