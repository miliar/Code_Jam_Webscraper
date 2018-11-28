#lines = open('input.in', 'r')
#lines = open('A-small-attempt1.in', 'r')
lines = open('A-large.in', 'r')

array = []
for line in lines:
	array.append(line)

lines.close()

cases = array[0]

for i in range(int(cases)):
        line = array[i + 1]
        tokens = line.split()
        shyness_string = tokens[1]

        need_add = 0
        total_persons = 0
        level = 0
        for c in shyness_string:
                if c == '0':
                        level += 1
                        continue
                if total_persons < level:
                        need_add += level - total_persons
                        total_persons = level
                total_persons += int(c)
                level += 1


        print 'Case #' + str(i + 1) + ': ' + str(need_add)
