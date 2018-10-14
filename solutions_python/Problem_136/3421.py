
input = open("B-small-attempt0.in", 'r')
output = open("output.txt", 'w')

cases = int(input.readline())
if (cases < 1) or (cases > 100):
    output.write("Bad input!\n")

else:
    outs = []
    for i in range(cases):
        params = input.readline()
        params = params.rstrip('\n').split(" ")
        C = float(params[0])
        F = float(params[1])
        X = float(params[2])
        if (C<1) or (C>500) or (F<1) or (F>4) or (X<1) or (X>2000):
            outs.append("Bad input!")
        else:
            R = 2.0
            T = 0.0
            while (C*(R+F) < X*F):
                T += C/R
                R += F
            T += X/R
            outs.append(str("%.7f" % T))

    for i in range(cases):
        output.write("Case #" + str(i+1) + ": " + outs[i] + "\n")

