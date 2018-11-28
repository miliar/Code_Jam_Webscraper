{
 "cells": [
  {
   "cell_type": "code",
   "execution_count": 2,
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
   "execution_count": 26,
   "metadata": {
    "collapsed": false
   },
   "outputs": [],
   "source": [
    "def read_prob(f_in):\n",
    "    D,N = map(int,f_in.readline().replace('\\n','').split(' '))\n",
    "    res = []\n",
    "    for i in range(N):\n",
    "        res.append(map(int,f_in.readline().replace('\\n','').split(' ')))\n",
    "    return D, res\n",
    "\n",
    "def write_solution(f_out, num_case, res):\n",
    "    f_out.write(\"Case #\"+str(num_case)+\": \"+str(res)+'\\n')\n",
    "\n",
    "def solve(*case):\n",
    "    def calc_finish(l):\n",
    "        d = l[0]\n",
    "        k = l[1][0]\n",
    "        s = l[1][1]\n",
    "        r = d-k\n",
    "        t = r*1.0 / s\n",
    "        return t\n",
    "    D = case[0]\n",
    "    l = case[1]\n",
    "    l = map(lambda x : [D,x], l)\n",
    "    res = map(calc_finish, l)\n",
    "    m = max(res)\n",
    "    return D*1.0/m\n",
    "    \n",
    "def main(file_name):\n",
    "    f_in = open(file_name, 'r')\n",
    "    nb_test_case = int(f_in.readline()[:-1])\n",
    "    f_out = open(file_name[:-2]+\"out\", 'w')\n",
    "    for i in range(nb_test_case):\n",
    "        write_solution(f_out,i+1,solve(*(read_prob(f_in))))"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 27,
   "metadata": {
    "collapsed": false
   },
   "outputs": [],
   "source": [
    "main(\"test.in\")"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 28,
   "metadata": {
    "collapsed": false
   },
   "outputs": [],
   "source": [
    "main(\"A-small-attempt0.in\")"
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
    "main(\"A-small-attempt0.in\")"
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
