__author__ = 'Levan Kasradze'

with open('a.in', 'r') as fin:
    with open('a.out', 'w') as fout:
        t = int(fin.readline())
        for i in range(1, t+1):
            r1 = int(fin.readline()) - 1
            t1 = []
            for j in range(4):
                t1.append(fin.readline().strip().split())
            r2 = int(fin.readline()) - 1
            t2 = []
            for j in range(4):
                t2.append(fin.readline().strip().split())

            cnt = 0
            card = 0
            for j in t1[r1]:
                if j in t2[r2]:
                    cnt += 1
                    card = j

            y = card
            if cnt == 0:
                y = 'Volunteer cheated!'
            elif cnt > 1:
                y = 'Bad magician!'
            fout.write('Case #' + str(i) + ': ' + y + '\n')