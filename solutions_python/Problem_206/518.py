def finish_time(start, finish, speed):
    return (finish - start) / speed

fileIn = open('A-large.in','r')
fileOut = open('out.txt','w')

T = int(fileIn.readline().strip())
for t in range(1, T+1):
    D, N = fileIn.readline().strip().split()
    D, N = int(D), int(N)
    last_finish = 0
    for i in range(N):
        K, S = fileIn.readline().strip().split()
        K, S = int(K), int(S)
        last_finish = max(finish_time(K, D, S), last_finish)
    speed = D/last_finish
    fileOut.write('Case #'+str(t)+': '+str(speed)+'\n')




fileOut.close()
fileIn.close()
