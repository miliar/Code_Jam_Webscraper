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
   "execution_count": 14,
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
      "number of cases -  100\n",
      "1 / 100\n",
      "2 / 100\n",
      "3 / 100\n",
      "4 / 100\n",
      "5 / 100\n",
      "6 / 100\n",
      "7 / 100\n",
      "8 / 100\n",
      "9 / 100\n",
      "10 / 100\n",
      "11 / 100\n",
      "12 / 100\n",
      "13 / 100\n",
      "14 / 100\n",
      "15 / 100\n",
      "16 / 100\n",
      "17 / 100\n",
      "18 / 100\n",
      "19 / 100\n",
      "20 / 100\n",
      "21 / 100\n",
      "22 / 100\n",
      "23 / 100\n",
      "24 / 100\n",
      "25 / 100\n",
      "26 / 100\n",
      "27 / 100\n",
      "28 / 100\n",
      "29 / 100\n",
      "30 / 100\n",
      "31 / 100\n",
      "32 / 100\n",
      "33 / 100\n",
      "34 / 100\n",
      "35 / 100\n",
      "36 / 100\n",
      "37 / 100\n",
      "38 / 100\n",
      "39 / 100\n",
      "40 / 100\n",
      "41 / 100\n",
      "42 / 100\n",
      "43 / 100\n",
      "44 / 100\n",
      "45 / 100\n",
      "46 / 100\n",
      "47 / 100\n",
      "48 / 100\n",
      "49 / 100\n",
      "50 / 100\n",
      "51 / 100\n",
      "52 / 100\n",
      "53 / 100\n",
      "54 / 100\n",
      "55 / 100\n",
      "56 / 100\n",
      "57 / 100\n",
      "58 / 100\n",
      "59 / 100\n",
      "60 / 100\n",
      "61 / 100\n",
      "62 / 100\n",
      "63 / 100\n",
      "64 / 100\n",
      "65 / 100\n",
      "66 / 100\n",
      "67 / 100\n",
      "68 / 100\n",
      "69 / 100\n",
      "70 / 100\n",
      "71 / 100\n",
      "72 / 100\n",
      "73 / 100\n",
      "74 / 100\n",
      "75 / 100\n",
      "76 / 100\n",
      "77 / 100\n",
      "78 / 100\n",
      "79 / 100\n",
      "80 / 100\n",
      "81 / 100\n",
      "82 / 100\n",
      "83 / 100\n",
      "84 / 100\n",
      "85 / 100\n",
      "86 / 100\n",
      "87 / 100\n",
      "88 / 100\n",
      "89 / 100\n",
      "90 / 100\n",
      "91 / 100\n",
      "92 / 100\n",
      "93 / 100\n",
      "94 / 100\n",
      "95 / 100\n",
      "96 / 100\n",
      "97 / 100\n",
      "98 / 100\n",
      "99 / 100\n",
      "100 / 100\n",
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
    "# Stable Neigh-bors"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 42,
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
      "number of cases -  100\n",
      "1 / 100\n",
      "2 / 100\n",
      "3 / 100\n",
      "4 / 100\n",
      "5 / 100\n",
      "6 / 100\n",
      "7 / 100\n"
     ]
    },
    {
     "ename": "IndexError",
     "evalue": "string index out of range",
     "output_type": "error",
     "traceback": [
      "\u001b[0;31m---------------------------------------------------------------------------\u001b[0m",
      "\u001b[0;31mIndexError\u001b[0m                                Traceback (most recent call last)",
      "\u001b[0;32m<ipython-input-42-85adae130dcc>\u001b[0m in \u001b[0;36m<module>\u001b[0;34m()\u001b[0m\n\u001b[1;32m     79\u001b[0m     \u001b[0;32mprint\u001b[0m \u001b[0mcur_case\u001b[0m \u001b[0;34m+\u001b[0m \u001b[0;36m1\u001b[0m\u001b[0;34m,\u001b[0m \u001b[0;34m'/'\u001b[0m\u001b[0;34m,\u001b[0m \u001b[0mtotal_cases\u001b[0m\u001b[0;34m\u001b[0m\u001b[0m\n\u001b[1;32m     80\u001b[0m     \u001b[0ml\u001b[0m \u001b[0;34m=\u001b[0m \u001b[0mdata\u001b[0m\u001b[0;34m[\u001b[0m\u001b[0mcounter\u001b[0m\u001b[0;34m]\u001b[0m\u001b[0;34m.\u001b[0m\u001b[0mstrip\u001b[0m\u001b[0;34m(\u001b[0m\u001b[0;34m)\u001b[0m\u001b[0;34m.\u001b[0m\u001b[0msplit\u001b[0m\u001b[0;34m(\u001b[0m\u001b[0;34m' '\u001b[0m\u001b[0;34m)\u001b[0m\u001b[0;34m\u001b[0m\u001b[0m\n\u001b[0;32m---> 81\u001b[0;31m     \u001b[0mres\u001b[0m \u001b[0;34m=\u001b[0m \u001b[0msolve_b\u001b[0m\u001b[0;34m(\u001b[0m\u001b[0ml\u001b[0m\u001b[0;34m)\u001b[0m\u001b[0;34m\u001b[0m\u001b[0m\n\u001b[0m\u001b[1;32m     82\u001b[0m \u001b[0;31m#     print res\u001b[0m\u001b[0;34m\u001b[0m\u001b[0;34m\u001b[0m\u001b[0m\n\u001b[1;32m     83\u001b[0m     \u001b[0mcounter\u001b[0m \u001b[0;34m+=\u001b[0m \u001b[0;36m1\u001b[0m\u001b[0;34m\u001b[0m\u001b[0m\n",
      "\u001b[0;32m<ipython-input-42-85adae130dcc>\u001b[0m in \u001b[0;36msolve_b\u001b[0;34m(l)\u001b[0m\n\u001b[1;32m     36\u001b[0m                 \u001b[0;32mif\u001b[0m \u001b[0mres\u001b[0m \u001b[0;32mand\u001b[0m \u001b[0mres\u001b[0m\u001b[0;34m[\u001b[0m\u001b[0;34m-\u001b[0m\u001b[0;36m1\u001b[0m\u001b[0;34m]\u001b[0m \u001b[0;34m==\u001b[0m \u001b[0mres\u001b[0m\u001b[0;34m[\u001b[0m\u001b[0;36m0\u001b[0m\u001b[0;34m]\u001b[0m \u001b[0;32mand\u001b[0m \u001b[0mc\u001b[0m\u001b[0;34m[\u001b[0m\u001b[0;36m2\u001b[0m\u001b[0;34m]\u001b[0m\u001b[0;34m[\u001b[0m\u001b[0;36m0\u001b[0m\u001b[0;34m]\u001b[0m \u001b[0;34m!=\u001b[0m \u001b[0mres\u001b[0m\u001b[0;34m[\u001b[0m\u001b[0;36m0\u001b[0m\u001b[0;34m]\u001b[0m \u001b[0;32mand\u001b[0m \u001b[0mc\u001b[0m\u001b[0;34m[\u001b[0m\u001b[0;36m2\u001b[0m\u001b[0;34m]\u001b[0m\u001b[0;34m[\u001b[0m\u001b[0;36m0\u001b[0m\u001b[0;34m]\u001b[0m \u001b[0;34m!=\u001b[0m \u001b[0mres\u001b[0m\u001b[0;34m[\u001b[0m\u001b[0;34m-\u001b[0m\u001b[0;36m1\u001b[0m\u001b[0;34m]\u001b[0m\u001b[0;34m:\u001b[0m\u001b[0;34m\u001b[0m\u001b[0m\n\u001b[1;32m     37\u001b[0m                     \u001b[0;32mreturn\u001b[0m \u001b[0;34m'IMPOSSIBLE'\u001b[0m\u001b[0;34m\u001b[0m\u001b[0m\n\u001b[0;32m---> 38\u001b[0;31m                 \u001b[0;32mif\u001b[0m \u001b[0mres\u001b[0m \u001b[0;32mand\u001b[0m \u001b[0mres\u001b[0m\u001b[0;34m[\u001b[0m\u001b[0;34m-\u001b[0m\u001b[0;36m1\u001b[0m\u001b[0;34m]\u001b[0m \u001b[0;34m==\u001b[0m \u001b[0mc\u001b[0m\u001b[0;34m[\u001b[0m\u001b[0;36m0\u001b[0m\u001b[0;34m]\u001b[0m\u001b[0;34m[\u001b[0m\u001b[0;36m0\u001b[0m\u001b[0;34m]\u001b[0m \u001b[0;32mor\u001b[0m \u001b[0mres\u001b[0m\u001b[0;34m[\u001b[0m\u001b[0;36m0\u001b[0m\u001b[0;34m]\u001b[0m \u001b[0;34m==\u001b[0m \u001b[0mc\u001b[0m\u001b[0;34m[\u001b[0m\u001b[0;36m1\u001b[0m\u001b[0;34m]\u001b[0m\u001b[0;34m[\u001b[0m\u001b[0;36m0\u001b[0m\u001b[0;34m]\u001b[0m\u001b[0;34m:\u001b[0m\u001b[0;34m\u001b[0m\u001b[0m\n\u001b[0m\u001b[1;32m     39\u001b[0m                     \u001b[0mres\u001b[0m \u001b[0;34m+=\u001b[0m \u001b[0mc\u001b[0m\u001b[0;34m[\u001b[0m\u001b[0;36m1\u001b[0m\u001b[0;34m]\u001b[0m\u001b[0;34m[\u001b[0m\u001b[0;36m0\u001b[0m\u001b[0;34m]\u001b[0m \u001b[0;34m+\u001b[0m \u001b[0mc\u001b[0m\u001b[0;34m[\u001b[0m\u001b[0;36m0\u001b[0m\u001b[0;34m]\u001b[0m\u001b[0;34m[\u001b[0m\u001b[0;36m0\u001b[0m\u001b[0;34m]\u001b[0m\u001b[0;34m\u001b[0m\u001b[0m\n\u001b[1;32m     40\u001b[0m                 \u001b[0;32melse\u001b[0m\u001b[0;34m:\u001b[0m\u001b[0;34m\u001b[0m\u001b[0m\n",
      "\u001b[0;31mIndexError\u001b[0m: string index out of range"
     ]
    }
   ],
   "source": [
    "from copy import deepcopy\n",
    "import numpy as np\n",
    "from math import floor, ceil\n",
    "\n",
    "def solve_b(l):\n",
    "    N, R, O, Y, G, B, V = map(int,l)\n",
    "    if V != 0 and V > Y:\n",
    "        return 'IMPOSSIBLE'\n",
    "    if O != 0 and O > B:\n",
    "        return 'IMPOSSIBLE'\n",
    "    if G != 0 and G > R:\n",
    "        return 'IMPOSSIBLE'\n",
    "    s = []\n",
    "    if V > 0:\n",
    "        Y -= V\n",
    "        s.append(('Y', (V * 'VY')))\n",
    "    if O > 0:\n",
    "        B -= O\n",
    "        s.append(('B', (O * 'OB')))\n",
    "    if G > 0:\n",
    "        R -= G\n",
    "        s.append(('R', (G * 'GR')))\n",
    "        \n",
    "    res = ''\n",
    "    c = [['Y', Y], ['B', B], ['R', R]]\n",
    "    n = Y + B + R\n",
    "    for x in range(n):\n",
    "        c.sort(lambda x, y: ord(y[0]) - ord(x[0]))\n",
    "        c.sort(lambda x, y: y[1] - x[1])\n",
    "#         print c\n",
    "        if x == n - 2:\n",
    "#             print 'micro'\n",
    "            if c[1][1] == 0 and c[2][1] == 0:\n",
    "                return 'IMPOSSIBLE'\n",
    "            else:\n",
    "                if res and res[-1] == res[0] and c[2][0] != res[0] and c[2][0] != res[-1]:\n",
    "                    return 'IMPOSSIBLE'\n",
    "                if res and res[-1] == c[0][0] or res[0] == c[1][0]:\n",
    "                    res += c[1][0] + c[0][0]\n",
    "                else:\n",
    "                    res += c[0][0] + c[1][0]\n",
    "#                 print res\n",
    "                break\n",
    "                    \n",
    "        \n",
    "        if res and (res[-1] == c[0][0]):\n",
    "            if c[1][1] == 0 and c[2][1] == 0:\n",
    "                return 'IMPOSSIBLE'\n",
    "            res += c[1][0]\n",
    "            c[1][1] -= 1\n",
    "        else:\n",
    "            res += c[0][0]\n",
    "            c[0][1] -= 1\n",
    "            \n",
    "    if res and res[0] == res[-1]:\n",
    "        return 'IMPOSSIBLE'\n",
    "    \n",
    "    for x in s:\n",
    "        if x[0] in res:\n",
    "            i = res.index(x[0])\n",
    "            res = res[:i+1] + x[1] + res[i + 1:]\n",
    "        elif not res:\n",
    "            res += x[1]\n",
    "        else:\n",
    "            return 'IMPOSSIBLE'\n",
    "    \n",
    "    return res\n",
    "print 'loading functions done'\n",
    "\n",
    "with open('round B/B-large.in', 'r') as f:\n",
    "    data = f.readlines()\n",
    "print 'loading data done'\n",
    "\n",
    "out = ''\n",
    "total_cases = int(data[0])\n",
    "counter = 1\n",
    "print 'number of cases - ', total_cases\n",
    "for cur_case in range(total_cases):\n",
    "    print cur_case + 1, '/', total_cases\n",
    "    l = data[counter].strip().split(' ')\n",
    "    res = solve_b(l)\n",
    "#     print res\n",
    "    counter += 1\n",
    "    # computation\n",
    "    out += 'Case #%d: %s\\n' % (cur_case + 1, res)\n",
    "    \n",
    "print 'saving data'\n",
    "with open('round B/outputB_large.txt', 'w') as f:\n",
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
   "execution_count": 16,
   "metadata": {
    "collapsed": false
   },
   "outputs": [],
   "source": [
    "\n",
    "a,b = [1,2]"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 17,
   "metadata": {
    "collapsed": false
   },
   "outputs": [
    {
     "data": {
      "text/plain": [
       "1"
      ]
     },
     "execution_count": 17,
     "metadata": {},
     "output_type": "execute_result"
    }
   ],
   "source": [
    "a"
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
