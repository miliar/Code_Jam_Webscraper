def read_file():
    #f = open('C:/Users/Avinash/Desktop/Google codejam 2017/pycharmworks/input2', 'r')
    # C:\Users\Avinash\Desktop\Google codejam 2017\pycharmworks\AA-small-practice.in
    f = open('C:/Users/Avinash/Desktop/Google codejam 2017/pycharmworks/B-small-attempt2.in', 'r')
    # f = open('C:/Users/Avinash/Desktop/Google codejam 2017/pycharmworks/C-small-1-attempt0.in', 'r')
    # f = open('C:/Users/Avinash/Desktop/Google codejam 2017/pycharmworks/B-large.in', 'r')
    data1 = f.readlines()
    f.close()
    return data1


def output(number, y, f):
    print("Case #" + str(y) + ": ", file=f)


def main():
    z = 0

    data = read_file()
    f = open('Round 2 3 small', 'w')
    for i in range(len(data)):

        if i == 0:
            t = data[i]
        else:
            z += 1
            array = []
            out = [item for item in data[i].split(' ')]
            N = int(out[0])
            R = int(out[1])
            Y = int(out[3])
            B = int(out[5])
            high = max(R, Y, B)
            low = min(R, Y, B)
            #print(N, R, Y, B)
            if high > N - high:
                #print(high)
                print("Case #" + str(z) + ": IMPOSSIBLE", file=f)
            else:
                if (R != 0):
                    array = 'R'
                    R -= 1
                elif (Y != 0):
                    array = 'Y'
                    Y -= 1
                elif (B != 0):
                    array = 'B'
                    B -= 1
                for j in range(1, N):
                    if (array[j - 1] == 'R'):
                        if (B == max(Y, B) and B != 0):
                            array += 'B'
                            B += - 1
                        elif Y == max(Y, B) and Y != 0:
                            array += 'Y'
                            Y += - 1
                    elif (array[j - 1] == 'B'):
                        if (R == max(Y, R) and R != 0):
                            array += 'R'
                            R += - 1
                        elif Y == max(Y, R) and Y != 0:
                            array += 'Y'
                            Y += - 1
                    elif (array[j - 1] == 'Y'):
                        if (R == max(B, R) and R != 0):
                            array += 'R'
                            R += - 1
                        elif (B == max(B, R) and B != 0):
                            array += 'B'
                            B += - 1
                    #print(R, Y, B, array)
                if(N!=len(array)):
                    print("Case #" + str(z) + ": IMPOSSIBLE", file=f)
                elif(array[0]==array[-1]):
                    print("Case #" + str(z) + ": IMPOSSIBLE", file=f)
                else:
                    print("Case #" + str(z) + ": " + array, file=f)
    f.close()


main()
