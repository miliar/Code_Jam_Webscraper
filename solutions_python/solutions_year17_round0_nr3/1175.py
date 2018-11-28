{
 "cells": [
  {
   "cell_type": "code",
   "execution_count": 45,
   "metadata": {
    "collapsed": false
   },
   "outputs": [],
   "source": [
    "f = open('C-small-2-attempt0.in','r')\n",
    "g = open('bath1.txt','w')\n",
    "T = f.readline()\n",
    "for t in range(0,int(T)):\n",
    "    inp = f.readline().replace(\"\\n\",\"\")\n",
    "    N = int(inp.split(\" \")[0])\n",
    "    K = int(inp.split(\" \")[1])\n",
    "    \n",
    "    upperLength = N\n",
    "    lowerLength = N-1\n",
    "    upperNumber = 1\n",
    "    lowerNumber = 0\n",
    "    while upperNumber + lowerNumber <= K/2:\n",
    "        if upperLength % 2 == 0:\n",
    "            newUpperLength = upperLength/2\n",
    "            newLowerLength = (lowerLength-1)/2\n",
    "            newUpperNumber = upperNumber\n",
    "            newLowerNumber = upperNumber+2*lowerNumber\n",
    "        else:\n",
    "            newUpperLength = (upperLength-1)/2\n",
    "            newLowerLength = lowerLength/2-1\n",
    "            newUpperNumber = 2*upperNumber+lowerNumber\n",
    "            newLowerNumber = lowerNumber\n",
    "        upperLength = newUpperLength\n",
    "        lowerLength = newLowerLength\n",
    "        upperNumber = newUpperNumber\n",
    "        lowerNumber = newLowerNumber\n",
    "    if K - (upperNumber+lowerNumber-1)<=upperNumber:\n",
    "        if upperLength % 2 == 0:\n",
    "            maxLength = upperLength/2\n",
    "            minLength = maxLength-1\n",
    "        else:\n",
    "            maxLength = (upperLength-1)/2\n",
    "            minLength = maxLength\n",
    "    else:\n",
    "        if lowerLength % 2 == 0:\n",
    "            maxLength = lowerLength/2\n",
    "            minLength = maxLength-1\n",
    "        else:\n",
    "            maxLength = (lowerLength-1)/2\n",
    "            minLength = maxLength\n",
    "    g.write(\"Case #%i: %i %i\" % (t+1,maxLength,minLength))\n",
    "    if t!=int(T)-1:\n",
    "        g.write(\"\\n\")"
   ]
  }
 ],
 "metadata": {
  "anaconda-cloud": {},
  "kernelspec": {
   "display_name": "Python [conda root]",
   "language": "python",
   "name": "conda-root-py"
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
 "nbformat_minor": 1
}
