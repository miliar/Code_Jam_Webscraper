t = input()
for i in range(t):
        first = input()
        for j in range(4):
                if j == first-1:
                        first_row = map(int,raw_input().split())
                else:
                        raw_input()
        second = input()
        for j in range(4):
                if j == second-1:
                        second_row = map(int,raw_input().split())
                else:
                        raw_input()
        count = 0
        value = 0
        for j in range(4):
                if first_row[j] in second_row:
                        count = count + 1
                        value = first_row[j]
        if count == 0:
                print 'Case #'+str(i+1)+': Volunteer cheated!'
        elif count == 1:
                print 'Case #'+str(i+1)+': '+str(value)
        else:
                print 'Case #'+str(i+1)+': Bad Magician!'
