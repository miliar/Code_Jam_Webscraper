{
 "cells": [
  {
   "cell_type": "code",
   "execution_count": 42,
   "metadata": {
    "collapsed": true
   },
   "outputs": [],
   "source": [
    "import numpy as np"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 155,
   "metadata": {
    "collapsed": false
   },
   "outputs": [],
   "source": [
    "def read_prob(f_in):\n",
    "    n, k = f_in.readline().replace('\\n','').split(' ')\n",
    "    return int(n), int(k)\n",
    "\n",
    "def write_solution(f_out, num_case, res):\n",
    "    f_out.write(\"Case #%s: %s %s\\n\"%(num_case, res[0], res[1]))\n",
    "\n",
    "def solve(case):\n",
    "    n = case[0]\n",
    "    k = case[1]\n",
    "    l = []\n",
    "    if(n%2==0):\n",
    "        l.append((n/2)-1)\n",
    "        l.append(n/2)\n",
    "    else:\n",
    "        l.append(n/2)\n",
    "        l.append(n/2)\n",
    "    argmax = np.argmax(l)\n",
    "    for i in range(1,k):\n",
    "        argmax = np.argmax(l)\n",
    "        new = l[argmax]\n",
    "        if(l[argmax]%2==0):\n",
    "            l[argmax]=((new/2)-1)\n",
    "            l.insert(argmax+1, new/2)\n",
    "        else:\n",
    "            l[argmax]=(new/2)\n",
    "            l.insert(argmax+1, new/2)\n",
    "    try:\n",
    "        return max(l[argmax],l[argmax+1]), min(l[argmax],l[argmax+1])\n",
    "    except:\n",
    "        return max(l[argmax],l[argmax-1]), min(l[argmax],l[argmax-1])\n",
    "    \n",
    "def main(file_name):\n",
    "    f_in = open(file_name, 'r')\n",
    "    nb_test_case = int(f_in.readline()[:-1])\n",
    "    f_out = open(file_name[:-2]+\"out\", 'w')\n",
    "    for i in range(nb_test_case):\n",
    "        write_solution(f_out,i+1,solve(read_prob(f_in)))"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 156,
   "metadata": {
    "collapsed": false
   },
   "outputs": [],
   "source": [
    "main('test.in')"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 157,
   "metadata": {
    "collapsed": false
   },
   "outputs": [],
   "source": [
    "main(\"C-small-1-attempt5.in\")"
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
   "version": "2.7.13"
  }
 },
 "nbformat": 4,
 "nbformat_minor": 1
}
