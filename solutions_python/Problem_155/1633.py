import sys

N = int(sys.stdin.readline())
f = open('standing_ovation3.txt', 'w')

for n in range(1, N+1):
    line = sys.stdin.readline()
    numbers = line.split()
    max_shyness = int(numbers[0])
    numbers_string = numbers[1]
    shyness = {}
    num_standing = 0
    total_people = 0
    people_added = 0
    a = 0

    for i in range(0, max_shyness + 1):
        val = int(numbers_string[i])
        shyness[i] = val
        total_people += val

    while num_standing < total_people:
        if num_standing < a:
            num_standing += 1
            total_people +=1
            people_added += 1
        else:
            num_standing += shyness[a]
            a += 1

    print people_added
    f.write("Case #" + str(n) + ": " + str(people_added) + "\n")
        
f.close()
