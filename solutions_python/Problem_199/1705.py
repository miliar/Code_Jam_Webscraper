def to_str(pancakes):
    result = str()
    for pancake in pancakes:
        if pancake:
            result += '+'
        else:
            result += '-'
    return result
        

if __name__=='__main__':
    
    with open('A-small-attempt0.in', 'r') as f:

        line_no = 0
        for line in f:

            if line_no == 0:
                line_no += 1
                continue
            
            words = line.split()
            pancakes = []
            for char in words[0]:
                pancakes.append(char == '+')
            k = int(words[1])
            count = 0
            
            for i in range(len(pancakes)):
                if not pancakes[i]:
                    if i + k > len(pancakes):
                        break
                    for j in range(i, i + k):
                        pancakes[j] = not pancakes[j]
                    count += 1
                    #print(to_str(pancakes))

            successful = True
            for pancake in pancakes:
                if not pancake:
                    successful = False
                    break

            if successful:
                print 'Case #' + str(line_no) + ': ' + str(count)
            else:
                print 'Case #' + str(line_no) + ': ' + 'IMPOSSIBLE'
            line_no += 1
