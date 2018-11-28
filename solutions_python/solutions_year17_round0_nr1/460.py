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
    "filePathIn = '/home/gael/Downloads/A-large.in'\n",
    "filePathOut = '/home/gael/Downloads/A-large-out.txt'"
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
    "    pms,k = l.split()\n",
    "    k = int(k)\n",
    "    pm = []\n",
    "    for i in range(len(pms)):\n",
    "        pm.append(1 if pms[i] == '+' else -1)\n",
    "    print(pm,k)\n",
    "    flips = 0\n",
    "    for i in range(len(pm)+1-k):\n",
    "        #print(i)\n",
    "        if pm[i] < 0:\n",
    "            flips += 1\n",
    "            for j in range(k):\n",
    "                pm[i+j] *= -1\n",
    "    if pm[-k:] == [1] * len(pm[-k:]):\n",
    "        print(flips,pm)\n",
    "        return(flips)\n",
    "    return 'IMPOSSIBLE'"
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
    "    ins += [l.strip()[:50]]\n",
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
