{
 "cells": [
  {
   "cell_type": "code",
   "execution_count": null,
   "metadata": {
    "collapsed": true
   },
   "outputs": [],
   "source": [
    "import numpy as np"
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
    "#filePathIn = '/home/gael/Downloads/sample.in'\n",
    "filePathOut = '/home/gael/Downloads/oooooooooooooooooooooout.txt'"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "metadata": {
    "scrolled": true
   },
   "outputs": [],
   "source": [
    "def solveCase(ac, aj, listLine):\n",
    "    print(ac,aj)\n",
    "    c = []\n",
    "    j = []\n",
    "    if ac:\n",
    "        for l in listLine[:ac]:\n",
    "            c += [list(map(lambda x: int(x), l.split()))]\n",
    "    if aj:\n",
    "        for l in listLine[-aj:]:\n",
    "            j += [list(map(lambda x: int(x), l.split()))]\n",
    "    print(c)\n",
    "    print(j)\n",
    "    \n",
    "    n = 0\n",
    "    if 1 in [ac,aj]:\n",
    "        n = 2\n",
    "        \n",
    "    elif 2 in [ac,aj]:\n",
    "        a = sorted(c + j, key=lambda p: p[0])\n",
    "        if a[1][0] - a[0][1] >= 720:\n",
    "            n = 2\n",
    "        elif a[0][0]+1440 - a[1][1] >= 720:\n",
    "            n = 2\n",
    "        else:\n",
    "            n = 4\n",
    "        print('a',a)\n",
    "        \n",
    "    return str(n)\n",
    "    #assert(False)\n",
    "    \n",
    "with open(filePathOut, 'w') as fileOut:\n",
    "    with open(filePathIn, 'r') as fileIn:\n",
    "        case = 0\n",
    "        lines = fileIn.readlines()\n",
    "        i = 0\n",
    "        nC = int(lines[i].strip())\n",
    "        i += 1\n",
    "        while i < len(lines):\n",
    "            l = lines[i].strip()\n",
    "            i += 1\n",
    "            case += 1\n",
    "            print('*'*14,case,'*'*14)\n",
    "            n,m = l.split()\n",
    "            n,m = int(n), int(m)\n",
    "            listLine = []\n",
    "            for lc in range(n+m):\n",
    "                listLine += [lines[i+lc].strip()]\n",
    "            i += n+m\n",
    "            strSolve = str(solveCase(n,m, listLine))\n",
    "            strCase = \"Case #\"+str(case)+\": \"+strSolve\n",
    "            print(strCase[:19])\n",
    "            fileOut.write(strCase+'\\n')\n",
    "        assert(nC == case)"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "metadata": {
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
