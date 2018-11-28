{
 "cells": [
  {
   "cell_type": "code",
   "execution_count": 70,
   "metadata": {
    "collapsed": false,
    "deletable": true,
    "editable": true
   },
   "outputs": [],
   "source": [
    "import pandas as pd\n",
    "import numpy as np\n",
    "import math"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 102,
   "metadata": {
    "collapsed": true
   },
   "outputs": [],
   "source": [
    "'''For any given pair (n,k), find an equivalent n' such that k' = 1'''\n",
    "def find_n_prime(n,k):\n",
    "    # in the sequence with num ppl = k, each number repeats 2^p times\n",
    "    # find the largest 2^p <= k (where p is an integer)\n",
    "    # this can be easily done in base 2\n",
    "    p = len(bin(k)) - 3 # this gives '0b.....'\n",
    "    n_prime = math.ceil((n - k + 1) / 2**p)\n",
    "    return(n_prime)"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 110,
   "metadata": {
    "collapsed": true
   },
   "outputs": [],
   "source": [
    "'''Find min and max where k == 1'''\n",
    "def find_mm(n,k):\n",
    "    if (k!=1):\n",
    "        n = find_n_prime(n,k)\n",
    "    n = n - 1\n",
    "    return([math.ceil(n/2),math.floor(n/2)])"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 111,
   "metadata": {
    "collapsed": false
   },
   "outputs": [
    {
     "data": {
      "text/plain": [
       "[2, 1]"
      ]
     },
     "execution_count": 111,
     "metadata": {},
     "output_type": "execute_result"
    }
   ],
   "source": [
    "find_n_prime(26,7)\n",
    "find_mm(9,3)"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 112,
   "metadata": {
    "collapsed": false
   },
   "outputs": [],
   "source": [
    "'''Format output'''\n",
    "def format_output(i,s):\n",
    "    return(\"Case #\"+str(i)+\": \"+\" \".join(map(str,s)))\n",
    "#format_output(1,[1 10])"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 118,
   "metadata": {
    "collapsed": false
   },
   "outputs": [
    {
     "data": {
      "text/plain": [
       "0        Case #1: 1 0\n",
       "1        Case #2: 1 0\n",
       "2        Case #3: 1 1\n",
       "3        Case #4: 0 0\n",
       "4    Case #5: 500 499\n",
       "dtype: object"
      ]
     },
     "execution_count": 118,
     "metadata": {},
     "output_type": "execute_result"
    }
   ],
   "source": [
    "# running test\n",
    "filename = \"C-small-2-attempt0\"\n",
    "input = pd.read_csv(filename+\".noheader.in\", delimiter = \" \", names = None, header = None) # don't want first line\n",
    "input.columns = ['n','k']\n",
    "input.head()\n",
    "output = input.apply(lambda x: format_output(x.name + 1, find_mm(x.n, x.k)), axis = 1)\n",
    "output.to_csv(filename + \".out\", index = False, header = False)\n",
    "output.head()"
   ]
  }
 ],
 "metadata": {
  "kernelspec": {
   "display_name": "Python 3",
   "language": "python",
   "name": "python3"
  },
  "language_info": {
   "codemirror_mode": {
    "name": "ipython",
    "version": 3
   },
   "file_extension": ".py",
   "mimetype": "text/x-python",
   "name": "python",
   "nbconvert_exporter": "python",
   "pygments_lexer": "ipython3",
   "version": "3.5.3"
  }
 },
 "nbformat": 4,
 "nbformat_minor": 2
}
