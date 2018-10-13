#f = open('C:/Users/Avinash/Desktop/Google codejam 2017/pycharmworks/input2','r')  # C:\Users\Avinash\Desktop\Google codejam 2017\pycharmworks\AA-small-practice.in
# f = open('C:/Users/Avinash/Desktop/Google codejam 2017/pycharmworks/A-large-practice.in', 'r')
f = open('C:/Users/Avinash/Desktop/Google codejam 2017/pycharmworks/A-large.in', 'r')
data = f.readlines()
f.close()
f = open('Oversized1', 'w')
t = data[0]
y = 0
for i in data[1:]:
    y += 1
    count = 0
    out = [item for item in i.split(' ')]
    string = out[0]
    flipper = int(out[1])

    #print(string, flipper)
    try:
        if flipper>len(string):
            for j in range(len(string)):
                if string[j]=="-":
                    print("Case #" + str(y) + ": IMPOSSIBLE", file=f)
                    break

        else:
            for j in range(len(string)):
                # print(string[j])
                string1 = ""
                if string[j] == "-":
                    # print(j)
                    for k in range(flipper):
                        if string[j + k] == "-":
                            string1 += "+"
                        else:
                            string1 += "-"
                    count += 1
                    string = string[:j] + string1 + string[j + flipper:]
                    # print(j)
                # print(string1)

                # print(string)
        #print(count)

        print("Case #" + str(y) + ": " + str(count), file=f)
    except:
        print("Case #" + str(y) + ": IMPOSSIBLE", file=f)

f.close()
