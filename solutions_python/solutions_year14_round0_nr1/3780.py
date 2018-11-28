
def get_result(a1, b1, a2, b2):
    #return repr(a1) + ' ' + repr(b1) + ' ' + repr(a2) + ' ' + repr(b2)
    s1 = set(b1[a1 - 1])  # set 1
    s2 = set(b2[a2 - 1])
    intc = s1 & s2  # set intersection
    if len(intc) == 1:
        return str(list(intc)[0])
    elif len(intc) == 0:
        return 'Volunteer cheated!'
    else:
        return 'Bad magician!'

def main():
    t = int(input())
    for ti in range(1, 1 + t):
        a1 = int(input())  # answer 1
        b1 = list()  # board 1
        for i in range(4):
            b1.append(list(map(int, input().split())))
        a2 = int(input())
        b2 = list()
        for i in range(4):
            b2.append(list(map(int, input().split())))
        print("Case #{cn}: {result}".format(
            cn=ti,
            result=get_result(a1, b1, a2, b2)))

main()
