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
    "class MinMax:\n",
    "    def __init__(self, fromNum):\n",
    "        self.max = fromNum // 2\n",
    "        self.min = fromNum - self.max - 1\n",
    "        self.num = 0\n",
    "        #print(\"new \", fromNum,\"->\", self.__repr__())\n",
    "    def __repr__(self):\n",
    "        return str(self.max)+\" \"+str(self.min)\n",
    "    def __eq__(self, another):\n",
    "        return self.min == another.min and self.max == another.max\n",
    "    def __hash__(self):\n",
    "        return hash(self.__repr__())\n",
    "    def __gt__(self, other):\n",
    "        return self.min < other.min or self.max < other.max\n",
    "\n",
    "mm = MinMax(8)\n",
    "diccc = {mm:5}\n",
    "print(diccc)\n",
    "diccc[mm] += 2\n",
    "print(diccc)\n",
    "mmm = MinMax(8)\n",
    "diccc[mmm] += 2\n",
    "print(diccc)\n",
    "\n",
    "def solveCase(l):\n",
    "    n,k = l.split()\n",
    "    n,k = int(n), int(k)\n",
    "    def isEven(num):\n",
    "        return 1 - num % 2\n",
    "    \n",
    "    print(n,k)\n",
    "    mm = MinMax(1)\n",
    "    mm.max = n\n",
    "    \n",
    "    levels = [{mm:1}]\n",
    "    for ll in range(999):\n",
    "        levels += [dict()]\n",
    "    i = 0\n",
    "    allFull = False\n",
    "    while (not allFull and i < len(levels)):\n",
    "        dici = levels[i]\n",
    "        nextDic = levels[i+1]\n",
    "        allFull = True\n",
    "        for key,val in dici.items():\n",
    "            #print(i,\" key,val\",key,':',val)\n",
    "            for tm in [key.max, key.min]:\n",
    "                if tm < 1:\n",
    "                    break\n",
    "                allFull = False\n",
    "                #print(\"dici\",dici,\"nextDic\",nextDic)\n",
    "                neMM = MinMax(tm)\n",
    "                oldVal = nextDic.get(neMM, 0)\n",
    "                nextDic[neMM] = oldVal + val\n",
    "                #print(\"dici\",dici,\"nextDic\",nextDic)\n",
    "        if allFull:\n",
    "            break\n",
    "        i += 1        \n",
    "        #print(levels[:i+1])\n",
    "    levels = levels[1:]\n",
    "    print(i)\n",
    "    #print(levels[:i])\n",
    "    for j in range(i):\n",
    "        #print(levels[j])\n",
    "        for key,val in sorted(levels[j].items()):\n",
    "            k -= val\n",
    "            print(j,\" key,val\",key,':',val,' k->',k)\n",
    "            if k <= 0:\n",
    "                return key\n",
    "    assert(False)\n",
    "    \n",
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
    "            print('*'*14,case,'*'*14)\n",
    "            strSolve = str(solveCase(l))\n",
    "            strCase = \"Case #\"+str(case)+\": \"+strSolve\n",
    "            print(strCase)\n",
    "            fileOut.write(strCase+'\\n')\n",
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
