{
 "cells": [
  {
   "cell_type": "code",
   "execution_count": 1,
   "metadata": {
    "collapsed": false
   },
   "outputs": [],
   "source": [
    "import os"
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
    "collapsed": false
   },
   "outputs": [],
   "source": [
    "def read_input(fn):\n",
    "    with open(fn, 'r') as f:\n",
    "        lines = f.readlines()\n",
    "        num_in = int(lines[0])\n",
    "    return num_in, map(lambda l: l.strip(), lines[1:])\n",
    "\n",
    "def write_output(solutions, out_fn):\n",
    "    with open(out_fn, 'w') as f:\n",
    "        i = 0\n",
    "        for sol in solutions:\n",
    "            i += 1\n",
    "            f.write(\"Case #{i}:{solution}\\n\".format(i=i, solution=sol))\n",
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
    "def p1(k, s):\n",
    "    flips = 0\n",
    "    head = 0\n",
    "    while (head + k) <= len(s):\n",
    "        #print head, s\n",
    "        if s[head]:\n",
    "            head += 1\n",
    "            continue\n",
    "        \n",
    "        for i in xrange(k):\n",
    "            #print head, flips, i\n",
    "            s[head + i] = not s[head + i]\n",
    "            \n",
    "        flips += 1\n",
    "        head += 1\n",
    "    \n",
    "    if all(s):\n",
    "        return \" \" + str(flips)\n",
    "    else:\n",
    "        return \" IMPOSSIBLE\""
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 7,
   "metadata": {
    "collapsed": false
   },
   "outputs": [],
   "source": [
    "p1_file = \"A-large.in\"\n",
    "_num_in, inputs = read_input(p1_file)\n",
    "\n",
    "#print inputs\n",
    "sols = []\n",
    "for in_line in inputs:\n",
    "    #print in_line\n",
    "    s, k = in_line.split(\" \")\n",
    "    sols.append(p1(int(k), [(c == '+') for c in s]))\n",
    "                    \n",
    "                    \n",
    "write_output(sols, \"p1_s.txt\")"
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
   "execution_count": 15,
   "metadata": {
    "collapsed": false
   },
   "outputs": [],
   "source": [
    "def p2(n):\n",
    "    for i in xrange(n, 0, -1):\n",
    "        digits = map(int, str(i))\n",
    "        if all(digits[i] <= digits[i+1] for i in xrange(len(digits) - 1)):\n",
    "            return i"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 20,
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
    "_num_in, inputs = read_input('p2.in')\n",
    "write_output((p2(int(n_str)) for n_str in inputs), 'p2_s.out')\n",
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
   "execution_count": null,
   "metadata": {
    "collapsed": false
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
