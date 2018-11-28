import sys;
sys.setrecursionlimit(15000)

def readLine(content):
    pp = content.pop(0).strip().split();
    f = map(float, pp);
    return f;

def sortBlocks(blocks):
    blocks.sort();
    return blocks[::-1];

class WarPlayer:
    def __init__(self, name, blocks):
        self.name = name;
        self.blocks = sortBlocks(blocks); # sorted list of block weights

    def startMove(self, i):
        # propose a block to play: start with it's lightest block
        b = self.blocks;
        mb = b.pop();
        return mb;

    def returnMove(self, x, i):
        # return lightest block which is heavier than given one
        b = self.blocks;

        if (b[0] < x): # if heaviest block is lighter than given - return lightest
            resp = b.pop();
            return resp;

        # else search for the lithest block which is heavier than given
        for i in reversed(xrange(len(b))):
            if (b[i] > x):
                resp = b.pop(i);
                return resp;
        #end for
    #end def

#end class WarPlayer

class LWarPlayer(WarPlayer):
    def returnMove(self, x, i):
        r = WarPlayer.returnMove(self, x, i);
        print "%d: %s moved with %f and %s" % (i, self.name, r, "Wins" if r > x else "Loses");
        return r;
#end of LoggingWarPlayer

class DWarPlayer(WarPlayer):
    def __init__(self, name, blocks, otherBlocks):
        WarPlayer.__init__(self, name, blocks);
        self.otherBlocks = otherBlocks;
    #end __init__

    def startMove(self, i):
        # propose a block to play:
        b = self.blocks;
        om = None;
        if (self.blocks[-1] < self.otherBlocks[-1] or len(b)==1):
            mb = b.pop(); # select lightest block

            # but say we are playing the block which is lighter than to opp second lightest but heavier than first
            om = self.getOppositesMove(mb)
            if (om is None):
                om = mb;
        else:
            om = b.pop(); # selet last one - it's heavier that opposite's
            om = b[0]; # but told it's heaviest one

        print "%d: %s moved with %f" % (i, self.name, om);
        return om;

    def getOppositesMove(self, x):
        b = self.otherBlocks;

        if (b[0] < x or len(b)==1): # if heaviest block is lighter than given - return lightest
            return None;

        # else search for the heaviest block
        else:
            return (b[0]+b[1])/2.0
        #end for


def playGame(gameName, n, k):
    print gameName;
    naomiWins = 0;
    num = len(k.blocks);
    for i in range(num):
        b = n.startMove(i);
        r = k.returnMove(b, i);
        if (b>=r):
            #print("Naomi win")
            naomiWins += 1;
        else:
            #print("Ken win")
            pass;
        #end if

    print gameName, naomiWins;
    return naomiWins;
#end playGame


def findResult(num, lineN, lineK):
    k = WarPlayer("Ken", list(lineK));
    n = WarPlayer("Naomi", list(lineN));

    print "Naomi:\t", n.blocks;
    print "Ken:\t", k.blocks;

    # play game
    naomiWarWins = playGame("War", n, k);

    k = LWarPlayer("Ken", list(lineK));
    n = DWarPlayer("Naomi", list(lineN), k.blocks);

    naomiDesWins = playGame("Deceitful War", n, k);

    return "%d %d" % (naomiDesWins, naomiWarWins);
#end def


fname = "D-large.in"
with open(fname) as f:
    content = f.readlines();

    T = int(content.pop(0))
    #print T

    with open("dwar.out.txt", "w+") as fout:
        for i in range(T):
            N = int(content.pop(0).strip()); # remove number of block
            lineN = readLine(content)
            lineK = readLine(content)
            res = "Case #%d: %s" % (i+1, findResult(N, lineN, lineK))
            print res

            fout.write(res)
            fout.write("\n")

