{
 "cells": [
  {
   "cell_type": "code",
   "execution_count": 20,
   "metadata": {
    "collapsed": true
   },
   "outputs": [],
   "source": [
    "# Problem A: flip pancake\n",
    "def Flip(s, k):\n",
    "    s = list(s)\n",
    "    n = len(s)\n",
    "    count = 0\n",
    "    for i in range(n):\n",
    "        if s[i] == '+':\n",
    "            continue\n",
    "        if s[i] == '-' and (n - i) < k:\n",
    "            return \"IMPOSSIBLE\"\n",
    "        else:\n",
    "            for j in range(i, i + k):\n",
    "                if s[j] == '+':\n",
    "                    s[j] = '-'\n",
    "                else:\n",
    "                    s[j] = '+'\n",
    "            count += 1\n",
    "    return count  "
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 22,
   "metadata": {
    "collapsed": false
   },
   "outputs": [],
   "source": [
    "# small case:\n",
    "ReadPath =\"A-large.in\"\n",
    "WritePath = \"A-large-res.txt\"\n",
    "f = open(ReadPath)\n",
    "g = open(WritePath, 'w')\n",
    "\n",
    "lineCount = 0\n",
    "for line in f:\n",
    "    if lineCount == 0:\n",
    "        CaseNum = int(line.strip())\n",
    "        lineCount += 1\n",
    "    else:\n",
    "        s, k  = line.strip().split(' ')\n",
    "        k = int(k)\n",
    "        FlipAns = Flip(s, k)\n",
    "        g.write(\"Case #\" + str(lineCount) + \": \" + str(FlipAns) + '\\n')\n",
    "        lineCount += 1\n",
    "g.close()\n",
    "\n"
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
