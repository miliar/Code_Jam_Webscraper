def main():
    f = open("input.txt", "r")
    lines = f.readlines()

    i = 0

    for e in lines:
        if i == 0:
            i = 0
        else:
            print "Case #" + str(i) + ": " +  str(test(e))
        i += 1


def test(data):
    data = data.split()
    loops = int(data[0])
    info = data[1]

    count = 0;
    loc = 0;
    people_needed = 0;
    people = 0;

    for e in info:
        value = int(e)
        if people - loc < 0 and value != 0:
            people_needed +=  loc-people
            people += (value+people_needed)
        else:
            people += value
        loc+=1

    return people_needed

main()
