{
 "cells": [
  {
   "cell_type": "code",
   "execution_count": 27,
   "metadata": {
    "collapsed": false
   },
   "outputs": [],
   "source": [
    "cases = [] \n",
    "with open('A-large.in') as f:\n",
    "    n_cases = int(f.readline())\n",
    "    for _ in range(n_cases):\n",
    "        r, c = map(int, f.readline().split())\n",
    "        rows = [f.readline().strip() for _ in range(r)]\n",
    "        cases.append((r, c, rows))"
   ]
  },
  {
   "cell_type": "raw",
   "metadata": {},
   "source": [
    "^ caret = up arrow\n",
    "> greater than = right arrow\n",
    "v lowercase v = down arrow\n",
    "< less than = left arrow"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 28,
   "metadata": {
    "collapsed": true
   },
   "outputs": [],
   "source": [
    "dird = {'^': (-1, 0), \n",
    "        '>': (0, +1),\n",
    "        'v': (+1, 0),\n",
    "        '<': (0, -1)}"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 29,
   "metadata": {
    "collapsed": true
   },
   "outputs": [],
   "source": [
    "def detect(rows, r, c, ri, ci, direction):\n",
    "    # finds arrow in that direction\n",
    "    dr, dc = dird[direction]\n",
    "    ri += dr\n",
    "    ci += dc\n",
    "    while 0 <= ri < r  and 0 <= ci < c:\n",
    "        if rows[ri][ci] != '.':\n",
    "            return True\n",
    "        ri += dr\n",
    "        ci += dc\n",
    "    return False    "
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 30,
   "metadata": {
    "collapsed": true
   },
   "outputs": [],
   "source": [
    "ret = []\n",
    "for i, (r, c, rows) in enumerate(cases):\n",
    "    ch = 0\n",
    "    for ri in range(r):\n",
    "        if ch == 'IMPOSSIBLE':\n",
    "            break\n",
    "        for ci in range(c):\n",
    "            val = rows[ri][ci]\n",
    "            if val == '.':\n",
    "                continue\n",
    "            elif detect(rows, r, c, ri, ci, val):\n",
    "                continue\n",
    "            else:\n",
    "                found = False\n",
    "                for direction in dird:\n",
    "                    if direction != val and not found:\n",
    "                        found |= detect(rows, r, c, ri, ci, direction)\n",
    "                if found:\n",
    "                    ch += 1\n",
    "                else:\n",
    "                    ch = 'IMPOSSIBLE'\n",
    "                    break\n",
    "    ret.append('Case #%s: %s' % (i + 1, ch))"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 31,
   "metadata": {
    "collapsed": true
   },
   "outputs": [],
   "source": [
    "with open('A-large.out', 'w') as f:\n",
    "    for line in ret:\n",
    "        f.write(line + '\\n')"
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
   "version": "2.7.6"
  }
 },
 "nbformat": 4,
 "nbformat_minor": 0
}
