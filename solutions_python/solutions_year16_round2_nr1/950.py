a = input()
b= []

for i in range(a):
    b.append(raw_input())

def func(string):
    d = {}
    d["W"] = 0
    d["U"] = 0
    d["G"] = 0
    d["Z"] = 0
    d["X"] = 0
    d["O"] = 0
    d["F"] = 0
    d["S"] = 0
    d["H"] = 0
    d["I"] = 0

    for j in string:

        d[j] = 0 
    for k in string:
        d[k] += 1
    d[2] = d["W"]
    d[4] = d["U"]
    d[6] = d["X"]
    d[8] = d["G"]
    d[0] = d["Z"]
    d[1] = d["O"] - d[2] - d[4] - d[0]
    d[3] = d["H"] - d[8]
    d[5] = d["F"] - d[4]
    d[7] = d["S"] - d[6]
    d[9] = d["I"] - d[5] - d[6] - d[8]

    result = ""
    for i in range(10):
        if d[i] != 0:
            result = result + str(i)*d[i]

    return result

for i in range(a):
    print "Case #" + str(i+1)+":",func(b[i])
