{
 "cells": [
  {
   "cell_type": "code",
   "execution_count": 241,
   "metadata": {
    "collapsed": true
   },
   "outputs": [],
   "source": [
    "def tidyNumbers(N):\n",
    "    N = list(str(N))\n",
    "    if N == sorted(N):\n",
    "        return ''.join(N)\n",
    "    for i in range(1, len(N)):\n",
    "        if N[i] == '0' or N[i] < N[i - 1]:\n",
    "            N[i - 1] = str(int(N[i- 1]) - 1)\n",
    "            return tidyNumbers(int(''.join(N[0:i] + ['9'] * (len(N) - i))))"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 249,
   "metadata": {
    "collapsed": true
   },
   "outputs": [],
   "source": [
    "inp = open(\"B-large.in\")\n",
    "#inp = open(\"test.txt\")\n",
    "out = open(\"output.txt\", 'w')\n",
    "num = int(inp.readline())\n",
    "for i in range(num):\n",
    "    N = int(inp.readline())\n",
    "    out.write('Case #' + str(i+1) + ': ' + tidyNumbers(N) + '\\n')\n",
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
