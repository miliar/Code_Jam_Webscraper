{
 "cells": [
  {
   "cell_type": "code",
   "execution_count": 1,
   "metadata": {
    "collapsed": true
   },
   "outputs": [],
   "source": [
    "import os\n",
    "import itertools\n",
    "nrange = lambda stop: iter(itertools.count().next, stop)"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 2,
   "metadata": {
    "collapsed": false
   },
   "outputs": [
    {
     "data": {
      "text/plain": [
       "'C:\\\\Users\\\\Patrick\\\\Documents'"
      ]
     },
     "execution_count": 2,
     "metadata": {},
     "output_type": "execute_result"
    }
   ],
   "source": [
    "os.getcwd()"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 3,
   "metadata": {
    "collapsed": true
   },
   "outputs": [],
   "source": [
    "def read_input(fn):\n",
    "    with open(fn, 'r') as f:\n",
    "        lines = f.readlines()\n",
    "        num_in = int(lines[0])\n",
    "    return num_in, map(lambda l: l.strip(), lines[1:])\n",
    "\n",
    "def write_output(solutions, out_fn, sep=\" \"):\n",
    "    with open(out_fn, 'w') as f:\n",
    "        i = 0\n",
    "        for sol in solutions:\n",
    "            i += 1\n",
    "            f.write(\"Case #{i}:{sep}{solution}\\n\".format(i=i, solution=sol, sep=sep))\n",
    "            "
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 4,
   "metadata": {
    "collapsed": false
   },
   "outputs": [],
   "source": [
    "def time_to_dest(start, speed, dest):\n",
    "    return float(dest - start) / speed\n",
    "\n",
    "def pA(distance, horses):\n",
    "    return distance / max(time_to_dest(start, speed, distance) for start, speed in horses)\n",
    "     \n"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 8,
   "metadata": {
    "collapsed": false
   },
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "100\n"
     ]
    }
   ],
   "source": [
    "_num_in, input_lines = read_input('pA.in')\n",
    "\n",
    "outputs = []\n",
    "prob_line = 0\n",
    "while prob_line < len(input_lines):\n",
    "    params = map(int, input_lines[prob_line].split(' '))\n",
    "    distance = params[0]\n",
    "    line_count = params[1]\n",
    "    input_array = [map(int, line.split(' ')) for line in input_lines[(prob_line + 1):(prob_line + 1 + line_count)]]\n",
    "    outputs.append(pA(distance, input_array))\n",
    "    prob_line = prob_line + line_count + 1\n",
    "\n",
    "write_output(\n",
    "    outputs, \n",
    "    'pA.out',\n",
    "    sep=' ')\n",
    "\n",
    "\n",
    "print len(outputs)"
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
   "execution_count": 20,
   "metadata": {
    "collapsed": false
   },
   "outputs": [],
   "source": [
    "def pB(n, r, o, y, g, b, v):\n",
    "    stalls = []\n",
    "    horse_counts = dict(r=r, o=o, y=y, g=g, b=b, v=v)\n",
    "    if any(v > n / 2 for k,v in horse_counts.iteritems()):\n",
    "        return \"IMPOSSIBLE\"\n",
    "    \n",
    "    last_key = None\n",
    "    while not all(v == 0 for v in horse_counts.values()):\n",
    "        max_h = None\n",
    "        for key, value in horse_counts.items():\n",
    "            if key != last_key and (value > horse_counts.get(max_h, 0) or \n",
    "                                    (value == horse_counts.get(max_h, 0) and len(stalls) > 0 and key == stalls[0])):\n",
    "                max_h = key\n",
    "        \n",
    "        horse_counts[max_h] -= 1\n",
    "        last_key = max_h\n",
    "        stalls.append(max_h)\n",
    "    \n",
    "    return \"\".join(stalls)\n",
    "    "
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 22,
   "metadata": {
    "collapsed": false
   },
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "99\n"
     ]
    }
   ],
   "source": [
    "_num_in, input_lines = read_input('pB.in')\n",
    "\n",
    "outputs = []\n",
    "prob_line = 0\n",
    "while prob_line < len(input_lines):\n",
    "    n, r, o, y, g, b, v = map(int, input_lines[prob_line].split(' '))\n",
    "    outputs.append(pB(n, r, o, y, g, b, v))\n",
    "    prob_line = prob_line + 1\n",
    "\n",
    "write_output(\n",
    "    outputs, \n",
    "    'pB.out',\n",
    "    sep=' ')\n",
    "\n",
    "\n",
    "print len(outputs)"
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
   "execution_count": 68,
   "metadata": {
    "collapsed": false
   },
   "outputs": [],
   "source": [
    "def valid_slice(space, up, down, left, right, valid):\n",
    "    return all((space[r][c] in valid)\n",
    "               for r in xrange(up, down + 1)\n",
    "               for c in xrange(left, right + 1))\n",
    "            \n",
    "\n",
    "def pAssign(space, r0, c0):\n",
    "    engulfable = [\"?\", space[r0][c0]]\n",
    "    \n",
    "    for up in xrange(r0, -1, -1):\n",
    "        if not valid_slice(space, up, r0, c0, c0, engulfable):\n",
    "            up += 1\n",
    "            break\n",
    "            \n",
    "    for left in xrange(c0, -1, -1):\n",
    "        if not valid_slice(space, up, r0, left, c0, engulfable):\n",
    "            left += 1\n",
    "            break\n",
    "    \n",
    "    for right in xrange(c0, len(space[r0])):\n",
    "        if not valid_slice(space, up, r0, left, right, engulfable):\n",
    "            right -= 1\n",
    "            break\n",
    "                \n",
    "    for down in xrange(r0, len(space)):\n",
    "        if not valid_slice(space, up, down, left, right, engulfable):\n",
    "            down -= 1\n",
    "            break\n",
    "    \n",
    "    for r in xrange(up, down + 1):\n",
    "        for c in xrange(left, right + 1):\n",
    "            space[r][c] = space[r0][c0]\n",
    "            \n",
    "def pA(grid, rows, cols):\n",
    "    seen = set()\n",
    "    for r in xrange(rows):\n",
    "        for c in xrange(cols):\n",
    "            if grid[r][c] != \"?\" and grid[r][c] not in seen:\n",
    "                seen.add(grid[r][c])\n",
    "                pAssign(grid, r, c)\n",
    "    return '\\n'.join(''.join(grid[r]) for r in xrange(rows))\n"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 72,
   "metadata": {
    "collapsed": false
   },
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "CODE\n",
      "CODE\n",
      "CJAM\n",
      "100\n"
     ]
    }
   ],
   "source": [
    "test = [\n",
    "    'CODE',\n",
    "    '????',\n",
    "    '?JAM',\n",
    "]\n",
    "print pA([list(line) for line in test], 3, 4)\n",
    "\n",
    "_num_in, input_lines = read_input('pAL.in')\n",
    "\n",
    "outputs = []\n",
    "prob_line = 0\n",
    "while prob_line < len(input_lines):\n",
    "    line_count = int(input_lines[prob_line].split(' ')[0])\n",
    "    input_array = [list(line) for line in input_lines[(prob_line + 1):(prob_line + 1 + line_count)]]\n",
    "    outputs.append(pA(input_array, len(input_array), len(input_array[0])))\n",
    "    prob_line = prob_line + 1 + line_count\n",
    "\n",
    "write_output(\n",
    "    outputs, \n",
    "    'pA.out',\n",
    "    sep='\\n')\n",
    "\n",
    "\n",
    "print len(inputs)"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "metadata": {
    "collapsed": false
   },
   "outputs": [],
   "source": []
  },
  {
   "cell_type": "code",
   "execution_count": 107,
   "metadata": {
    "collapsed": false
   },
   "outputs": [],
   "source": [
    "from collections import defaultdict\n",
    "\n",
    "def pB(packages, serving_size):\n",
    "    packages_avail = defaultdict(lambda : [0] * len(serving_size))\n",
    "    for ing_idx in xrange(len(serving_size)):\n",
    "        print ing_idx\n",
    "        for package_size in packages[ing_idx]:\n",
    "            serving_count = float(package_size) / serving_size[ing_idx]\n",
    "            closest_serving_exact = round(serving_count) * serving_size[ing_idx]\n",
    "            print package_size, serving_count, \n",
    "            print [(closest_serving_exact * .9), closest_serving_exact, (closest_serving_exact * 1.1)]\n",
    "            if (closest_serving_exact != 0 and \n",
    "                    ((closest_serving_exact * .9) <= package_size <= (closest_serving_exact * 1.1))):\n",
    "                packages_avail[round(serving_count)][ing_idx] += 1\n",
    "                print 'ok'\n",
    "                \n",
    "    print packages_avail.items()\n",
    "    print \" \"\n",
    "    return sum(min(packages_at_size) for packages_at_size in packages_avail.values())\n",
    "            \n",
    "        "
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 108,
   "metadata": {
    "collapsed": false
   },
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "0\n",
      "900 1.8 [900.0, 1000.0, 1100.0]\n",
      "ok\n",
      "1\n",
      "660 2.2 [540.0, 600.0, 660.0]\n",
      "ok\n",
      "[(2.0, [1, 1])]\n",
      " \n",
      "0\n",
      "1500 3.0 [1350.0, 1500.0, 1650.0000000000002]\n",
      "ok\n",
      "1\n",
      "809 2.69666666667 [810.0, 900.0, 990.0000000000001]\n",
      "[(3.0, [1, 0])]\n",
      " \n",
      "0\n",
      "450 9.0 [405.0, 450.0, 495.00000000000006]\n",
      "ok\n",
      "449 8.98 [405.0, 450.0, 495.00000000000006]\n",
      "ok\n",
      "1\n",
      "1100 11.0 [990.0, 1100.0, 1210.0]\n",
      "ok\n",
      "1101 11.01 [990.0, 1100.0, 1210.0]\n",
      "ok\n",
      "[(9.0, [2, 0]), (11.0, [0, 2])]\n",
      " \n",
      "0\n",
      "300 0.6 [450.0, 500.0, 550.0]\n",
      "1\n",
      "500 1.66666666667 [540.0, 600.0, 660.0]\n",
      "[]\n",
      " \n",
      "0\n",
      "11 1.1 [9.0, 10.0, 11.0]\n",
      "ok\n",
      "13 1.3 [9.0, 10.0, 11.0]\n",
      "17 1.7 [18.0, 20.0, 22.0]\n",
      "11 1.1 [9.0, 10.0, 11.0]\n",
      "ok\n",
      "16 1.6 [18.0, 20.0, 22.0]\n",
      "14 1.4 [9.0, 10.0, 11.0]\n",
      "12 1.2 [9.0, 10.0, 11.0]\n",
      "18 1.8 [18.0, 20.0, 22.0]\n",
      "ok\n",
      "[(1.0, [2]), (2.0, [1])]\n",
      " \n",
      "0\n",
      "1260 18.0 [1134.0, 1260.0, 1386.0]\n",
      "ok\n",
      "1500 21.4285714286 [1323.0, 1470.0, 1617.0000000000002]\n",
      "ok\n",
      "700 10.0 [630.0, 700.0, 770.0000000000001]\n",
      "ok\n",
      "1\n",
      "800 10.0 [720.0, 800.0, 880.0000000000001]\n",
      "ok\n",
      "1440 18.0 [1296.0, 1440.0, 1584.0000000000002]\n",
      "ok\n",
      "1600 20.0 [1440.0, 1600.0, 1760.0000000000002]\n",
      "ok\n",
      "2\n",
      "1700 18.8888888889 [1539.0, 1710.0, 1881.0000000000002]\n",
      "ok\n",
      "1620 18.0 [1458.0, 1620.0, 1782.0000000000002]\n",
      "ok\n",
      "900 10.0 [810.0, 900.0, 990.0000000000001]\n",
      "ok\n",
      "[(19.0, [0, 0, 1]), (18.0, [1, 1, 1]), (10.0, [1, 1, 1]), (20.0, [0, 1, 0]), (21.0, [1, 0, 0])]\n",
      " \n",
      "[1, 0, 0, 0, 3, 2]\n"
     ]
    }
   ],
   "source": [
    "_num_in, input_lines = read_input('pB.in')\n",
    "\n",
    "outputs = []\n",
    "prob_line = 0\n",
    "while prob_line < len(input_lines):\n",
    "    line_count = int(input_lines[prob_line].split(' ')[0])\n",
    "    serving_size = map(int, input_lines[prob_line + 1].split(' '))\n",
    "    input_packages = map(lambda s: map(int, s.split(' ')), input_lines[(prob_line + 2):(prob_line + 2 + line_count)])\n",
    "    outputs.append(pB(input_packages, serving_size))\n",
    "    prob_line = prob_line + 2 + line_count\n",
    "\n",
    "print outputs"
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
  },
  {
   "cell_type": "code",
   "execution_count": 6,
   "metadata": {
    "collapsed": true
   },
   "outputs": [],
   "source": [
    "def p3_2(stall_num, users):\n",
    "    gaps = {stall_num: 1}\n",
    "    while users > 0:\n",
    "        next_size = max(gaps.iterkeys())\n",
    "        empty = next_size - 1\n",
    "        ls, rs = empty / 2, (empty + 1)/2\n",
    "        if gaps[next_size] >= users:\n",
    "            return rs, ls\n",
    "        \n",
    "        if rs > 0:\n",
    "            if rs in gaps:\n",
    "                gaps[rs] += gaps[next_size]\n",
    "            else:\n",
    "                gaps[rs] = gaps[next_size]\n",
    "                \n",
    "            if ls > 0:\n",
    "                if ls in gaps:\n",
    "                    gaps[ls] += gaps[next_size]\n",
    "                else:\n",
    "                    gaps[ls] = gaps[next_size]\n",
    "        \n",
    "        users -= gaps[next_size]\n",
    "        del gaps[next_size]\n",
    "        \n",
    "    return -1, -1\n",
    "    "
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 7,
   "metadata": {
    "collapsed": false
   },
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "100\n"
     ]
    }
   ],
   "source": [
    "_num_in, inputs = read_input('p3_large.in')\n",
    "\n",
    "write_output(\n",
    "    (' '.join(map(str, p3_2(int(n), int(k))))\n",
    "     for n, k in map(lambda in_str: map(int, in_str.split(' ')), inputs)), \n",
    "    'p3_s.out')\n",
    "\n",
    "\n",
    "print len(inputs)"
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
