{
 "cells": [
  {
   "cell_type": "code",
   "execution_count": 14,
   "metadata": {
    "collapsed": true
   },
   "outputs": [],
   "source": [
    "# Problem C: Bathroom Stall\n",
    "def chooseMyStall(N, k):\n",
    "    available = dict()\n",
    "    available[N] = 1\n",
    "    for i in range(k):\n",
    "        maxRange = max(available.keys())\n",
    "        myRangeLen = maxRange - 1 # 1 is for me\n",
    "        minSpan = myRangeLen / 2\n",
    "        maxSpan = myRangeLen - minSpan\n",
    "        available[maxRange] -= 1\n",
    "        if available[maxRange] == 0: \n",
    "            del available[maxRange]\n",
    "        if minSpan not in available:\n",
    "            available[minSpan] = 0\n",
    "        available[minSpan] += 1\n",
    "        if maxSpan not in available:\n",
    "            available[maxSpan] = 0\n",
    "        available[maxSpan] += 1\n",
    "    return (maxSpan, minSpan)"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 28,
   "metadata": {
    "collapsed": false
   },
   "outputs": [],
   "source": [
    "ReadPath = \"C-small-2-attempt0.in\"\n",
    "WritePath = \"C-small-2-attempt0-res.txt\"\n",
    "f = open(ReadPath, 'r')\n",
    "g = open(WritePath, 'w')\n",
    "lineCount = 0\n",
    "\n",
    "for line in f:\n",
    "    if lineCount == 0:\n",
    "        caseNum = int(line.strip())\n",
    "        lineCount += 1\n",
    "    else:\n",
    "        N, k = line.strip().split(' ')\n",
    "        N = int(N)\n",
    "        k = int(k)\n",
    "        maxSpan, minSpan = chooseMyStall(N, k)\n",
    "        g.write(\"Case #\" + str(lineCount) + \": \" + str(maxSpan) + \" \" + str(minSpan) + \"\\n\")\n",
    "        lineCount += 1\n",
    "g.close()"
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
   "display_name": "Python 2",
   "language": "python",
   "name": "python2"
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
   "version": "2.7.11"
  }
 },
 "nbformat": 4,
 "nbformat_minor": 0
}
