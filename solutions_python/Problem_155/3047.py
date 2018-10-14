PATH = "/Users/vchoubard/Projects/Python/Google code jam/"
INPUT_FILE = PATH + "A-large.in"
OUTPUT_FILE = PATH + "output.out"

f = open(INPUT_FILE, 'r')
o = open(OUTPUT_FILE, 'w')
nb_cases = int(f.readline())
for x in range(nb_cases):
    standing = 0
    friends = 0
    max_shine, people = f.readline().split(" ")
    for shiness in range(int(max_shine) + 1):
        nb_person = int(people[shiness])
        if shiness > standing and nb_person > 0:
            new_friends = shiness - standing
            friends += new_friends
            standing += new_friends

        standing += nb_person

    o.write("Case #{0}: {1}\n".format(str(x+1), str(friends)))

f.close()
o.close()

