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
    "def read_input(filename='./input.txt'):\n",
    "    input_d = []\n",
    "    with open(filename) as f:\n",
    "        num_cases = int(f.readline().strip())\n",
    "        for i in range(num_cases):\n",
    "            tmp = f.readline()\n",
    "            pattern, size = tmp.split()\n",
    "            pattern = [1 if p == '+' else 0 for p in pattern]\n",
    "            input_d.append((pattern,int(size)))\n",
    "    return input_d"
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
    "inp = read_input('./A-large.in.txt')"
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
    "mapping = {0: 1, 1:0}"
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
    "from copy import deepcopy"
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
    "def check(i):\n",
    "    i = deepcopy(i)\n",
    "    beg = deepcopy(i[0])\n",
    "    num_same = 0\n",
    "    num_iters = 0\n",
    "    while 0 in i[0]:\n",
    "        idx = -1\n",
    "        for idx, c in enumerate(i[0]):\n",
    "            if c == 0:\n",
    "                break\n",
    "\n",
    "        if idx+i[1] > len(i[0]):\n",
    "            return -1\n",
    "\n",
    "#         print(idx, idx+i[1])\n",
    "#         print(i)\n",
    "        for idx_ in range(idx, idx+i[1]):\n",
    "            i[0][idx_] = mapping[i[0][idx_]]\n",
    "        num_iters += 1\n",
    "\n",
    "        if all([j==k for j,k in zip(beg, i[0])]):\n",
    "            num_same += 1\n",
    "            if num_same == 3:\n",
    "                break\n",
    "    return num_iters"
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
    "check(inp[2])"
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
    "results = [\"Case #{}: {}\".format(j+1, check(i)) if check(i) >= 0 else \"Case #{}: {}\".format(j+1, 'IMPOSSIBLE') for j, i in enumerate(inp)]"
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
    "results[:100]"
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
    "with open('result_large.txt', 'w') as f:\n",
    "    for c in results:\n",
    "        f.write(c)\n",
    "        f.write('\\n')"
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
    "ls"
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
    "cat result_large.txt"
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
   "display_name": "Python 3",
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
