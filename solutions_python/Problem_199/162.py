def flip(cakes,k,i):

    for i in range(i,i+k):

        if pancakes[i] == '+':

            pancakes[i] = '-'

        else:

            pancakes[i] = '+'
        
def happy(cakes):

    for i in cakes:

        if i=='-':

            return 0

    return 1
    


for tests in range(int(input())):
    
    pancakes, k = input().split()

    pancakes = list(pancakes)

    k = int(k)

    count = 0

    for i in range(0,len(pancakes)-k+1):

        if pancakes[i]=='-':

            flip(pancakes,k,i)

            count+=1

    output = 'Case #' + str(tests+1)+': '

    if happy(pancakes):

        output += str(count)

    else:
        
        output += 'IMPOSSIBLE'

    print(output)
    

    
