{
 "cells": [
  {
   "cell_type": "code",
   "execution_count": 15,
   "metadata": {
    "collapsed": true
   },
   "outputs": [],
   "source": [
    "# File names\n",
    "f_in_name = \"C-large.in\"\n",
    "f_out_name = \"C-large_out.txt\""
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 16,
   "metadata": {
    "collapsed": false
   },
   "outputs": [],
   "source": [
    "f_in = open(f_in_name)\n",
    "lines = f_in.readlines()\n",
    "f_in.close\n",
    "\n",
    "# Solve each test case\n",
    "answers = []\n",
    "n_cases = int(lines[0])\n",
    "for line in lines[1:]:\n",
    "    \n",
    "    ## SOLVE PROBLEM\n",
    "    ##################\n",
    "    n, k = [int(i) for i in line.strip().split()]\n",
    "    \n",
    "    def calc_s1_s2(n, k):\n",
    "        s1 = (n-1) // 2\n",
    "        if n % 2 == 0:\n",
    "            s1 += 1\n",
    "        s2 = (n-1) // 2\n",
    "        return s1, s2\n",
    "    s1, s2 = calc_s1_s2(n, k)\n",
    "    while k >= 2:\n",
    "        if k % 2 == 0:\n",
    "            n = s1\n",
    "        else:\n",
    "            n = s2\n",
    "        k = k // 2\n",
    "        s1, s2 = calc_s1_s2(n, k)\n",
    "        \n",
    "    answers.append(\"{} {}\".format(s1, s2))\n",
    "        \n",
    "# Write to file\n",
    "f_out = open(f_out_name, 'w')\n",
    "for i, a in enumerate(answers):\n",
    "    f_out.write(\"Case #{}: {}\\n\".format(i+1, a))\n",
    "f_out.close()"
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
   "display_name": "Python [conda env:py35]",
   "language": "python",
   "name": "conda-env-py35-py"
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
   "version": "3.5.2"
  }
 },
 "nbformat": 4,
 "nbformat_minor": 2
}
