{
 "cells": [
  {
   "cell_type": "code",
   "execution_count": 37,
   "metadata": {
    "collapsed": false
   },
   "outputs": [],
   "source": [
    "with open('A-large.in', 'r') as inp:\n",
    "    with open('answer.txt', 'w') as outp:\n",
    "        T = int(inp.readline())\n",
    "        for i in range(T):\n",
    "            line, k = inp.readline().rstrip().split(' ')\n",
    "            k = int(k)\n",
    "            answer = solve1(line, k)\n",
    "            outp.write(\"Case #{0}: {1}\\n\".format(str(i + 1), [str(answer), \"IMPOSSIBLE\"][answer == -1]))"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 36,
   "metadata": {
    "collapsed": true
   },
   "outputs": [],
   "source": [
    "def solve1(s, k):\n",
    "    answer = 0\n",
    "    current_on = []\n",
    "    for i, sym in enumerate(s):\n",
    "        if i + k <= len(s):\n",
    "            current_state = sum(current_on[-(k - 1):]) + int(sym == '-')\n",
    "            if current_state % 2 == 1:\n",
    "                current_on.append(1)\n",
    "                answer += 1\n",
    "            else:\n",
    "                current_on.append(0)\n",
    "        else:\n",
    "            current_state = sum(current_on[-(k - 1):]) + int(sym == '-')\n",
    "            if current_state % 2 == 1:\n",
    "                answer = -1\n",
    "                break\n",
    "            current_on.append(0)\n",
    "    return answer"
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
    "with open('B-large.in', 'r') as inp:\n",
    "    with open('answer2.txt', 'w') as outp:\n",
    "        T = int(inp.readline())\n",
    "        for i in range(T):\n",
    "            n = inp.readline().rstrip()\n",
    "            answer = solve2(list(n))\n",
    "            #print n\n",
    "            #print str(int(''.join(answer)))\n",
    "            #print ' '\n",
    "            if int(n) < int(str(int(''.join(answer)))):\n",
    "                print '!!!!!!!!!!!!!!!!!!!!!!!!!!!!!'\n",
    "            outp.write(\"Case #{0}: {1}\\n\".format(str(i + 1), str(int(''.join(answer)))))"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 67,
   "metadata": {
    "collapsed": true
   },
   "outputs": [],
   "source": [
    "def solve2(n):\n",
    "    bad = None\n",
    "    for i, sym in enumerate(n):\n",
    "        if i != 0 and sym < n[i - 1]:\n",
    "            bad = i\n",
    "            break\n",
    "    if bad is None:\n",
    "        return n\n",
    "    last_to_change = bad - 1\n",
    "    first_to_change = bad - 1\n",
    "    while first_to_change != 0 and n[first_to_change - 1] == n[last_to_change]:\n",
    "        first_to_change -= 1\n",
    "        if first_to_change == 0:\n",
    "            break\n",
    "    print first_to_change, last_to_change, bad\n",
    "    for i in range(first_to_change, last_to_change + 1):\n",
    "        n[i] = str(int(n[i]) - 1)\n",
    "    for i in range(first_to_change + 1, len(n)):\n",
    "        n[i] = '9'\n",
    "    return n"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 91,
   "metadata": {
    "collapsed": false
   },
   "outputs": [],
   "source": [
    "with open('C-small-2-attempt0.in', 'r') as inp:\n",
    "    with open('answer3.txt', 'w') as outp:\n",
    "        T = int(inp.readline())\n",
    "        for i in range(T):\n",
    "            n, k = map(int, inp.readline().rstrip().split())\n",
    "            answer = solve3(n, k)\n",
    "            #print n, k, answer\n",
    "            outp.write(\"Case #{0}: {1} {2}\\n\".format(str(i + 1), str(answer[0]), str(answer[1])))"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 90,
   "metadata": {
    "collapsed": true
   },
   "outputs": [],
   "source": [
    "from collections import defaultdict\n",
    "from copy import deepcopy\n",
    "def solve3(n, k):\n",
    "    current_people = 0\n",
    "    cnt = {n: 1}\n",
    "    current_inc = 1\n",
    "    while current_people + current_inc < k:\n",
    "        #print current_people, current_inc, cnt\n",
    "        buf_cnt = defaultdict(int)\n",
    "        for num, val in cnt.items():\n",
    "            buf_cnt[num / 2] += val\n",
    "            buf_cnt[(num - 1) / 2] += val\n",
    "        cnt = deepcopy(buf_cnt)\n",
    "        current_people += current_inc\n",
    "        current_inc *= 2\n",
    "    #print current_people, cnt\n",
    "    while current_people <= k:\n",
    "        max_seg = max(cnt.keys())\n",
    "        if current_people + cnt[max_seg] >= k:\n",
    "            return max_seg / 2, (max_seg - 1) / 2\n",
    "        current_people += cnt[max_seg]\n",
    "        del cnt[max_seg]"
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
  "anaconda-cloud": {},
  "kernelspec": {
   "display_name": "Python [conda root]",
   "language": "python",
   "name": "conda-root-py"
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
