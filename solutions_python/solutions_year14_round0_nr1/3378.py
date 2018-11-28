import sys
sys.stdin = open("input.txt")
sys.stdout = open("output.txt", "w+")

for case in range(input()):
    output = "Case #%s: " % (case+1)

    A = input()
    X = [raw_input(), raw_input(), raw_input(), raw_input()][A-1].split()

    B = input()
    Y = [raw_input(), raw_input(), raw_input(), raw_input()][B-1].split()

    Z = list(set(X) & set(Y))
    if len(Z) == 0:
        output += "Volunteer cheated!"
    elif len(Z) == 1:
        output += Z[0]
    else:
        output += "Bad magician!"

    print output
