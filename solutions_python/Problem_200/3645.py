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
    "import numpy as np"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 76,
   "metadata": {
    "collapsed": false
   },
   "outputs": [
    {
     "ename": "SyntaxError",
     "evalue": "invalid syntax (<ipython-input-76-266b0fc9bf2a>, line 25)",
     "output_type": "error",
     "traceback": [
      "\u001b[0;36m  File \u001b[0;32m\"<ipython-input-76-266b0fc9bf2a>\"\u001b[0;36m, line \u001b[0;32m25\u001b[0m\n\u001b[0;31m    case = case[:i-1]+c1+case[i:]case = case[:i-1]+c1+case[i:]\u001b[0m\n\u001b[0m                                    ^\u001b[0m\n\u001b[0;31mSyntaxError\u001b[0m\u001b[0;31m:\u001b[0m invalid syntax\n"
     ]
    }
   ],
   "source": [
    "def read_prob(f_in):\n",
    "    n = f_in.readline().replace('\\n','')\n",
    "    return n\n",
    "\n",
    "def write_solution(f_out, num_case, res):\n",
    "    f_out.write(\"Case #\"+str(num_case)+\": \"+str(res)+'\\n')\n",
    "\n",
    "def solve(case):\n",
    "    def tidy(c1,c2):\n",
    "        modif = False\n",
    "        if(c2<c1 or c2=='0'):\n",
    "            modif = True\n",
    "            c2='9'\n",
    "            if(c1=='0'):\n",
    "                c1='9'\n",
    "            else:\n",
    "                c1=str(int(c1)-1)\n",
    "        return c1,modif\n",
    "    res = \"\"\n",
    "    for i in range(len(case)-1,0,-1):\n",
    "        c1, modif = tidy(case[i-1], case[i])\n",
    "        #case = case[:i]+c2+case[i+1:]\n",
    "        if(modif):\n",
    "            case = case[:i-1]+c1+\"9\"*len(case[i:])\n",
    "        case = case[:i-1]+c1+case[i:]\n",
    "        case = case[:i-1]+c1+case[i:]\n",
    "    if(case[0]=='0'):\n",
    "        case = case[1:]\n",
    "    return case\n",
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
   "execution_count": 75,
   "metadata": {
    "collapsed": false
   },
   "outputs": [
    {
     "data": {
      "text/plain": [
       "'9999999999999999999999999999999999999999999999999999999'"
      ]
     },
     "execution_count": 75,
     "metadata": {},
     "output_type": "execute_result"
    }
   ],
   "source": [
    "\"9\"*55"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 74,
   "metadata": {
    "collapsed": false
   },
   "outputs": [],
   "source": [
    "main(\"B-small-attempt0.in\")"
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
