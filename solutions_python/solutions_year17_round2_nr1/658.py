def read_file():
    #f = open('C:/Users/Avinash/Desktop/Google codejam 2017/pycharmworks/input2', 'r')
    # C:\Users\Avinash\Desktop\Google codejam 2017\pycharmworks\AA-small-practice.in
    f = open('C:/Users/Avinash/Desktop/Google codejam 2017/pycharmworks/A-large.in', 'r')
    # f = open('C:/Users/Avinash/Desktop/Google codejam 2017/pycharmworks/C-small-1-attempt0.in', 'r')
    # f = open('C:/Users/Avinash/Desktop/Google codejam 2017/pycharmworks/B-large.in', 'r')
    data1 = f.readlines()
    f.close()
    return data1


def output(number, y, f):
    print("Case #" + str(y) + ": ", file=f)


def main():
    y = 0

    data = read_file()
    f = open('Round 1 1', 'w')
    i = 0
    while (i < (len(data))):

        #print(i)
        array = []
        if i == 0:
            t = data[i]
            i+=1
        else:
            y += 1
            out = [item for item in data[i].split(' ')]
            D = int(out[0])
            N = int(out[1])
            for a in range(N):
                out = [item for item in data[i + a + 1].split(' ')]
                K = int(out[0])
                S = int(out[1])
                array.append((D - K) / S)
            i += N+1
            #print(i,N,D)
            speed = max(array)
            #print(speed)
            number = D / speed
            #print(number)
            print("Case #" + str(y) + ": " + str(number), file=f)

    f.close()


main()
