{
 "cells": [
  {
   "cell_type": "code",
   "execution_count": 69,
   "metadata": {
    "collapsed": false
   },
   "outputs": [],
   "source": [
    "from collections import *\n",
    "from itertools import *\n",
    "\n",
    "def solve(N, P, recipe, ingredients):\n",
    "    unique = set()\n",
    "    unique.add(0) #special case\n",
    "    \n",
    "    for i in range(N):\n",
    "        for j in range(P):\n",
    "            minval = ingredients[i][j] * 10 / (11 * recipe[i]) + ((ingredients[i][j] * 10 % (11 * recipe[i])) > 0)\n",
    "            maxval = ingredients[i][j] * 10 / (9 * recipe[i])\n",
    "            if minval > maxval:\n",
    "                minval, maxval = 0, 0\n",
    "            unique.add(minval)\n",
    "            unique.add(maxval)\n",
    "            ingredients[i][j] = minval, maxval\n",
    "    U = len(unique)\n",
    "    mapping = dict(zip(sorted(unique), range(len(unique))))\n",
    "    \n",
    "    for i, j in product(range(N), range(P)):\n",
    "        old = ingredients[i][j]\n",
    "        ingredients[i][j] = mapping[old[0]], mapping[old[1]]\n",
    "    \n",
    "    for i in range(N):\n",
    "        ingredients[i].sort(key=lambda x: x[1])\n",
    "    \n",
    "    #print ingredients\n",
    "        \n",
    "    kits = 0\n",
    "    for serving in range(1, U):\n",
    "        good = True\n",
    "        while good:\n",
    "            picked = []\n",
    "            for i in range(len(ingredients)):\n",
    "                for j in range(len(ingredients[i])):\n",
    "                    r = ingredients[i][j]\n",
    "                    if r[0] <= serving <= r[1]:\n",
    "                        picked.append(j)\n",
    "                        break\n",
    "\n",
    "            if len(picked) == N:\n",
    "                kits += 1\n",
    "                for i in range(N):\n",
    "                    ingredients[i].pop(picked[i])\n",
    "            else:\n",
    "                good = False\n",
    "            \n",
    "    \n",
    "    return kits\n",
    "    \n",
    "    "
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 71,
   "metadata": {
    "collapsed": false
   },
   "outputs": [],
   "source": [
    "infile = open('B-small-attempt0.in')\n",
    "outfile = open('out.txt', 'w')\n",
    "T = int(infile.readline())\n",
    "for t in range(1, T+1):\n",
    "    N, P = map(int, infile.readline().split())\n",
    "    recipe = map(int, infile.readline().split())\n",
    "    ingredients = [map(int, infile.readline().split()) for _ in range(N)]\n",
    "    #print ingredients\n",
    "    outfile.write('Case #{}: {}\\n'.format(t, solve(N, P, recipe, ingredients)))\n",
    "    #print N, P\n",
    "infile.close()\n",
    "outfile.close()"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 16,
   "metadata": {
    "collapsed": false
   },
   "outputs": [
    {
     "data": {
      "text/plain": [
       "5"
      ]
     },
     "execution_count": 16,
     "metadata": {},
     "output_type": "execute_result"
    }
   ],
   "source": [
    "(441 * 10/ 11 / 100) + ((441*10%(11 * 100))>0)"
   ]
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
   "version": "2.7.12"
  }
 },
 "nbformat": 4,
 "nbformat_minor": 1
}
