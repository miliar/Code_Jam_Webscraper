{
 "cells": [
  {
   "cell_type": "code",
   "execution_count": 5,
   "metadata": {
    "collapsed": true
   },
   "outputs": [],
   "source": [
    "import math"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 44,
   "metadata": {
    "collapsed": false
   },
   "outputs": [],
   "source": [
    "def solve(pancakes, K):\n",
    "    widest = sorted(pancakes, cmp = lambda (a,b),(c,d): cmp(a,c), reverse=True)\n",
    "    overall = sorted(pancakes, cmp= lambda (a,b),(c,d) : cmp(a*b, c*d), reverse=True)\n",
    "    \n",
    "    topk = overall[:K]\n",
    "    r = max([r for r,h in topk])\n",
    "    best = math.pi*r*r + sum([a*b for a,b in topk]) * math.pi * 2\n",
    "    #print topk\n",
    "    \n",
    "    for r,h in widest:\n",
    "        #print (r,h), topk[-1]\n",
    "        \n",
    "        if (r,h) in topk:\n",
    "            break\n",
    "        res = math.pi*r*r + (r*h+sum(a*b for a,b in topk[:-1])) *math.pi * 2\n",
    "        \n",
    "        if res > best:\n",
    "            best = res\n",
    "        \n",
    "    return best"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 49,
   "metadata": {
    "collapsed": true
   },
   "outputs": [],
   "source": [
    "def parse(text):\n",
    "    T = int(text.next())\n",
    "    for i in range(T):\n",
    "        N,K = [int(x) for x in text.next().rstrip().split(\" \")]\n",
    "        \n",
    "        pancakes = []\n",
    "        for j in range(N):\n",
    "            r,h = [int(x) for x in text.next().rstrip().split(\" \")]\n",
    "            pancakes.append((r,h))\n",
    "            \n",
    "        soln = solve(pancakes, K)\n",
    "        \n",
    "        print \"Case #%d: %f\" % (i+1, soln)"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 50,
   "metadata": {
    "collapsed": true
   },
   "outputs": [],
   "source": [
    "TEXT = \"\"\"4\n",
    "2 1\n",
    "100 20\n",
    "200 10\n",
    "2 2\n",
    "100 20\n",
    "200 10\n",
    "3 2\n",
    "100 10\n",
    "100 10\n",
    "100 10\n",
    "4 2\n",
    "9 3\n",
    "7 1\n",
    "10 1\n",
    "8 4\"\"\""
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 51,
   "metadata": {
    "collapsed": false
   },
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "Case #1: 138230.076758\n",
      "Case #2: 150796.447372\n",
      "Case #3: 43982.297150\n",
      "Case #4: 625.176938\n"
     ]
    }
   ],
   "source": [
    "parse(x for x in TEXT.splitlines())"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 52,
   "metadata": {
    "collapsed": false
   },
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "Case #1: 138230.076758\n",
      "Case #2: 150796.447372\n",
      "Case #3: 43982.297150\n",
      "Case #4: 625.176938\n",
      "Case #5: 304417951090.751892\n",
      "Case #6: 267002122974.991394\n",
      "Case #7: 7331783211076.537109\n",
      "Case #8: 3244632056648.302734\n",
      "Case #9: 8227516786763.760742\n",
      "Case #10: 23342646186.960838\n",
      "Case #11: 514737358504.146729\n",
      "Case #12: 196950613949.207703\n",
      "Case #13: 4009149370406.785645\n",
      "Case #14: 8562510541856.970703\n",
      "Case #15: 282481388730.988220\n",
      "Case #16: 177647585775.422699\n",
      "Case #17: 2939088981747.248535\n",
      "Case #18: 3462981535705.542969\n",
      "Case #19: 7876230038599.625000\n",
      "Case #20: 367748647493.817505\n",
      "Case #21: 4703349845171.217773\n",
      "Case #22: 2706482809417.278320\n",
      "Case #23: 6818840403979.035156\n",
      "Case #24: 16657003088429.363281\n",
      "Case #25: 222447187707.252930\n",
      "Case #26: 24015620383.798424\n",
      "Case #27: 13126068729359.386719\n",
      "Case #28: 597230552975.142578\n",
      "Case #29: 8154273755.422476\n",
      "Case #30: 16761975001.679039\n",
      "Case #31: 279754286125.388428\n",
      "Case #32: 7926800484880.724609\n",
      "Case #33: 2254762634490.075684\n",
      "Case #34: 1147246026389.978027\n",
      "Case #35: 17229464394754.566406\n",
      "Case #36: 7919450638769.914062\n",
      "Case #37: 12692408223624.113281\n",
      "Case #38: 212334390195.392517\n",
      "Case #39: 4217344809152.083008\n",
      "Case #40: 251995111222.168091\n",
      "Case #41: 144077083385.088379\n",
      "Case #42: 1152541455203.730713\n",
      "Case #43: 32101003388.566242\n",
      "Case #44: 17220627159.016384\n",
      "Case #45: 21547602932.570404\n",
      "Case #46: 7913106219.219484\n",
      "Case #47: 10097185641793.832031\n",
      "Case #48: 250497270712.983551\n",
      "Case #49: 2544677968617.386719\n",
      "Case #50: 176166883888.809418\n",
      "Case #51: 156192410345.977417\n",
      "Case #52: 3823028736774.335938\n",
      "Case #53: 10876867893436.816406\n",
      "Case #54: 3864762625395.469727\n",
      "Case #55: 221841322591.619537\n",
      "Case #56: 261088606465.758148\n",
      "Case #57: 2890884363791.585938\n",
      "Case #58: 2348604564950.107910\n",
      "Case #59: 2547090024429.428711\n",
      "Case #60: 680528863796.976562\n",
      "Case #61: 17141730930080.222656\n",
      "Case #62: 6211453154120.361328\n",
      "Case #63: 3480339372998.128906\n",
      "Case #64: 191363702784.365082\n",
      "Case #65: 49929428889.379311\n",
      "Case #66: 65973445725385.656250\n",
      "Case #67: 5095319310216.232422\n",
      "Case #68: 8125929621.634591\n",
      "Case #69: 5086173194696.845703\n",
      "Case #70: 207964776371.344055\n",
      "Case #71: 16999720476.402700\n",
      "Case #72: 1593886614388.905518\n",
      "Case #73: 15737961500.534449\n",
      "Case #74: 7485032700.568781\n",
      "Case #75: 278299344283.800171\n",
      "Case #76: 3485800038115.506348\n",
      "Case #77: 9.424778\n",
      "Case #78: 16955962407.286503\n",
      "Case #79: 140612505092.464294\n",
      "Case #80: 2655801123339.563477\n",
      "Case #81: 1121707127279.863037\n",
      "Case #82: 157428540271.809540\n",
      "Case #83: 270003764100.420746\n",
      "Case #84: 3535658431199.899414\n",
      "Case #85: 4495896394787.738281\n",
      "Case #86: 8108542876.075565\n",
      "Case #87: 1105293769244.909180\n",
      "Case #88: 40329348968.406967\n",
      "Case #89: 7257206591.020529\n",
      "Case #90: 1621211955314.627930\n",
      "Case #91: 529599434127.108948\n",
      "Case #92: 849583418354.321777\n",
      "Case #93: 1806750345529.438232\n",
      "Case #94: 1757375411419.081055\n",
      "Case #95: 8166218145078.676758\n",
      "Case #96: 264493138489.542938\n",
      "Case #97: 3339239188955.880859\n",
      "Case #98: 23053246092.906548\n",
      "Case #99: 9511777297.585485\n",
      "Case #100: 14377307010893.732422\n"
     ]
    }
   ],
   "source": [
    "parse(open(\"C:\\Users\\mheik\\Downloads\\A-large.in\"))"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "metadata": {
    "collapsed": true
   },
   "outputs": [],
   "source": []
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "metadata": {
    "collapsed": true
   },
   "outputs": [],
   "source": []
  }
 ],
 "metadata": {
  "kernelspec": {
   "display_name": "Python [Root]",
   "language": "python",
   "name": "Python [Root]"
  },
  "language_info": {
   "codemirror_mode": {
    "name": "ipython",
    "version": 2
   },
   "file_extension": ".py",
   "mimetype": "text/x-python",
   "name": "python",
   "nbconvert_exporter": "python",
   "pygments_lexer": "ipython2",
   "version": "2.7.12"
  }
 },
 "nbformat": 4,
 "nbformat_minor": 0
}
