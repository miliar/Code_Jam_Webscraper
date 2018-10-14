f = open('A-large.in','r')
o = open('A-large.out','w')
runs = int(f.readline())

def gcd(a,b):
    while b:
        a,b = b,a%b
    return a

for i in range(runs):
    line = f.readline()
    (pancakes,k) = line.split(' ')
    k = int(k)
    pancakes = list(pancakes)
    for item in range(len(pancakes)):
        if pancakes[item]=='+':
            pancakes[item] = 1
        else:
            pancakes[item] = 0
    if(sum(pancakes) == len(pancakes)):
        out = 'Case #'+str(i+1)+': '+str(0)+'\n'
        o.write(out)
        continue                                            #This section works for Case 16 not 11
    #if (k%2==0 and (len(pancakes)-sum(pancakes))%2==1) or (k%2==1 and ((len(pancakes)-sum(pancakes))%k)%2==1):
                                                            #This section works for Case 11 not 16
    # if (k%2==0 and (len(pancakes)-sum(pancakes))%2==1) or (k%2==1 and ((sum(pancakes) - (len(pancakes)-sum(pancakes)))%2==1)):
    # #if -(len(pancakes) - sum(pancakes)) % gcd(k, 2) != 0:
    #     out = 'Case #'+str(i+1)+': IMPOSSIBLE\n'
    #     o.write(out)
    #     continue

    flips = [0]*len(pancakes)
    flips[0] = 1-pancakes[0]
    for j in range(1,len(pancakes)-k+1):
        flips[j] = (pancakes[j-1] - pancakes[j]) #sum(pancakes[max(0,j-k):j]))%2
        if j >= k:
            flips[j] += flips[j-k]
        flips[j] = flips[j] % 2

    for j in range(len(flips)):
        if(flips[j] == 1):
            for m in range(j,j+k):
                if(pancakes[m] == 1):
                    pancakes[m] = 0
                else:
                    pancakes[m] = 1
    if(sum(pancakes) == len(pancakes)):
        out = 'Case #'+str(i+1)+': '+str(sum(flips)) +'\n'
    else:
        out = 'Case #'+str(i+1)+': IMPOSSIBLE\n'
    o.write(out)
