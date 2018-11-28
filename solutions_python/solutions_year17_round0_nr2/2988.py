{
 "cells": [
  {
   "cell_type": "code",
   "execution_count": 27,
   "metadata": {
    "collapsed": true
   },
   "outputs": [],
   "source": [
    "with open('B-small-attempt0.in') as f:\n",
    "    data = f.read()"
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
    "def make_figure(text):\n",
    "    didg = [int(d) for d in text]\n",
    "    #print(didg)\n",
    "    for i in reversed(range(1,len(didg))):\n",
    "        if didg[i] < didg[i-1]:\n",
    "            didg[i-1] -= 1\n",
    "            for k in range(i, len(didg)):\n",
    "                didg[k] = 9\n",
    "    #print(didg)\n",
    "    if didg[0] == 0:\n",
    "        return ''.join([str(d) for d in didg[1:len(didg)]])\n",
    "    else:\n",
    "        return ''.join([str(d) for d in didg])"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 29,
   "metadata": {
    "collapsed": false
   },
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "Case #1: 129\n",
      "Case #2: 999\n",
      "Case #3: 7\n",
      "Case #4: 113\n",
      "Case #5: 699\n",
      "Case #6: 478\n",
      "Case #7: 999\n",
      "Case #8: 299\n",
      "Case #9: 128\n",
      "Case #10: 889\n",
      "Case #11: 299\n",
      "Case #12: 249\n",
      "Case #13: 466\n",
      "Case #14: 134\n",
      "Case #15: 899\n",
      "Case #16: 399\n",
      "Case #17: 689\n",
      "Case #18: 238\n",
      "Case #19: 49\n",
      "Case #20: 149\n",
      "Case #21: 199\n",
      "Case #22: 399\n",
      "Case #23: 899\n",
      "Case #24: 159\n",
      "Case #25: 689\n",
      "Case #26: 669\n",
      "Case #27: 899\n",
      "Case #28: 799\n",
      "Case #29: 799\n",
      "Case #30: 699\n",
      "Case #31: 699\n",
      "Case #32: 59\n",
      "Case #33: 269\n",
      "Case #34: 399\n",
      "Case #35: 89\n",
      "Case #36: 399\n",
      "Case #37: 799\n",
      "Case #38: 357\n",
      "Case #39: 899\n",
      "Case #40: 399\n",
      "Case #41: 899\n",
      "Case #42: 135\n",
      "Case #43: 899\n",
      "Case #44: 799\n",
      "Case #45: 389\n",
      "Case #46: 179\n",
      "Case #47: 467\n",
      "Case #48: 899\n",
      "Case #49: 579\n",
      "Case #50: 79\n",
      "Case #51: 599\n",
      "Case #52: 469\n",
      "Case #53: 499\n",
      "Case #54: 799\n",
      "Case #55: 599\n",
      "Case #56: 699\n",
      "Case #57: 799\n",
      "Case #58: 556\n",
      "Case #59: 199\n",
      "Case #60: 699\n",
      "Case #61: 1\n",
      "Case #62: 199\n",
      "Case #63: 339\n",
      "Case #64: 599\n",
      "Case #65: 29\n",
      "Case #66: 258\n",
      "Case #67: 799\n",
      "Case #68: 588\n",
      "Case #69: 799\n",
      "Case #70: 399\n",
      "Case #71: 179\n",
      "Case #72: 458\n",
      "Case #73: 269\n",
      "Case #74: 299\n",
      "Case #75: 159\n",
      "Case #76: 333\n",
      "Case #77: 799\n",
      "Case #78: 499\n",
      "Case #79: 599\n",
      "Case #80: 3\n",
      "Case #81: 568\n",
      "Case #82: 599\n",
      "Case #83: 489\n",
      "Case #84: 599\n",
      "Case #85: 599\n",
      "Case #86: 899\n",
      "Case #87: 699\n",
      "Case #88: 599\n",
      "Case #89: 899\n",
      "Case #90: 289\n",
      "Case #91: 699\n",
      "Case #92: 339\n",
      "Case #93: 599\n",
      "Case #94: 899\n",
      "Case #95: 899\n",
      "Case #96: 899\n",
      "Case #97: 699\n",
      "Case #98: 599\n",
      "Case #99: 599\n",
      "Case #100: 799\n",
      "\n"
     ]
    }
   ],
   "source": [
    "lines = data.split()\n",
    "N = int(lines[0])\n",
    "output = ''\n",
    "for i in range(1, N+1):\n",
    "    output += 'Case #' + str(i) + ': ' + str(make_figure(lines[i])) + '\\n'\n",
    "print(output)"
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
    "out_file = 'case_2.txt'\n",
    "\n",
    "with open(out_file, 'w') as f:\n",
    "    f.write(output)"
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
   "version": "3.6.0"
  }
 },
 "nbformat": 4,
 "nbformat_minor": 2
}
