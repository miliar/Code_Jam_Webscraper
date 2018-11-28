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
    "def tidy(n):\n",
    "    return sorted(list(str(n)))==list(str(n))"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 2,
   "metadata": {
    "collapsed": true
   },
   "outputs": [],
   "source": [
    "def find_tidy(n):\n",
    "    for i in range(n, 0, -1):\n",
    "        if tidy(i):\n",
    "            return i"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 10,
   "metadata": {
    "collapsed": true
   },
   "outputs": [],
   "source": [
    "def main(num_cases, cases):\n",
    "    for i in range(int(num_cases)):\n",
    "        print('Case #'+str(i+1)+': '+str(find_tidy(int(cases[i]))))"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 4,
   "metadata": {
    "collapsed": false
   },
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "4\n",
      "132\n",
      "Case #1: 129\n",
      "1000\n",
      "Case #2: 999\n",
      "7\n",
      "Case #3: 7\n",
      "111111111111111110\n"
     ]
    },
    {
     "ename": "KeyboardInterrupt",
     "evalue": "",
     "output_type": "error",
     "traceback": [
      "\u001b[0;31m---------------------------------------------------------------------------\u001b[0m",
      "\u001b[0;31mKeyboardInterrupt\u001b[0m                         Traceback (most recent call last)",
      "\u001b[0;32m<ipython-input-4-58ca95c5b364>\u001b[0m in \u001b[0;36m<module>\u001b[0;34m()\u001b[0m\n\u001b[0;32m----> 1\u001b[0;31m \u001b[0mmain\u001b[0m\u001b[0;34m(\u001b[0m\u001b[0;34m)\u001b[0m\u001b[0;34m\u001b[0m\u001b[0m\n\u001b[0m",
      "\u001b[0;32m<ipython-input-3-28977a0200e0>\u001b[0m in \u001b[0;36mmain\u001b[0;34m()\u001b[0m\n\u001b[1;32m      3\u001b[0m     \u001b[0;32mfor\u001b[0m \u001b[0mi\u001b[0m \u001b[0;32min\u001b[0m \u001b[0mrange\u001b[0m\u001b[0;34m(\u001b[0m\u001b[0mnum_cases\u001b[0m\u001b[0;34m)\u001b[0m\u001b[0;34m:\u001b[0m\u001b[0;34m\u001b[0m\u001b[0m\n\u001b[1;32m      4\u001b[0m         \u001b[0mn\u001b[0m \u001b[0;34m=\u001b[0m \u001b[0mint\u001b[0m\u001b[0;34m(\u001b[0m\u001b[0minput\u001b[0m\u001b[0;34m(\u001b[0m\u001b[0;34m)\u001b[0m\u001b[0;34m)\u001b[0m\u001b[0;34m\u001b[0m\u001b[0m\n\u001b[0;32m----> 5\u001b[0;31m         \u001b[0mprint\u001b[0m\u001b[0;34m(\u001b[0m\u001b[0;34m'Case #'\u001b[0m\u001b[0;34m+\u001b[0m\u001b[0mstr\u001b[0m\u001b[0;34m(\u001b[0m\u001b[0mi\u001b[0m\u001b[0;34m+\u001b[0m\u001b[0;36m1\u001b[0m\u001b[0;34m)\u001b[0m\u001b[0;34m+\u001b[0m\u001b[0;34m': '\u001b[0m\u001b[0;34m+\u001b[0m\u001b[0mstr\u001b[0m\u001b[0;34m(\u001b[0m\u001b[0mfind_tidy\u001b[0m\u001b[0;34m(\u001b[0m\u001b[0mn\u001b[0m\u001b[0;34m)\u001b[0m\u001b[0;34m)\u001b[0m\u001b[0;34m)\u001b[0m\u001b[0;34m\u001b[0m\u001b[0m\n\u001b[0m",
      "\u001b[0;32m<ipython-input-2-cb0db355c1ec>\u001b[0m in \u001b[0;36mfind_tidy\u001b[0;34m(n)\u001b[0m\n\u001b[1;32m      1\u001b[0m \u001b[0;32mdef\u001b[0m \u001b[0mfind_tidy\u001b[0m\u001b[0;34m(\u001b[0m\u001b[0mn\u001b[0m\u001b[0;34m)\u001b[0m\u001b[0;34m:\u001b[0m\u001b[0;34m\u001b[0m\u001b[0m\n\u001b[1;32m      2\u001b[0m     \u001b[0;32mfor\u001b[0m \u001b[0mi\u001b[0m \u001b[0;32min\u001b[0m \u001b[0mrange\u001b[0m\u001b[0;34m(\u001b[0m\u001b[0mn\u001b[0m\u001b[0;34m,\u001b[0m \u001b[0;36m0\u001b[0m\u001b[0;34m,\u001b[0m \u001b[0;34m-\u001b[0m\u001b[0;36m1\u001b[0m\u001b[0;34m)\u001b[0m\u001b[0;34m:\u001b[0m\u001b[0;34m\u001b[0m\u001b[0m\n\u001b[0;32m----> 3\u001b[0;31m         \u001b[0;32mif\u001b[0m \u001b[0mtidy\u001b[0m\u001b[0;34m(\u001b[0m\u001b[0mi\u001b[0m\u001b[0;34m)\u001b[0m\u001b[0;34m:\u001b[0m\u001b[0;34m\u001b[0m\u001b[0m\n\u001b[0m\u001b[1;32m      4\u001b[0m             \u001b[0;32mreturn\u001b[0m \u001b[0mi\u001b[0m\u001b[0;34m\u001b[0m\u001b[0m\n",
      "\u001b[0;31mKeyboardInterrupt\u001b[0m: "
     ]
    }
   ],
   "source": [
    "main()"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 11,
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
      "Case #4: 66\n",
      "Case #5: 779\n",
      "Case #6: 558\n",
      "Case #7: 199\n",
      "Case #8: 899\n",
      "Case #9: 799\n",
      "Case #10: 599\n",
      "Case #11: 789\n",
      "Case #12: 289\n",
      "Case #13: 134\n",
      "Case #14: 189\n",
      "Case #15: 899\n",
      "Case #16: 277\n",
      "Case #17: 899\n",
      "Case #18: 199\n",
      "Case #19: 599\n",
      "Case #20: 699\n",
      "Case #21: 128\n",
      "Case #22: 379\n",
      "Case #23: 679\n",
      "Case #24: 699\n",
      "Case #25: 279\n",
      "Case #26: 368\n",
      "Case #27: 8\n",
      "Case #28: 299\n",
      "Case #29: 127\n",
      "Case #30: 499\n",
      "Case #31: 1\n",
      "Case #32: 669\n",
      "Case #33: 799\n",
      "Case #34: 599\n",
      "Case #35: 799\n",
      "Case #36: 359\n",
      "Case #37: 889\n",
      "Case #38: 469\n",
      "Case #39: 279\n",
      "Case #40: 899\n",
      "Case #41: 149\n",
      "Case #42: 444\n",
      "Case #43: 489\n",
      "Case #44: 689\n",
      "Case #45: 149\n",
      "Case #46: 589\n",
      "Case #47: 688\n",
      "Case #48: 555\n",
      "Case #49: 299\n",
      "Case #50: 469\n",
      "Case #51: 799\n",
      "Case #52: 399\n",
      "Case #53: 69\n",
      "Case #54: 29\n",
      "Case #55: 567\n",
      "Case #56: 899\n",
      "Case #57: 199\n",
      "Case #58: 179\n",
      "Case #59: 779\n",
      "Case #60: 449\n",
      "Case #61: 669\n",
      "Case #62: 399\n",
      "Case #63: 135\n",
      "Case #64: 699\n",
      "Case #65: 599\n",
      "Case #66: 899\n",
      "Case #67: 235\n",
      "Case #68: 158\n",
      "Case #69: 699\n",
      "Case #70: 999\n",
      "Case #71: 799\n",
      "Case #72: 259\n",
      "Case #73: 56\n",
      "Case #74: 399\n",
      "Case #75: 699\n",
      "Case #76: 129\n",
      "Case #77: 239\n",
      "Case #78: 479\n",
      "Case #79: 899\n",
      "Case #80: 699\n",
      "Case #81: 599\n",
      "Case #82: 299\n",
      "Case #83: 79\n",
      "Case #84: 599\n",
      "Case #85: 899\n",
      "Case #86: 389\n",
      "Case #87: 339\n",
      "Case #88: 599\n",
      "Case #89: 599\n",
      "Case #90: 779\n",
      "Case #91: 289\n",
      "Case #92: 159\n",
      "Case #93: 699\n",
      "Case #94: 399\n",
      "Case #95: 499\n",
      "Case #96: 199\n",
      "Case #97: 699\n",
      "Case #98: 799\n",
      "Case #99: 499\n",
      "Case #100: 778\n"
     ]
    }
   ],
   "source": [
    "with open('B-small-attempt0.in') as f:\n",
    "    text = f.read()\n",
    "    text = text.split('\\n')\n",
    "    main(text[0], text[1:])"
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
   "version": "3.5.2"
  }
 },
 "nbformat": 4,
 "nbformat_minor": 2
}
