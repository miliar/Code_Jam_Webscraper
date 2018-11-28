{
 "cells": [
  {
   "cell_type": "markdown",
   "metadata": {},
   "source": [
    "Oversized Pancake Flipper"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 49,
   "metadata": {
    "collapsed": true
   },
   "outputs": [],
   "source": [
    "from pprint import pprint"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 102,
   "metadata": {
    "collapsed": false
   },
   "outputs": [],
   "source": [
    "def solve(bits, m, n):\n",
    "    # construct flips\n",
    "    strat = [None] * (n - m + 1)\n",
    "    for i in range(n - m + 1):\n",
    "        strat[i] = [0] * i + [1] * m + [0] * (n - m - i)\n",
    "    pprint(strat)\n",
    "\n",
    "def main(lines):\n",
    "    tests = map(lambda x: x.split(' '), lines[1:])\n",
    "    for i, (init, m) in enumerate(tests):\n",
    "        # pprint('-----Case {}-----'.format(i))\n",
    "        m_int = int(m)\n",
    "        bits = map(lambda x: True if x == '+' else False, init)\n",
    "        n_int = len(bits)\n",
    "        result = greedy(bits, m_int, n_int)\n",
    "        print \"Case #{}: {}\".format(i + 1 , result)"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 137,
   "metadata": {
    "collapsed": false
   },
   "outputs": [],
   "source": [
    "def greedy(S, K):\n",
    "    N = len(S)\n",
    "    counter = 0\n",
    "    for i in range(N - K + 1):\n",
    "        if not S[i]:\n",
    "            counter += 1\n",
    "            for j in range(K):\n",
    "                S[i + j] = not S[i + j]\n",
    "    if all(S):\n",
    "        return counter\n",
    "    else:\n",
    "        return 'IMPOSSIBLE'\n",
    "\n",
    "def run_test(test):\n",
    "    chunks = test.split()\n",
    "    S = map(lambda ch: True if ch == '+' else False, chunks[0])\n",
    "    K = int(chunks[1])\n",
    "    return greedy(S, K)"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 140,
   "metadata": {
    "collapsed": false
   },
   "outputs": [],
   "source": [
    "# FILE_NAME = 'A-small-attempt0'\n",
    "FILE_NAME = 'A-large'\n",
    "INPUT_SUFFIX = '.in'\n",
    "OUTPUT_SUFFIX = '.out'\n",
    "\n",
    "INPUT_FILE = FILE_NAME + INPUT_SUFFIX\n",
    "OUTPUT_FILE = FILE_NAME + OUTPUT_SUFFIX\n",
    "\n",
    "with open(INPUT_FILE, 'r') as file_in:\n",
    "    lines = file_in.readlines()\n",
    "    T = lines[0]\n",
    "    tests = lines[1:]\n",
    "    \n",
    "with open(OUTPUT_FILE, 'w') as file_out:\n",
    "    for i_test, test in enumerate(tests):\n",
    "        result = run_test(test)\n",
    "        file_out.write('Case #{}: {}\\n'.format(i_test + 1, result))"
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
   "version": "2.7.11"
  }
 },
 "nbformat": 4,
 "nbformat_minor": 0
}
