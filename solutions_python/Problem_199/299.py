{
 "cells": [
  {
   "cell_type": "code",
   "execution_count": 18,
   "metadata": {
    "collapsed": false
   },
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "['+', '+', '+', '+', '-', '+', '+', '-']\n",
      "['+', '+', '+', '+', '+', '-', '-', '-']\n",
      "['+', '+', '+', '+', '+', '+', '+', '+']\n",
      "['+', '-', '+', '-', '-']\n",
      "['+', '+', '-', '+', '+']\n"
     ]
    }
   ],
   "source": [
    "def solve(seq, K):\n",
    "    flips = 0\n",
    "    for index, val in enumerate(seq):\n",
    "        if index + K > len(seq):\n",
    "            break\n",
    "        if val == '-':\n",
    "            flip(seq, index, K)\n",
    "            flips += 1\n",
    "            print (seq)\n",
    "    if seq.count('-') == 0:\n",
    "        return flips\n",
    "    else:\n",
    "        return -1\n",
    "    \n",
    "\n",
    "def flip(seq, index, K):\n",
    "    for i in range(index, index + K):\n",
    "        if seq[i] == '-':\n",
    "            seq[i] = '+'\n",
    "        else:\n",
    "            seq[i] = '-'\n",
    "\n",
    "infile = open('test.txt')\n",
    "outfile = open('out.txt', 'w')\n",
    "\n",
    "T = int(infile.readline())\n",
    "for t in range(1, T+1):\n",
    "    seq, K = infile.readline().split()\n",
    "    K = int(K)\n",
    "    result = solve(list(seq), K)\n",
    "    if result == -1:\n",
    "        printed = 'IMPOSSIBLE'\n",
    "    else:\n",
    "        printed = str(result)\n",
    "    \n",
    "    outfile.write('Case #{}: {}\\n'.format(t, printed))\n",
    "\n",
    "infile.close()\n",
    "outfile.close()"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 10,
   "metadata": {
    "collapsed": false
   },
   "outputs": [
    {
     "data": {
      "text/plain": [
       "2"
      ]
     },
     "execution_count": 10,
     "metadata": {},
     "output_type": "execute_result"
    }
   ],
   "source": [
    "seq.count('-')"
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
