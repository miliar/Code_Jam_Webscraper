rf = open('B-large.in', 'r')

line_counter = 0
T = None

INI_RATE = 2.0
num_facts = 0

case_num = 0
sec = 0

fw = open("B-large.out", "w")
times = []

for l in rf:
    tokens = l.split()
    if len(tokens) > 0:
        line_counter += 1
        if line_counter == 1:
            T = int(tokens[0])
        else:
            case_num += 1
            C, F, X = tokens
            C = float(C)
            F = float(F)
            X = float(X)
            num_facts = 0
            times = []

            # while cookie collection till target at current rate takes more time
            # then with rate from additional target (although starting from 0 cookies)
            # keep adding factories
            while((X-C)/(INI_RATE + num_facts * F) > X/(INI_RATE + (num_facts+1) * F)):
                num_facts += 1

            for i in range(0, num_facts):
                times.append(C/(INI_RATE + i*F))

            fw.write("Case #%d: %.8f\n" % (case_num, sum(times) + X/(INI_RATE + num_facts * F)))

