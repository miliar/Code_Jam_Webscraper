import sys

file = open(sys.argv[1])
case = int(file.readline())

pala_list = []
final = []

def is_pala(nb):
        str_nb = str(nb)
        len_nb = len(str_nb)

        for i in range (int(len_nb/2)):
                if str_nb[i] != str_nb[len_nb - 1 - i]:
                       return 0

        return 1

for i in range(10000000):
        result = is_pala(i)

        if result:
                pala_list.append(i)


for value in pala_list:
        result = is_pala(value**2)

        if result:
                final.append(value**2)


for a in range(case):
        found = 0
        min, max = map(int, file.readline().split())

        for value in final:
                if value >= min and value <= max:
                        found += 1

        print "Case #%d: %d" % (a+1, found)




