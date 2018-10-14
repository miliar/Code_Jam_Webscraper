import os

if __name__ == "__main__":
    fin = open("A-large.in", "r")
    fout = open("A.out", "w")
    T = int(fin.readline())
    for t in range(T):
        t += 1

        line = fin.readline().strip()
        smax, persons = line.split()
        smax = int(smax)

        count_need = 0
        count_current = 0
        for i in range(smax+1):
            num_person = int(persons[i])
            if num_person > 0:
                if count_current < i:
                    count_need += i - count_current
                    count_current += i - count_current
            count_current += num_person

        fout.write("Case #%d: %s\n" % (t, count_need))
    fout.close()

