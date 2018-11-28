FILE_NAME = "test.in"

def main(file_name):
    input_file = open(file_name, 'r', 0)
    T = int(input_file.readline())
    for i in range(T):
        N = int(input_file.readline())
        points = []
        for j in range(N):
            x, y = input_file.readline().split(' ')
            x, y = int(x), int(y)
            points.append((x,y))
        y = 0
        c = 0
        for j in points:
            for k in points[c+1:]:
                if intersect(j,k):
                    y += 1
            c += 1
        print "Case #%d: %d" % (i+1, y)

def intersect(x,y):
    if x[0] < y[0] and x[1] < y[1]:
        return False
    if x[0] > y[0] and x[1] > y[1]:
        return False
    return True 

main(FILE_NAME)
