{
 "cells": [
  {
   "cell_type": "code",
   "execution_count": null,
   "metadata": {
    "collapsed": false
   },
   "outputs": [],
   "source": [
    "#import math"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "metadata": {
    "collapsed": true
   },
   "outputs": [],
   "source": [
    "filePathIn = '/home/gael/Downloads/B-large.in'\n",
    "filePathIn = '/home/gael/Downloads/B-small-attempt0.in'\n",
    "filePathIn = '/home/gael/Downloads/sample.in'\n",
    "filePathOut = '/home/gael/Downloads/oooooooooooooooooooooout.txt'"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "metadata": {
    "collapsed": false
   },
   "outputs": [],
   "source": [
    "def solveCase(l):\n",
    "    pm = []\n",
    "    for i in range(len(l)):\n",
    "        pm.append(int(l[i]))\n",
    "    print(pm)\n",
    "    for i in range(len(pm)-1)[::-1]:\n",
    "        if pm[i] <= pm[i+1]:\n",
    "            continue\n",
    "        print(pm[i:i+2])\n",
    "        pm[i] -= 1\n",
    "        pm[i+1:] = [9] * len(pm[i+1:])\n",
    "    s = ''\n",
    "    for i in range(len(pm)):\n",
    "        assert(pm[i] >= 0)\n",
    "        s += str(pm[i])\n",
    "    return int(s)"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "metadata": {
    "collapsed": false
   },
   "outputs": [],
   "source": [
    "with open(filePathOut, 'w') as fileOut:\n",
    "    with open(filePathIn, 'r') as fileIn:\n",
    "        n = -1\n",
    "        case = 0\n",
    "        for l in fileIn:\n",
    "            l = l.strip()\n",
    "            if n < 0:\n",
    "                n = int(l)\n",
    "                print(n)\n",
    "                continue\n",
    "            case += 1\n",
    "            fileOut.write(\"Case #\"+str(case)+\": \"+str(solveCase(l))+'\\n')\n",
    "        assert(n == case)"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "metadata": {
    "collapsed": false,
    "scrolled": true
   },
   "outputs": [],
   "source": [
    "ins = []\n",
    "outs = [' ']\n",
    "for l in open(filePathIn,'r'):\n",
    "    ins += [l.strip()[:1550]]\n",
    "for l in open(filePathOut,'r'):\n",
    "    outs += [l.strip()]\n",
    "#print(outs)\n",
    "for check in zip(*[ins,outs]):\n",
    "    print(check)"
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
   "display_name": "Python [default]",
   "language": "python",
   "name": "python3"
  },
  "language_info": {
   "codemirror_mode": {
    "name": "ipython",
    "version": 3
   },
   "file_extension": ".py",
   "mimetype": "text/x-python",
   "name": "python",
   "nbconvert_exporter": "python",
   "pygments_lexer": "ipython3",
   "version": "3.5.2"
  }
 },
 "nbformat": 4,
 "nbformat_minor": 2
}
