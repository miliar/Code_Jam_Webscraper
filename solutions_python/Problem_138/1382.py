import sys

fh = open(sys.argv[1])
oh = open("output.txt", "w")

t = fh.readline()
n = 0
naomi = []
ken = []
count = 0
test_no = 1

for line in fh.readlines():
    if not line:
        continue

    count += 1
    if count == 1:
        n = int(line.strip())
    elif count == 2:
        naomi = [float(i) for i in line.split()]
    elif count == 3:
        ken = [float(i) for i in line.split()]
        ken_set = set(ken)

        fair_score = n
        score = 0

        ken.sort()
        naomi.sort()

        ken_fair = ken[:]
        naomi_fair = naomi[:]

        for i in naomi_fair:
            for j in ken_fair:
                if j > i:
                    fair_score -= 1
                    ken_fair.remove(j)
                    break

        i = 0
        while i < n:
            ken_choice = ken[-1-i]

            if naomi[-1] > ken_choice:
                naomi_choice = naomi[-1]
                naomi_told = naomi_choice
            else:
                naomi_choice = naomi[0]
                naomi_told = ken_choice - 0.00001

                # pick unique weight
                while naomi_told in ken_set:
                    naomi_told = naomi_choice - 0.00001

            if naomi_choice > ken_choice:
                score +=1

            naomi.remove(naomi_choice)

            #print naomi_choice, naomi_told, ken_choice

            ken_set.remove(ken_choice)
            i += 1

        ans = "Case #%d: %d %d\n" % (test_no, score, fair_score)
        oh.write(ans)

        count = 0
        test_no += 1

fh.close()
oh.close()
