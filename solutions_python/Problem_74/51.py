
import sys

def main():

    if len(sys.argv) == 2:
        filename = sys.argv[1] #input file name from command line
    else:
        filename = "testcases.txt"
    inputfile = open(filename, 'r')
    testcases = int(inputfile.readline())
    for i in xrange(testcases):
        print 'Case #%s: %s'%(i+1,jammit(inputfile.readline()))

def jammit(inputline):
    cases = int(inputline.split()[0])
    if cases == 0:
        return 0
    botrecord = {}
    time = 0
    datas = inputline.split()[1:]
    while (len(datas)):
        bot = datas[0]
        butt = int(datas[1])
        rec = botrecord.setdefault(bot,[0,1])
        timeready = (rec[0] + abs(butt - rec[1]))
        if time > timeready:
            time += 1
        else:
            time = timeready + 1
        botrecord[bot] = [time,butt]


        datas = datas[2:]
    
    return time



# def jammit(dataset):
#     bots = dataset[2]
#     botIndex = dataset[1]
#     tokens = dataset[0]
#     botsNextTime = [-2]*len(bots)
#     botsLocs = [1]*len(bots)
#     time = 0
#     nextBot = bots.index(tokens[0][0])
#     print 'nextBot', nextBot
#     #while(sum(map(len,botIndex.values())) > 0):
#     while(len(tokens)):
#         for i,bot in zip(range(len(bots)),bots):
#             if botsNextTime[i] == NEED_NEW_TARGET: 
#                 if len(botIndex[bots[i]]) == 0:
#                     del(bots[i])
#                 else:
#                     botsNextTime[i] = time+abs(tokens[botIndex[bots[i]][0]][1] - botsLocs[i])

#         if botsNextTime[nextBot] <= time:
#             time += 1 
#         else:
#             time = botsNextTime[nextBot]+1
#         print 'new time', time
#         botsNextTime[nextBot] = NEED_NEW_TARGET
#         tokens = tokens[1:]
#     return time


# def do_jam(inputline):    
#     bots = ['B','O']
#     botsNextTime = [-2]*len(bots)
#     botsLocs = [1]*len(bots)
#     time = 0

#     while(len(inputline)):
# #        print inputline
#         if len(inputline) < 3:
#             break
#         else:
#             nextBot = bots.index(inputline.split()[0])

#         for i,bot in zip(range(len(bots)),bots):
#             if botsNextTime[i] == NEED_NEW_TARGET: 
#                 nextIndex = inputline.find(bot)
#                 if nextIndex == -1:
#                     botsNextTime[i] = -1
#                 else:
#                     nextbutt = int(inputline[nextIndex + 2])
#                     botsNextTime[i] = time + abs(nextbutt - botsLocs[i])
#                     botsLocs[i] = nextbutt
#                     print 'next step for bot', bots[i], 
#                     print nextbutt, time, botsLocs[i], abs(nextbutt - botsLocs[i])



#         print 'botsNextTime',bots[nextBot], botsNextTime[nextBot],
#         if botsNextTime[nextBot] <= time:
#             time += 1 
#         else:
#             time = botsNextTime[nextBot]+1
#         print 'new time', time
#         botsNextTime[nextBot] = NEED_NEW_TARGET
#         inputline = " ".join(inputline.split()[2:])


#     return time



# def tokenizeAndIndex(inputline):
#     items = inputline.split()
#     biglist = []
#     bots = {}
#     count = 0
#     botIndex = {}
#     while(len(items)):
# #        print items[0], items[1], count
#         biglist.append((items[0], int(items[1])))
#         if botIndex.has_key(items[0]):
#             botIndex[items[0]].append(count)
#         else:
#             botIndex[items[0]] = [count]
             
#         bots[items[0]] = 1
#         items = items[2:]
#         count += 1
#     return [biglist, botIndex, bots.keys()]


main()
