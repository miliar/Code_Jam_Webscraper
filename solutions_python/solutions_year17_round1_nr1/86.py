{
 "cells": [
  {
   "cell_type": "code",
   "execution_count": 20,
   "metadata": {
    "collapsed": false
   },
   "outputs": [
    {
     "data": {
      "text/plain": [
       "['C', 'C', 'C', 'C', 'A', 'A', 'A', 'B', 'B']"
      ]
     },
     "execution_count": 20,
     "metadata": {},
     "output_type": "execute_result"
    }
   ],
   "source": [
    "def solve(R, C, rows):\n",
    "    for index, row in enumerate(rows):\n",
    "        if row.count('?') != len(row):\n",
    "            rows[index] = propagate(row)\n",
    "    first = True\n",
    "    curr = ['?']\n",
    "    for index, row in enumerate(rows):\n",
    "        if row[0] != '?' and first:\n",
    "            first = False\n",
    "            for j in range(index):\n",
    "                rows[j] = row\n",
    "        elif curr[0] != '?' and row[0] == '?':\n",
    "            rows[index] = curr\n",
    "        curr = rows[index]\n",
    "    return rows\n",
    "\n",
    "def propagate(row):\n",
    "    curr = '?'\n",
    "    first = True\n",
    "    for i, cell in enumerate(row):\n",
    "        if row[i] != '?' and first:\n",
    "            first = False\n",
    "            for j in range(i):\n",
    "                row[j] = row[i]\n",
    "        elif curr != '?' and row[i] == '?':\n",
    "             row[i] = curr\n",
    "        curr = row[i]\n",
    "    return row\n",
    "\n",
    "\n",
    "\n",
    "propagate(list('??C?A??B?'))"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 26,
   "metadata": {
    "collapsed": false
   },
   "outputs": [],
   "source": [
    "infile = open('test.txt')\n",
    "outfile = open('out.txt', 'w')\n",
    "T = int(infile.readline())\n",
    "for t in range(1, T+1):\n",
    "    R, C = map(int, infile.readline().split())\n",
    "    rows = [list(infile.readline().strip()) for _ in range(R)]\n",
    "    outfile.write('Case #{}:\\n'.format(t))\n",
    "    \n",
    "    soln = solve(R, C, rows)\n",
    "    for row in soln:\n",
    "        outfile.write(''.join(row) + '\\n')\n",
    "\n",
    "infile.close()\n",
    "outfile.close()"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 15,
   "metadata": {
    "collapsed": false
   },
   "outputs": [
    {
     "data": {
      "text/plain": [
       "False"
      ]
     },
     "execution_count": 15,
     "metadata": {},
     "output_type": "execute_result"
    }
   ],
   "source": [
    "[1,2] == [2,1]"
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
