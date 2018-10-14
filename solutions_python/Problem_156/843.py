
def runCase(original_data, n):

    go_on = True
    stack = [original_data]
    stack_counts = [0]
    stack_finished = []
    stack_finished_counts = [100000]

    i = 0
    while i < len(stack) and len(stack) > 0:

        stack[i].sort()
        

        if stack_counts[i] > min(stack_finished_counts):
            stack.pop(i)
            stack_counts.pop(i)
            i = i -1

        else:
                              
            if stack[i][-1] == 0:

                stack.pop(i)
                stack_finished_counts.append(stack_counts.pop(i))
                i = i -1
                
            elif stack[i][-1] == 3:

                stack.pop(i)
                stack_finished_counts.append(stack_counts.pop(i)+3)
                i = i-1

            elif stack[i][-1] == 2:

                stack.pop(i)
                stack_finished_counts.append(stack_counts.pop(i)+2)
                i = i-1

            elif stack[i][-1] == 1:
                stack.pop(i)
                stack_finished_counts.append(stack_counts.pop(i)+1)
                i = i-1

            elif stack[i][-1] < 0:
                print("ERRROR")

            else:

                """Variante Essen Lassen"""               
                stack.append([a - 1 for a in stack[i]])
                stack_counts.append(stack_counts[i]+1)

                """Variante Special Special"""
                highest_plate = stack[i][-1]
                for j in range(3,min(highest_plate//2+1,5)):
                    neu = stack[i][:]
                    neu[-1] = highest_plate//j + highest_plate%j
                    neu.append( highest_plate - (highest_plate//j + highest_plate%j ))
                    stack.append(neu)
                    stack_counts.append(stack_counts[i]+1)
                    
                """Variante Special Round"""
                highest_plate = stack[i][-1]
                stack[i][-1] = highest_plate//2 + highest_plate%2
                stack[i].append( highest_plate//2 )
                stack_counts[i] += 1





                i = i-1


                

        i += 1
    return min(stack_finished_counts)


        

        
f = open('B-small-attempt5.in', 'r')
output = ""

amountCases = int(f.readline())

for caseNumber in range(amountCases):
    print(caseNumber)
    n_data = f.readline()
    n = int(n_data[0])
    data = [int(j) for j in f.readline().split()]
    result = runCase(data, n)
    output += "Case #" + str(caseNumber+1) + ": " + str(result) + "\n"

        
print(output)

