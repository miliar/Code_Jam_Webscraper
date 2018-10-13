def test1(x,r,c):
    if x > r and x > c:
        return True
    return False

def test2(x,r,c):
    if not (r*c) % x == 0:
        return True
    return False

def test3(x,r,c):
    if x > 6:
        return True
    return False


#Check if can make piece bigger than width and length
def test4(x,r,c):
    max_width = (x+1)/2

    max_length = max_width
    if x%2 == 0:
        max_length += 1
    #if max_width > max(r,c):
    #    return True
    if max_width > min(r,c):
        return True
    elif max_width > min(r,c) and max_length > max(r,c):
        return True
    else:
        return False

def test5(x,r,c):
    if x == 4:
        if min(r,c) == 2 and max(r,c)%4 == 0:
            return True
    return False

def ominos(x,r,c):
    test = test1(x,r,c) or test2(x,r,c) or test3(x,r,c) or test4(x,r,c) or test5(x,r,c)
    if test:
        return "RICHARD"
    else:
        return "GABRIEL"


file_name = "D-small-attempt2"
file_handle = open(file_name + ".in")
output_file = open(file_name + ".out", 'w')

test_cases = int(file_handle.readline())

for i in range(0,test_cases):
    line_split = file_handle.readline().split()

    x = int(line_split[0])
    r = int(line_split[1])
    c = int(line_split[2])

    output_file.write("Case #{0}: {1}\n".format(str(i+1), ominos(x,r,c)))
    

file_handle.close()
output_file.close()
