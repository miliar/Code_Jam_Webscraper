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
   "execution_count": 67,
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
   "execution_count": null,
   "metadata": {
    "collapsed": false
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
    "    #print engulfable, r0, c0\n",
    "    \n",
    "    for up in xrange(r0, -1, -1):\n",
    "        if not valid_slice(space, up, r0, c0, c0, engulfable):\n",
    "            up += 1\n",
    "            break\n",
    "    #print '^', up\n",
    "            \n",
    "    for left in xrange(c0, -1, -1):\n",
    "        if not valid_slice(space, up, r0, left, c0, engulfable):\n",
    "            left += 1\n",
    "            break\n",
    "    #print '<', left\n",
    "    \n",
    "    for right in xrange(c0, len(space[r0])):\n",
    "        if not valid_slice(space, up, r0, left, right, engulfable):\n",
    "            right -= 1\n",
    "            break\n",
    "    #print '>', right\n",
    "                \n",
    "    for down in xrange(r0, len(space)):\n",
    "        if not valid_slice(space, up, down, left, right, engulfable):\n",
    "            down -= 1\n",
    "            break\n",
    "    #print 'v', down\n",
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
   "execution_count": 71,
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
    "_num_in, input_lines = read_input('pA.in')\n",
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
