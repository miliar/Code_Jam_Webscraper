import heapq

num_cases = int(raw_input())

for case in range(1, num_cases + 1):
    N = int(raw_input())

    stream = raw_input()
    stream = stream.split(" ")
    naomi = [float(s) for s in stream]

    stream = raw_input()
    stream = stream.split(" ")
    ken = [float(s) for s in stream]

    naomi_war = sorted(naomi)
    ken_war = sorted(ken)

    naomi_d = sorted(naomi)
    ken_d = sorted(ken)

    war_count = 0
    d_count = 0

    len_war = len(naomi_war)
    len_d = len(naomi_d)

    while (len_war != 0 or len_d != 0):
        if len_war > 0:
            if naomi_war[-1] > ken_war[-1]:
                naomi_war.pop()
                ken_war.pop(0)
                war_count = war_count + 1
            else:
                naomi_war.pop()
                ken_war.pop()

        if len_d > 0:
            if naomi_d[0] > ken_d[0]:
                naomi_d.pop(0)
                ken_d.pop(0)
                d_count = d_count + 1
            else:
                naomi_d.pop(0)
                ken_d.pop()

        len_war = len(naomi_war)
        len_d = len(naomi_d)

    print ("Case #%d: %d %d" % (case, d_count, war_count))