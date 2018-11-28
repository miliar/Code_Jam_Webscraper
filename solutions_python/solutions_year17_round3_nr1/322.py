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
    "filePathIn = '/home/gael/Downloads/A-large.in'\n",
    "#filePathIn = '/home/gael/Downloads/A-small-attempt0 (1).in'\n",
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
    "\n",
    "def solveCase(n, k, listLine):\n",
    "    def area(ps):\n",
    "        ps = sorted(ps, key=lambda p: -p[0])\n",
    "        v = 0\n",
    "        for p in ps:\n",
    "            v += p[1]\n",
    "        v += ps[0][0]\n",
    "        return v\n",
    "    print(n,k)\n",
    "    arr = np.full((n,2),0).astype(int)\n",
    "    prh = []\n",
    "    for l in listLine:\n",
    "        r,h = l.split()\n",
    "        r = int(r)\n",
    "        h = int(h)\n",
    "        prh += [[np.pi * r * r, 2 * np.pi * r * h, h]]\n",
    "\n",
    "    print(prh)\n",
    "    prh = sorted(prh, key=lambda p: -p[1])\n",
    "    krh = prh[:k]\n",
    "    \n",
    "    hrh = prh[k:]\n",
    "    print(krh)\n",
    "    print(hrh)\n",
    "\n",
    "    vmax = area(krh)\n",
    "    if k > -1:\n",
    "        for i in range(n-k):\n",
    "            vmax = max(vmax, area([hrh[i]] + krh[:-1]))\n",
    "  \n",
    "    return str(vmax)\n",
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
    "            for lc in range(n):\n",
    "                listLine += [lines[i+lc].strip()]\n",
    "            i += n\n",
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
