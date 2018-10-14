{
 "cells": [
  {
   "cell_type": "code",
   "execution_count": 24,
   "metadata": {
    "collapsed": true
   },
   "outputs": [],
   "source": [
    "def oversizedPancakeFlipper(pancakes, K):\n",
    "    pancakes = list(pancakes)\n",
    "    if '-' not in pancakes:\n",
    "        return '0'\n",
    "    flips = 0\n",
    "    for i in range(len(pancakes) - K + 1):\n",
    "        if pancakes[i] == '+':\n",
    "            continue\n",
    "        flips += 1\n",
    "        for j in range(K):\n",
    "            if pancakes[i + j] == '-':\n",
    "                pancakes[i + j] = '+'\n",
    "            else:\n",
    "                pancakes[i + j] = '-'\n",
    "    if '-' in pancakes:\n",
    "        return 'IMPOSSIBLE'\n",
    "    return str(flips)"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 25,
   "metadata": {
    "collapsed": false
   },
   "outputs": [
    {
     "data": {
      "text/plain": [
       "'IMPOSSIBLE'"
      ]
     },
     "execution_count": 25,
     "metadata": {},
     "output_type": "execute_result"
    }
   ],
   "source": [
    "oversizedPancakeFlipper('-+-+-', 4)"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 27,
   "metadata": {
    "collapsed": false
   },
   "outputs": [],
   "source": [
    "inp = open(\"A-small-attempt0.in\")\n",
    "#inp = open(\"test.txt\")\n",
    "out = open(\"output.txt\", 'w')\n",
    "num = int(inp.readline())\n",
    "for i in range(num):\n",
    "    pancakes, K = inp.readline().split(' ')\n",
    "    K = int(K)\n",
    "    out.write('Case #' + str(i+1) + ': ' + oversizedPancakeFlipper(pancakes, K) + '\\n')\n",
    "inp.close()\n",
    "out.close()"
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
   "version": "2.7.13"
  }
 },
 "nbformat": 4,
 "nbformat_minor": 0
}
