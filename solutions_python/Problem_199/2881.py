def happy_faces(pancake_row):
    if "-" in pancake_row:
        return False

    return True


def reversing_faces(item):
    if item == "+":
        return "-"
    else:
        return "+"


count = 0
case_no = 0
file_name = open("A-large.in", "r")
for line in file_name:
    flips = 0
    if (count == 0):
        count += 1
        case_no = int(line)
        continue
    pancake = line.replace("\n","")
    k= int(pancake.split(' ')[1])
    pancake_list = list(pancake.split(' ')[0])
    try:
        for i in xrange(len(pancake_list)):
            if pancake_list[i] == "-":
                flips += 1
                for j in xrange(i,i + k):
                    pancake_list[j] = reversing_faces(pancake_list[j])
        if (happy_faces(''.join(pancake_list))):
            print("Case #{}: {}".format(count, flips))
        else:
            print("Case #{}: {}".format(count, "IMPOSSIBLE"))
        count =count + 1
    except:
        print("Case #{}: {}".format(count, "IMPOSSIBLE"))
        count=count + 1

