
def war(ken, naomi):
    Len = len(ken)
    p_ken = 0
    p_naomi = 0
    ans = 0

    while p_ken < Len and p_naomi < Len:
        if ken[p_ken] > naomi[p_naomi]:
            p_ken += 1
            p_naomi += 1
            ans += 1
        else:
            p_ken +=1

    return Len - ans

def dwar(ken, naomi):
    ans = 0

    while len(ken) > 0:
        if naomi[0] > ken[0]:
            ans += 1
            del naomi[0]
            del ken[0]
        else:
             del naomi[0]
             del ken[-1]

    return ans

def main():
    file_in = open('D-large.in')
    file_out = open('out.txt', 'w')

    cases = int(file_in.readline())

    for case in range(cases):
        ken = []
        naomi = []
        N = int(file_in.readline())
        line = file_in.readline().split(" ")
        for x in line:
            naomi.append(float(x))
        line = file_in.readline().split(" ")
        for x in line:
            ken.append(float(x))

        naomi.sort()
        ken.sort()

        ans_war = war(ken, naomi)
        ans_dwar = dwar(ken, naomi)

        file_out.write("Case #" + str(case + 1) + ": " + str(ans_dwar) + " " +str(ans_war)+ "\n")

    file_in.close()
    file_out.close()



main()





















