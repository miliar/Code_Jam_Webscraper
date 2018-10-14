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
    "def parse(text):\n",
    "    T = int(text.next())\n",
    "    for i in range(T):\n",
    "        N, Q = [int(x) for x in text.next().split(\" \")]\n",
    "        \n",
    "        horses = []\n",
    "        for j in range(N):\n",
    "            horses.append([int(x) for x in text.next().split(\" \")])\n",
    "        \n",
    "        routes = []\n",
    "        for j in range(N):\n",
    "            routes.append([int(x) for x in text.next().split(\" \")])\n",
    "            \n",
    "        pairs = []\n",
    "        for k in range(Q):\n",
    "            pairs.append([int(x) for x in text.next().split(\" \")])\n",
    "            \n",
    "        res = solve(horses, routes, pairs)\n",
    "        \n",
    "        print \"Case #%d: %s\" % (i+1, \" \".join([str(x) for x in res]))"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 25,
   "metadata": {
    "collapsed": false
   },
   "outputs": [],
   "source": [
    "def solve(horses, routes, pairs):\n",
    "    \n",
    "    #print \"new\", horses, routes, pairs\n",
    "    \n",
    "    def city(dist, speed, start, end):\n",
    "        #print dist, speed, start, end\n",
    "        \n",
    "        if start == end:\n",
    "            return 0\n",
    "        \n",
    "        nextdist = routes[start][start+1]\n",
    "        \n",
    "        best = None\n",
    "        \n",
    "        #keep horse\n",
    "        if dist >= nextdist:\n",
    "            res = city(dist-nextdist, speed, start+1, end) \n",
    "            if res is not None:\n",
    "                best = 1.0*nextdist/speed + res\n",
    "        \n",
    "        #new horse\n",
    "        newdist, newspeed = horses[start]\n",
    "        if newdist >= nextdist:    \n",
    "            res = city(newdist-nextdist, newspeed, start+1, end) \n",
    "            if res is not None:\n",
    "                res += 1.0*nextdist/newspeed\n",
    "                \n",
    "                if best is None or res < best:\n",
    "                    best = res\n",
    "                    \n",
    "        return best\n",
    "        \n",
    "    soln = []\n",
    "    for start, end in pairs:\n",
    "        soln.append(city(0,0,start-1, end-1))\n",
    "            \n",
    "    return soln\n"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 26,
   "metadata": {
    "collapsed": false
   },
   "outputs": [],
   "source": [
    "TEXT=\"\"\"2\n",
    "3 1\n",
    "2 3\n",
    "2 4\n",
    "4 4\n",
    "-1 1 -1\n",
    "-1 -1 1\n",
    "-1 -1 -1\n",
    "1 3\n",
    "4 1\n",
    "13 10\n",
    "1 1000\n",
    "10 8\n",
    "5 5\n",
    "-1 1 -1 -1\n",
    "-1 -1 1 -1\n",
    "-1 -1 -1 10\n",
    "-1 -1 -1 -1\n",
    "1 4\n",
    "4 3\n",
    "30 60\n",
    "10 1000\n",
    "12 5\n",
    "20 1\n",
    "-1 10 -1 31\n",
    "10 -1 10 -1\n",
    "-1 -1 -1 10\n",
    "15 6 -1 -1\n",
    "2 4\n",
    "3 1\n",
    "3 2\"\"\""
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 27,
   "metadata": {
    "collapsed": false
   },
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "Case #1: 0.583333333333\n",
      "Case #2: 1.2\n"
     ]
    }
   ],
   "source": [
    "parse(x for x in TEXT.splitlines())"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 28,
   "metadata": {
    "collapsed": false
   },
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "Case #1: 0.583333333333\n",
      "Case #2: 1.2\n",
      "Case #3: 77.7352413088\n",
      "Case #4: 1.83333333333\n",
      "Case #5: 310.784980405\n",
      "Case #6: 94.6686353536\n",
      "Case #7: 161.911504388\n",
      "Case #8: 64.6711897286\n",
      "Case #9: 56.6159654551\n",
      "Case #10: 167.601612317\n",
      "Case #11: 289.363399824\n",
      "Case #12: 1.0\n",
      "Case #13: 3.2\n",
      "Case #14: 82.690852868\n",
      "Case #15: 101.471574606\n",
      "Case #16: 106.185458448\n",
      "Case #17: 251.390768713\n",
      "Case #18: 465.401615186\n",
      "Case #19: 57.9020270816\n",
      "Case #20: 834.77678854\n",
      "Case #21: 224.334700331\n",
      "Case #22: 97.0147399731\n",
      "Case #23: 72.2325200613\n",
      "Case #24: 122.241101109\n",
      "Case #25: 56.2364891089\n",
      "Case #26: 220.665667013\n",
      "Case #27: 101.52516075\n",
      "Case #28: 987.028173694\n",
      "Case #29: 88.1754742551\n",
      "Case #30: 46.5797614597\n",
      "Case #31: 587.957931676\n",
      "Case #32: 168.406496605\n",
      "Case #33: 154.629486993\n",
      "Case #34: 122.978159196\n",
      "Case #35: 90.6839432556\n",
      "Case #36: 57.906526687\n",
      "Case #37: 62.6723497437\n",
      "Case #38: 74.7673621548\n",
      "Case #39: 189.962020972\n",
      "Case #40: 156.415087448\n",
      "Case #41: 46.1758085831\n",
      "Case #42: 0.666666666667\n",
      "Case #43: 99000000000.0\n",
      "Case #44: 131538173.571\n",
      "Case #45: 13681654.7535\n",
      "Case #46: 1.0\n",
      "Case #47: 106.272223053\n",
      "Case #48: 1841.29885255\n",
      "Case #49: 0.5\n",
      "Case #50: 75.7160804873\n",
      "Case #51: 103.603916593\n",
      "Case #52: 92.9749701097\n",
      "Case #53: 140.390681004\n",
      "Case #54: 95.4247949112\n",
      "Case #55: 88.662949663\n",
      "Case #56: 57.05716608\n",
      "Case #57: 66.8020769845\n",
      "Case #58: 72.324423113\n",
      "Case #59: 143.850940831\n",
      "Case #60: 1.5\n",
      "Case #61: 91.7234505458\n",
      "Case #62: 315.718639543\n",
      "Case #63: 64.4018103783\n",
      "Case #64: 177.444643705\n",
      "Case #65: 242.383171309\n",
      "Case #66: 432.203492918\n",
      "Case #67: 70.618765718\n",
      "Case #68: 349.302747691\n",
      "Case #69: 177.278115624\n",
      "Case #70: 86.0918521411\n",
      "Case #71: 529.47147206\n",
      "Case #72: 59.7778136542\n",
      "Case #73: 653.457305453\n",
      "Case #74: 86.5100535141\n",
      "Case #75: 57.8344537042\n",
      "Case #76: 211.618614567\n",
      "Case #77: 151.434531978\n",
      "Case #78: 56.2595334247\n",
      "Case #79: 282.453494809\n",
      "Case #80: 195664312.486\n",
      "Case #81: 130.363849116\n",
      "Case #82: 161149017.106\n",
      "Case #83: 162.87745044\n",
      "Case #84: 98499999999.5\n",
      "Case #85: 88.6087583776\n",
      "Case #86: 86.3309706039\n",
      "Case #87: 143.406400253\n",
      "Case #88: 50.0329643781\n",
      "Case #89: 55972964.2908\n",
      "Case #90: 58786324.8562\n",
      "Case #91: 161.518688139\n",
      "Case #92: 331055757.501\n",
      "Case #93: 192.765936703\n",
      "Case #94: 77.3318621965\n",
      "Case #95: 37684063.7695\n",
      "Case #96: 92.5597555727\n",
      "Case #97: 3.2\n",
      "Case #98: 1.5\n",
      "Case #99: 199.240713647\n"
     ]
    }
   ],
   "source": [
    "parse(open(\"C:\\Users\\mheik\\Downloads\\C-small-attempt0.in\"))"
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
