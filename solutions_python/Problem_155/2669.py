import sys

with open("A-large.in.txt") as f:
    content = f.read().splitlines()
T = content[0]
content.remove(T)
T = int(T)
trials = list()
for element in content:
    x = element.split(" ")
    trials.append(x[1])
for t in range(T):
    total_friends_needed = 0
    total_clapping = 0
    element = trials[t]
    for i in range(len(element)):
        if i == 0:
            total_clapping += int(element[0])
        elif i <= (total_clapping + total_friends_needed):
            total_clapping += int(element[i])
        elif int(element[i]) > 0:
            total_friends_needed += i - (total_clapping + total_friends_needed)
            total_clapping += int(element[i])
    print("Case #{}: ".format(t+1) + str(total_friends_needed))