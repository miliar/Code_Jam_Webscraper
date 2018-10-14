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
   "execution_count": 3,
   "metadata": {
    "collapsed": false
   },
   "outputs": [],
   "source": [
    "from pprint import pprint\n",
    "from IPython import embed\n",
    "from heapq import *"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 43,
   "metadata": {
    "collapsed": false
   },
   "outputs": [],
   "source": [
    "def compute_spaces(max_space):\n",
    "    if max_space % 2 == 0:\n",
    "        return {max_space / 2: 1, max_space / 2 - 1: 1}\n",
    "    else:\n",
    "        return {(max_space - 1) / 2: 2}\n",
    "\n",
    "def solve(N, K):\n",
    "    heap = []\n",
    "    count = {N: 1}\n",
    "    heappush(heap, -N)\n",
    "    while K > 0:\n",
    "        max_space = -heappop(heap)\n",
    "        max_count = count[max_space]\n",
    "        new_spaces = compute_spaces(max_space)\n",
    "        \n",
    "        for new_space, new_count in new_spaces.iteritems():\n",
    "            if new_space != 0:\n",
    "                if new_space in count:\n",
    "                    count[new_space] += new_count * max_count\n",
    "                else:\n",
    "                    heappush(heap, -new_space)\n",
    "                    count[new_space] = new_count * max_count\n",
    "        K -= max_count\n",
    "    \n",
    "    max_space = max(new_spaces)\n",
    "    min_space = min(new_spaces)\n",
    "    return \"{} {}\".format(max_space, min_space)\n",
    "    \n",
    "def run_test(test):\n",
    "    chunks = test.split(' ')\n",
    "    N = int(chunks[0])\n",
    "    K = int(chunks[1])\n",
    "    return solve(N, K)"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 60,
   "metadata": {
    "collapsed": false,
    "scrolled": false
   },
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "CPU times: user 28.7 ms, sys: 7.07 ms, total: 35.7 ms\n",
      "Wall time: 31.8 ms\n"
     ]
    }
   ],
   "source": [
    "%%time\n",
    "FILE_NAME = 'C-large'\n",
    "# FILE_NAME = 'A-large'\n",
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
    "\n",
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
