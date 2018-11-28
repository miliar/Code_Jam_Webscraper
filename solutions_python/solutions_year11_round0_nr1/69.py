"""
Code Jam 2011 Qualification Round
BotTrust by Warren Usui
"""
def doAction(queue, loc, boolv):
    if len(queue) > 0:
        if loc == queue[0]:
            if boolv:
                queue.pop(0)
                return queue, loc, True
        if loc < queue[0]:
            loc += 1
        if loc > queue[0]:
            loc -= 1  
    return queue, loc, False

def BotTrust(fileHead):
    rootd = 'C:\\wutemp\\CodeJam\\2011'
    infile = "{0}\\{1}.in".format(rootd,fileHead)
    outfile = "{0}\\{1}.out".format(rootd,fileHead)
    fin = open(infile,'r')
    fout = open(outfile,'w')
    number = int(fin.readline())
    for iterv in xrange(0,number):
        count = 0
        txt = fin.readline()
        cnumbs = txt.split(" ")
        pushes = int(cnumbs[0])
        oqueue = []
        bqueue = []
        order = []
        indx = 1
        for _ in xrange(0,pushes):
            numb = int(cnumbs[indx+1])
            order.append(cnumbs[indx])
            if cnumbs[indx] == 'B':
                bqueue.append(numb)
            else:
                oqueue.append(numb)
            indx += 2
        bloc = 1
        oloc = 1
        while len(order) > 0:
            oqueue, oloc, oact = doAction(oqueue, oloc, order[0] == 'O')
            bqueue, bloc, bact = doAction(bqueue, bloc, order[0] == 'B')
            if oact or bact:
                order.pop(0)
            count += 1
        odata = "Case #{0}: {1}\n".format(iterv+1, count)
        fout.write(odata)
        
if __name__ == '__main__':
    BotTrust('A-large')