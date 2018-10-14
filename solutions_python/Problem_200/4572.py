{
 "cells": [
  {
   "cell_type": "code",
   "execution_count": 47,
   "metadata": {
    "collapsed": false
   },
   "outputs": [],
   "source": []
  },
  {
   "cell_type": "code",
   "execution_count": 59,
   "metadata": {
    "collapsed": false
   },
   "outputs": [],
   "source": [
    "def getBigTidy(s):\n",
    "    length=len(s)\n",
    "    t=1\n",
    "    b=0\n",
    "    a=0\n",
    "    while t>0 and t<length:\n",
    "        if int(s[t])==int(s[t-1]):            \n",
    "            t+=1\n",
    "        elif int(s[t])-int(s[t-1])>=0:\n",
    "            b=t\n",
    "            t+=1           \n",
    "        else:\n",
    "            t=0\n",
    "            a=1\n",
    "    return([b,a])\n",
    "\n",
    "        "
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 60,
   "metadata": {
    "collapsed": false
   },
   "outputs": [],
   "source": [
    "def BigTidy(s):\n",
    "    K=getBigTidy(s)\n",
    "    a=K[1]\n",
    "    if a==0:\n",
    "        return(int(s))\n",
    "    else:\n",
    "        b=K[0]\n",
    "        L=s[0:b]\n",
    "        newb=str(int(s[b])-1)\n",
    "        L+=newb\n",
    "        L+='9'*(len(s)-(b+1))\n",
    "        return(int(L))\n",
    "        "
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 70,
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
      "Case #4: 99999999999999999\n",
      "Case #5: 1\n",
      "Case #6: 1112333449999999\n",
      "Case #7: 179999999999999999\n",
      "Case #8: 127999999999999999\n",
      "Case #9: 79999999999\n",
      "Case #10: 11199\n",
      "Case #11: 999999999999999999\n",
      "Case #12: 19999999999999999\n",
      "Case #13: 14589\n",
      "Case #14: 39999999999999999\n",
      "Case #15: 24666999999\n",
      "Case #16: 499999999999999999\n",
      "Case #17: 399999999999999999\n",
      "Case #18: 69999999999999999\n",
      "Case #19: 39999\n",
      "Case #20: 23444555889\n",
      "Case #21: 59\n",
      "Case #22: 111233447788899999\n",
      "Case #23: 399999999999999999\n",
      "Case #24: 1122445555566699\n",
      "Case #25: 99999999999999999\n",
      "Case #26: 9\n",
      "Case #27: 159999999999999999\n",
      "Case #28: 299\n",
      "Case #29: 799999999999999999\n",
      "Case #30: 12233344449999999\n",
      "Case #31: 999999999999999999\n",
      "Case #32: 799999999999999999\n",
      "Case #33: 199999999999999999\n",
      "Case #34: 459999999999999999\n",
      "Case #35: 1145999999999999\n",
      "Case #36: 599999999999999999\n",
      "Case #37: 69\n",
      "Case #38: 699999999999999999\n",
      "Case #39: 499999999999999999\n",
      "Case #40: 599\n",
      "Case #41: 69999\n",
      "Case #42: 11222444499\n",
      "Case #43: 339999999999999999\n",
      "Case #44: 599999999999999999\n",
      "Case #45: 179999999999999999\n",
      "Case #46: 6999999999999999\n",
      "Case #47: 11334456666777889\n",
      "Case #48: 17899\n",
      "Case #49: 148999999999999999\n",
      "Case #50: 36788\n",
      "Case #51: 899999999999999999\n",
      "Case #52: 799\n",
      "Case #53: 99\n",
      "Case #54: 11144466799999999\n",
      "Case #55: 12455599999\n",
      "Case #56: 99999999999999999\n",
      "Case #57: 4999999999999999\n",
      "Case #58: 34445599999\n",
      "Case #59: 39\n",
      "Case #60: 779999999999999999\n",
      "Case #61: 117\n",
      "Case #62: 19\n",
      "Case #63: 29999999999999999\n",
      "Case #64: 99999999999999999\n",
      "Case #65: 599999999999999999\n",
      "Case #66: 111222233339999999\n",
      "Case #67: 7999999999999999\n",
      "Case #68: 69999999999999999\n",
      "Case #69: 69999\n",
      "Case #70: 199999999999999999\n",
      "Case #71: 699\n",
      "Case #72: 29999999999\n",
      "Case #73: 2677888999999999\n",
      "Case #74: 79999999999\n",
      "Case #75: 122899999999999999\n",
      "Case #76: 11112333444559999\n",
      "Case #77: 7999999999999999\n",
      "Case #78: 35666699999\n",
      "Case #79: 299999999999999999\n",
      "Case #80: 789999999999999999\n",
      "Case #81: 11122345556779999\n",
      "Case #82: 3999999999999999\n",
      "Case #83: 589999999999999999\n",
      "Case #84: 199999999999999999\n",
      "Case #85: 799999999999999999\n",
      "Case #86: 899999999999999999\n",
      "Case #87: 499999999999999999\n",
      "Case #88: 299999999999999999\n",
      "Case #89: 19999999999\n",
      "Case #90: 1699999999999999\n",
      "Case #91: 59\n",
      "Case #92: 599999999999999999\n",
      "Case #93: 389999999999999999\n",
      "Case #94: 99999999999999999\n",
      "Case #95: 11122334588899999\n",
      "Case #96: 59999\n",
      "Case #97: 1133445556666999\n",
      "Case #98: 699999999999999999\n",
      "Case #99: 25999999999\n",
      "Case #100: 159999999999999999\n"
     ]
    }
   ],
   "source": [
    "file=open(\"B-large.in\", \"r\")\n",
    "ansFile=open(\"tidyAnswer.txt\", \"w\")\n",
    "\n",
    "T=int(file.readline())\n",
    "for i in range(1,T+1):\n",
    "    newTidy=BigTidy(file.readline().rstrip())\n",
    "    print(\"Case #%d: %d\" % (i,newTidy))\n",
    "    ansFile.write(\"Case #%d: %d\\n\" % (i,newTidy))\n",
    "    \n",
    "ansFile.close()\n",
    "file.close()"
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
    "\n"
   ]
  }
 ],
 "metadata": {
  "kernelspec": {
   "display_name": "Python [Root]",
   "language": "python",
   "name": "Python [Root]"
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
 "nbformat_minor": 0
}
