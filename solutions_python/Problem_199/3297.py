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
   "execution_count": 27,
   "metadata": {
    "collapsed": false
   },
   "outputs": [],
   "source": [
    "def read_prob(f_in):\n",
    "    s,k = f_in.readline().replace('\\n','').split(' ')\n",
    "    return s,k\n",
    "\n",
    "def write_solution(f_out, num_case, res):\n",
    "    f_out.write(\"Case #\"+str(num_case)+\": \"+str(res)+'\\n')\n",
    "\n",
    "def solve(*case):\n",
    "    def flip(s,k,i):\n",
    "        def change(s):\n",
    "            res_s = \"\"\n",
    "            for c in s:\n",
    "                if(c=='-'):\n",
    "                    res_s+='+'\n",
    "                else:\n",
    "                    res_s+='-'\n",
    "            return res_s\n",
    "        s=s[:i]+change(s[i:i+k])+s[i+k:]\n",
    "        return s\n",
    "    s = case[0]\n",
    "    k = int(case[1])\n",
    "    cpt=0\n",
    "    for i in range(len(s)-k+1):\n",
    "        if(s[i]=='-'):\n",
    "            cpt+=1\n",
    "            s = flip(s,int(k),int(i))\n",
    "    if(\"-\" in s):\n",
    "        return \"IMPOSSIBLE\"\n",
    "    return cpt\n",
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
   "execution_count": 30,
   "metadata": {
    "collapsed": false
   },
   "outputs": [],
   "source": [
    "main(\"A-large.in\")"
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
   "version": "2.7.13"
  }
 },
 "nbformat": 4,
 "nbformat_minor": 1
}
