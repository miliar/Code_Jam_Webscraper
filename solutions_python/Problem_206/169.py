{
 "cells": [
  {
   "cell_type": "markdown",
   "metadata": {},
   "source": [
    "# Steed 2: Cruise Control"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 13,
   "metadata": {
    "collapsed": false
   },
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "loading functions done\n",
      "loading data done\n",
      "number of cases -  99\n",
      "1 / 99\n",
      "2 / 99\n",
      "3 / 99\n",
      "4 / 99\n",
      "5 / 99\n",
      "6 / 99\n",
      "7 / 99\n",
      "8 / 99\n",
      "9 / 99\n",
      "10 / 99\n",
      "11 / 99\n",
      "12 / 99\n",
      "13 / 99\n",
      "14 / 99\n",
      "15 / 99\n",
      "16 / 99\n",
      "17 / 99\n",
      "18 / 99\n",
      "19 / 99\n",
      "20 / 99\n",
      "21 / 99\n",
      "22 / 99\n",
      "23 / 99\n",
      "24 / 99\n",
      "25 / 99\n",
      "26 / 99\n",
      "27 / 99\n",
      "28 / 99\n",
      "29 / 99\n",
      "30 / 99\n",
      "31 / 99\n",
      "32 / 99\n",
      "33 / 99\n",
      "34 / 99\n",
      "35 / 99\n",
      "36 / 99\n",
      "37 / 99\n",
      "38 / 99\n",
      "39 / 99\n",
      "40 / 99\n",
      "41 / 99\n",
      "42 / 99\n",
      "43 / 99\n",
      "44 / 99\n",
      "45 / 99\n",
      "46 / 99\n",
      "47 / 99\n",
      "48 / 99\n",
      "49 / 99\n",
      "50 / 99\n",
      "51 / 99\n",
      "52 / 99\n",
      "53 / 99\n",
      "54 / 99\n",
      "55 / 99\n",
      "56 / 99\n",
      "57 / 99\n",
      "58 / 99\n",
      "59 / 99\n",
      "60 / 99\n",
      "61 / 99\n",
      "62 / 99\n",
      "63 / 99\n",
      "64 / 99\n",
      "65 / 99\n",
      "66 / 99\n",
      "67 / 99\n",
      "68 / 99\n",
      "69 / 99\n",
      "70 / 99\n",
      "71 / 99\n",
      "72 / 99\n",
      "73 / 99\n",
      "74 / 99\n",
      "75 / 99\n",
      "76 / 99\n",
      "77 / 99\n",
      "78 / 99\n",
      "79 / 99\n",
      "80 / 99\n",
      "81 / 99\n",
      "82 / 99\n",
      "83 / 99\n",
      "84 / 99\n",
      "85 / 99\n",
      "86 / 99\n",
      "87 / 99\n",
      "88 / 99\n",
      "89 / 99\n",
      "90 / 99\n",
      "91 / 99\n",
      "92 / 99\n",
      "93 / 99\n",
      "94 / 99\n",
      "95 / 99\n",
      "96 / 99\n",
      "97 / 99\n",
      "98 / 99\n",
      "99 / 99\n",
      "saving data\n"
     ]
    }
   ],
   "source": [
    "from copy import deepcopy\n",
    "import numpy as np\n",
    "from math import floor, ceil\n",
    "\n",
    "def solve_a(d,n,h):\n",
    "    cur_h = 0\n",
    "    for x in range(len(h),1):\n",
    "        a1 = h[x][1]\n",
    "        b1 = h[x][0]\n",
    "        a2 = h[cur_h][1]\n",
    "        b2 = h[cur_h][0]\n",
    "        t = (b2 - b1) / float(a1 - a2)\n",
    "        p = a1 * t + b1\n",
    "        if p >= d:\n",
    "            continue\n",
    "        cur_h = x\n",
    "    t = (d - h[cur_h][0]) / float(h[cur_h][1])\n",
    "    return h[cur_h][1] + h[cur_h][0] / t\n",
    "\n",
    "def solve_a2(d,n,h):\n",
    "    s = map(lambda a: d/((d-a[0])/float(a[1])),h)\n",
    "    return min(s)\n",
    "    \n",
    "print 'loading functions done'\n",
    "\n",
    "with open('round B/A-large.in', 'r') as f:\n",
    "    data = f.readlines()\n",
    "print 'loading data done'\n",
    "\n",
    "out = ''\n",
    "total_cases = int(data[0])\n",
    "print 'number of cases - ', total_cases\n",
    "counter = 1\n",
    "for cur_case in range(total_cases):\n",
    "    print cur_case + 1, '/', total_cases\n",
    "    # computation\n",
    "    l = data[counter].strip().split(' ')\n",
    "    d = int(l[0])\n",
    "    n = int(l[1])\n",
    "    counter += 1\n",
    "    h = map(lambda line: map(int, line.split(' ')), data[counter:counter+n])\n",
    "    h.sort(lambda x,y: x[0] - y[0])\n",
    "    counter += n\n",
    "#     print d,n,h\n",
    "    res = solve_a2(d,n,h)\n",
    "#     print res\n",
    "    out += 'Case #%d: %0.6f\\n' % (cur_case + 1, res)\n",
    "    \n",
    "print 'saving data'\n",
    "with open('round B/outputA_large.txt', 'w') as f:\n",
    "    f.write(out)"
   ]
  },
  {
   "cell_type": "markdown",
   "metadata": {},
   "source": [
    "# B"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 4,
   "metadata": {
    "collapsed": false,
    "scrolled": true
   },
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "loading functions done\n",
      "loading data done\n",
      "number of cases -  3\n",
      "1 / 3\n",
      "2 / 3\n",
      "3 / 3\n",
      "saving data\n"
     ]
    }
   ],
   "source": [
    "from copy import deepcopy\n",
    "import numpy as np\n",
    "from math import floor, ceil\n",
    "\n",
    "print 'loading functions done'\n",
    "\n",
    "with open('round B/inputB.txt', 'r') as f:\n",
    "    data = f.readlines()\n",
    "print 'loading data done'\n",
    "\n",
    "out = ''\n",
    "total_cases = int(data[0])\n",
    "print 'number of cases - ', total_cases\n",
    "for cur_case in range(total_cases):\n",
    "    print cur_case + 1, '/', total_cases\n",
    "    # computation\n",
    "    out += 'Case #%d:\\n' % (cur_case + 1)\n",
    "    \n",
    "print 'saving data'\n",
    "with open('round B/outputB.txt', 'w') as f:\n",
    "    f.write(out)"
   ]
  },
  {
   "cell_type": "markdown",
   "metadata": {},
   "source": [
    "# C"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 5,
   "metadata": {
    "collapsed": false
   },
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "loading functions done\n",
      "loading data done\n",
      "number of cases -  3\n",
      "1 / 3\n",
      "2 / 3\n",
      "3 / 3\n",
      "saving data\n"
     ]
    }
   ],
   "source": [
    "from copy import deepcopy\n",
    "import numpy as np\n",
    "from math import floor, ceil\n",
    "\n",
    "print 'loading functions done'\n",
    "\n",
    "with open('round B/inputC.txt', 'r') as f:\n",
    "    data = f.readlines()\n",
    "print 'loading data done'\n",
    "\n",
    "out = ''\n",
    "total_cases = int(data[0])\n",
    "print 'number of cases - ', total_cases\n",
    "for cur_case in range(total_cases):\n",
    "    print cur_case + 1, '/', total_cases\n",
    "    # computation\n",
    "    out += 'Case #%d:\\n' % (cur_case + 1)\n",
    "    \n",
    "print 'saving data'\n",
    "with open('round B/outputC.txt', 'w') as f:\n",
    "    f.write(out)"
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
 "nbformat_minor": 2
}
