__author__ = 'Nikola Culumovic'

number_of_cases = int(input())
cases = []
for i in range(number_of_cases):
    case = str(input())
    case = list(case.split()[1])
    audience = int(case[0])
    friends_needed = 0
    if len(case) != 1:
        for shy_level in range(1, len(case)):
            if int(case[shy_level]) != 0:
                if audience < shy_level:
                    friends_needed += (shy_level - audience)
                    audience = shy_level
                audience += int(case[shy_level])
    print("Case #"+str(i+1)+": "+str(friends_needed))