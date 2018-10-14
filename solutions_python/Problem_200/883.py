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
    "# Problem B: tidy number\n",
    "def maxTidyNumber(N):\n",
    "    s = map(int, list(str(N)))\n",
    "    n = len(s)\n",
    "    if n == 1:\n",
    "        return str(N)\n",
    "    for i in range(n - 1):\n",
    "        if s[i] <= s[i + 1]:\n",
    "            continue\n",
    "        else:\n",
    "            s[i] -= 1\n",
    "            for j in range(i + 1, n):\n",
    "                s[j] = 9\n",
    "            break\n",
    "    for i in range(n - 1):\n",
    "        if s[n - 1 - i] >= s[n - 1 - i - 1]:\n",
    "            continue\n",
    "        else:\n",
    "            s[n - 1 - i] = 9\n",
    "            s[n - 1 - i - 1] -= 1\n",
    "    if s[0] == 0:\n",
    "        s.remove(s[0])\n",
    "    return ''.join(map(str, s))"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 34,
   "metadata": {
    "collapsed": true
   },
   "outputs": [],
   "source": [
    "ReadPath = \"B-large.in\"\n",
    "WritePath = \"B-large-res.txt\"\n",
    "f = open(ReadPath, 'r')\n",
    "g = open(WritePath, 'w')\n",
    "lineCount = 0\n",
    "for line in f:\n",
    "    if lineCount == 0:\n",
    "        caseNum = int(line.strip())\n",
    "        lineCount += 1\n",
    "    else:\n",
    "        N = line.strip()\n",
    "        g.write(\"Case #\" + str(lineCount) + \": \" + maxTidyNumber(N) + \"\\n\")\n",
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
