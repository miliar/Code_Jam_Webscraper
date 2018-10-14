{
 "cells": [
  {
   "cell_type": "code",
   "execution_count": 110,
   "metadata": {
    "collapsed": false
   },
   "outputs": [],
   "source": [
    "def solve(cs,ds):\n",
    "        \n",
    "    alltasks = [(a,b,\"C\") for a,b in cs] + \\\n",
    "                [(a,b,\"D\") for a,b in ds]\n",
    "        \n",
    "    alltasks = sorted(alltasks)\n",
    "    \n",
    "    alltasks.append((alltasks[0][0] + 24*60, alltasks[0][1] + 24*60, alltasks[0][2]))\n",
    "    \n",
    "    cextend = []\n",
    "    dextend = []\n",
    "    swaps = []\n",
    "    for i in range(len(alltasks)-1):\n",
    "        a,b,c = alltasks[i]\n",
    "        d,e,f = alltasks[i+1]\n",
    "        \n",
    "        if c != f:\n",
    "            swaps.append(d-b)\n",
    "        \n",
    "        elif c == \"C\":\n",
    "            cextend.append(d-b)\n",
    "        else:\n",
    "            dextend.append(d-b)\n",
    "    \n",
    "    cmust = sum(b-a for a,b in cs)\n",
    "    dmust = sum(b-a for a,b in ds)\n",
    "    \n",
    "    call = cmust + sum(cextend)\n",
    "    dall = dmust + sum(dextend)\n",
    "    \n",
    "    #make sure cs are smaller\n",
    "    if dall < call:\n",
    "        return solve(ds,cs)\n",
    "    \n",
    "    #print cs\n",
    "    #print ds\n",
    "    #print cmust,cstart,cend,cextend\n",
    "    #print dmust,dstart,dend,dextend\n",
    "    #print swaps\n",
    "\n",
    "    dextend = sorted(dextend, reverse=True)\n",
    "    \n",
    "    for i in range(len(dextend)+1):\n",
    "        #print \"try\", call, sum(swaps), i, sum(dextend[:i]), dstart, dend\n",
    "        if call + sum(swaps) + sum(dextend[:i]) >= 12*60:\n",
    "            return len(swaps) + 2*i\n",
    "\n",
    "    assert(False)"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 111,
   "metadata": {
    "collapsed": true
   },
   "outputs": [],
   "source": [
    "def parse(text):\n",
    "    T = int(text.next())\n",
    "    for i in range(T):\n",
    "        ac, aj = [int(x) for x in text.next().rstrip().split(\" \")]\n",
    "        \n",
    "        cs = []\n",
    "        for j in range(ac):\n",
    "            c,d = [int(x) for x in text.next().rstrip().split(\" \")]\n",
    "            cs.append((c,d))\n",
    "            \n",
    "        \n",
    "        js = []\n",
    "        for j in range(aj):\n",
    "            c,d = [int(x) for x in text.next().rstrip().split(\" \")]\n",
    "            js.append((c,d))\n",
    "          \n",
    "        soln = solve(cs,js)\n",
    "        \n",
    "        print \"Case #%d: %d\" % (i+1, soln)"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 112,
   "metadata": {
    "collapsed": true
   },
   "outputs": [],
   "source": [
    "TEXT = \"\"\"5\n",
    "1 1\n",
    "540 600\n",
    "840 900\n",
    "2 0\n",
    "900 1260\n",
    "180 540\n",
    "1 1\n",
    "1439 1440\n",
    "0 1\n",
    "2 2\n",
    "0 1\n",
    "1439 1440\n",
    "1438 1439\n",
    "1 2\n",
    "3 4\n",
    "0 10\n",
    "1420 1440\n",
    "90 100\n",
    "550 600\n",
    "900 950\n",
    "100 150\n",
    "1050 1400\"\"\""
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 113,
   "metadata": {
    "collapsed": false
   },
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "Case #1: 2\n",
      "Case #2: 4\n",
      "Case #3: 2\n",
      "Case #4: 4\n",
      "Case #5: 6\n"
     ]
    }
   ],
   "source": [
    "parse(x for x in TEXT.splitlines())"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 115,
   "metadata": {
    "collapsed": false
   },
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "Case #1: 2\n",
      "Case #2: 4\n",
      "Case #3: 2\n",
      "Case #4: 2\n",
      "Case #5: 2\n",
      "Case #6: 2\n",
      "Case #7: 4\n",
      "Case #8: 2\n",
      "Case #9: 2\n",
      "Case #10: 2\n",
      "Case #11: 2\n",
      "Case #12: 2\n",
      "Case #13: 2\n",
      "Case #14: 2\n",
      "Case #15: 2\n",
      "Case #16: 2\n",
      "Case #17: 2\n",
      "Case #18: 2\n",
      "Case #19: 2\n",
      "Case #20: 2\n",
      "Case #21: 2\n",
      "Case #22: 2\n",
      "Case #23: 2\n",
      "Case #24: 2\n",
      "Case #25: 2\n",
      "Case #26: 2\n",
      "Case #27: 2\n",
      "Case #28: 2\n",
      "Case #29: 2\n",
      "Case #30: 2\n",
      "Case #31: 2\n",
      "Case #32: 2\n",
      "Case #33: 2\n",
      "Case #34: 4\n",
      "Case #35: 4\n",
      "Case #36: 4\n",
      "Case #37: 2\n",
      "Case #38: 2\n",
      "Case #39: 2\n",
      "Case #40: 4\n",
      "Case #41: 2\n",
      "Case #42: 2\n",
      "Case #43: 2\n",
      "Case #44: 4\n",
      "Case #45: 4\n",
      "Case #46: 2\n",
      "Case #47: 2\n",
      "Case #48: 2\n",
      "Case #49: 2\n",
      "Case #50: 2\n",
      "Case #51: 2\n",
      "Case #52: 2\n",
      "Case #53: 2\n",
      "Case #54: 4\n",
      "Case #55: 2\n",
      "Case #56: 2\n",
      "Case #57: 2\n",
      "Case #58: 2\n",
      "Case #59: 4\n",
      "Case #60: 2\n",
      "Case #61: 4\n",
      "Case #62: 4\n",
      "Case #63: 4\n",
      "Case #64: 4\n",
      "Case #65: 2\n",
      "Case #66: 2\n",
      "Case #67: 2\n",
      "Case #68: 2\n",
      "Case #69: 2\n",
      "Case #70: 2\n",
      "Case #71: 2\n",
      "Case #72: 2\n",
      "Case #73: 2\n",
      "Case #74: 2\n",
      "Case #75: 2\n",
      "Case #76: 2\n",
      "Case #77: 2\n",
      "Case #78: 2\n",
      "Case #79: 2\n",
      "Case #80: 4\n",
      "Case #81: 2\n",
      "Case #82: 2\n",
      "Case #83: 2\n",
      "Case #84: 2\n",
      "Case #85: 4\n",
      "Case #86: 2\n",
      "Case #87: 2\n",
      "Case #88: 2\n",
      "Case #89: 2\n",
      "Case #90: 2\n",
      "Case #91: 2\n",
      "Case #92: 4\n",
      "Case #93: 4\n",
      "Case #94: 2\n",
      "Case #95: 2\n",
      "Case #96: 2\n",
      "Case #97: 2\n",
      "Case #98: 2\n",
      "Case #99: 2\n",
      "Case #100: 2\n"
     ]
    }
   ],
   "source": [
    "parse(open(\"C:\\Users\\mheik\\Downloads\\B-small-attempt1.in\"))"
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
