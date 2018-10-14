{
 "cells": [
  {
   "cell_type": "markdown",
   "metadata": {},
   "source": []
  },
  {
   "cell_type": "code",
   "execution_count": 63,
   "metadata": {
    "collapsed": false
   },
   "outputs": [],
   "source": [
    "def readInput(filename):\n",
    "    f=open(filename, 'r')\n",
    "    inputVals=f.read()\n",
    "    f.close()\n",
    "    inputList=[]\n",
    "    string=''\n",
    "    for i in xrange(len(inputVals)):\n",
    "        if inputVals[i]=='\\n':\n",
    "            inputList.append(string)\n",
    "            string=''\n",
    "        else:\n",
    "            string+=inputVals[i]\n",
    "\n",
    "    if string !='': #otherwise extra new line at EOF can cause failure.\n",
    "        inputList.append(string)\n",
    "    if len(inputList)!=3*int(inputList[0])+1:\n",
    "        print \"Error! Length mismatch.\"\n",
    "    del inputList[0]\n",
    "    return inputList"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 88,
   "metadata": {
    "collapsed": true
   },
   "outputs": [],
   "source": [
    "def parseInput(inputList):\n",
    "    #make sure you don't accidently assume things like\n",
    "    #numbers are only one character long\n",
    "    parsedInput=[]\n",
    "    lineN=0\n",
    "    while lineN<len(inputList):\n",
    "        N,K=inputList[lineN].split()\n",
    "        N=int(N)\n",
    "        K=int(K)\n",
    "        U=float(inputList[lineN+1])\n",
    "        P=inputList[lineN+2].split()\n",
    "        P=[float(val) for val in P]\n",
    "        parsedInput.append( (N,K,U,P) )\n",
    "        lineN+=3\n",
    "    assert lineN==len(inputList)\n",
    "    return parsedInput"
   ]
  },
  {
   "cell_type": "markdown",
   "metadata": {
    "collapsed": false
   },
   "source": [
    ".09\n",
    ".9,.1,.1\n",
    "1/3\n",
    ".99+.(1-.99)*(0.1+0.1)=.992\n",
    ".9,.19,.1\n",
    ".9+(1-.9)*(.19+.1)=.929\n",
    "2/3\n",
    ".99*.1+.99*.1+.1*.1=.208\n",
    ".9*.1+.9*.19+.19*.1=.28\n",
    ".9*.145+.9*.145+.145*.145=.282025\n",
    "^actually wrong\n",
    ".99*.1*(1-.1)+.99*.1*(1-.1)+.1*.1*(1-.99)=.1783\n",
    ".9*.1*(1-.19)+.9*.19*(1-.1)+.19*.1*(1-.9)=.2287\n",
    ".9*.145*(1-.145)+.9*.145*(1-.145)+.145*.145*(1-.9)+.145*.145*.9=.24418\n",
    "\n",
    "f(xyz..)=xy+yz+xz-> df=(xdy+ydx)...\n",
    "g(x1,x2...;k)=Sigma(k,n) x1*x2*...*xk*(1-x_k+1)...*(1-xn)=Sigma x1*...xk -x1*..*x_k+1 (+/- alternating decreasing) x1...xn \n",
    "f(x1,..x2)=sigma(k>=K) g(x1,x2...;k)\n",
    "\n",
    "(x-a)*(y+a), (1-x+a)*(y+a), (x-a)*(1-y-a), (1-x+a)*(1-y-a)\n",
    "p=xy+a(x-y)-a^2, y+a-p, x-a-p, p+1-y-x\n",
    "Sum=1\n",
    "\n",
    "\n",
    "x1...xn appear symmetrically throughout the various terms. changing a middling value i think is always nonoptimal but we can easily verify\n",
    "thus depending on the case we either always add to the minimum value or the maximum value\n",
    "if max, increase until its 1 then increase next max so on and so forth\n",
    "if min increase until its equal to 2nd min then increase both evenly until 3rd and so on and so forth"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 65,
   "metadata": {
    "collapsed": true
   },
   "outputs": [],
   "source": [
    "def main(inputList):\n",
    "    f=open(outputFile, 'w')\n",
    "    for i,inp in enumerate(inputList):\n",
    "        out=solveProblem(inp)\n",
    "        string=\"Case #{0}: {1}\\n\".format(i+1, out)\n",
    "        f.write(string)\n",
    "    f.close()"
   ]
  },
  {
   "cell_type": "markdown",
   "metadata": {},
   "source": []
  },
  {
   "cell_type": "code",
   "execution_count": 66,
   "metadata": {
    "collapsed": false
   },
   "outputs": [],
   "source": [
    "from itertools import combinations\n",
    "def calcProbability(N,K,P):\n",
    "    assert N==len(P)\n",
    "    sum=0\n",
    "    for k_prime in range(K,N+1):\n",
    "        index_iterator=combinations(range(N),k_prime)\n",
    "        for indices in index_iterator:\n",
    "            indices=frozenset(indices)\n",
    "            term=1\n",
    "            for i in range(N):\n",
    "                term*=P[i] if (i in indices) else (1-P[i])\n",
    "            sum+=term\n",
    "    return sum"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 91,
   "metadata": {
    "collapsed": false
   },
   "outputs": [],
   "source": [
    "from copy import copy\n",
    "def solveProblem(inp):\n",
    "    N,K,U,P=inp\n",
    "    P.sort()\n",
    "    old_P=copy(P)\n",
    "    old_U=U\n",
    "    i=0\n",
    "    P.append(1.0)#hack\n",
    "    while U>10**-10:\n",
    "        diff=min((i+1.0)*(P[i+1]-P[i]),U)\n",
    "        U-=diff\n",
    "        diff/=(i+1.0)\n",
    "        for j in range(i+1):\n",
    "            P[j]+=diff\n",
    "        i+=1\n",
    "    del P[-1]\n",
    "    ascending_answer=calcProbability(N,K,P)\n",
    "    P=old_P\n",
    "    U=old_U\n",
    "    P.sort(reverse=True)\n",
    "    i=0\n",
    "    while U>10**-10:\n",
    "        diff=min(1.-P[i],U)\n",
    "        U-=diff\n",
    "        P[i]+=diff\n",
    "        i+=1\n",
    "    descending_answer=calcProbability(N,K,P)\n",
    "    return max(ascending_answer,descending_answer)"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 68,
   "metadata": {
    "collapsed": false
   },
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "0.1\n",
      "0.1\n",
      "0.75 0.76\n"
     ]
    },
    {
     "data": {
      "text/plain": [
       "0.76"
      ]
     },
     "execution_count": 68,
     "metadata": {},
     "output_type": "execute_result"
    }
   ],
   "source": [
    "solveProblem((2,1,.1,[0.5,.4]))"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "metadata": {
    "collapsed": false
   },
   "outputs": [],
   "source": []
  },
  {
   "cell_type": "code",
   "execution_count": 94,
   "metadata": {
    "collapsed": false
   },
   "outputs": [],
   "source": [
    "filename='C-small-1-attempt0'\n",
    "outputFile=filename+'.out'\n",
    "inputFile=filename+'.in'\n",
    "inputList=parseInput(readInput(inputFile))"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 95,
   "metadata": {
    "collapsed": false
   },
   "outputs": [],
   "source": [
    "main(inputList)"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 23,
   "metadata": {
    "collapsed": false
   },
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "Help on class combinations in module itertools:\n",
      "\n",
      "class combinations(__builtin__.object)\n",
      " |  combinations(iterable, r) --> combinations object\n",
      " |  \n",
      " |  Return successive r-length combinations of elements in the iterable.\n",
      " |  \n",
      " |  combinations(range(4), 3) --> (0,1,2), (0,1,3), (0,2,3), (1,2,3)\n",
      " |  \n",
      " |  Methods defined here:\n",
      " |  \n",
      " |  __getattribute__(...)\n",
      " |      x.__getattribute__('name') <==> x.name\n",
      " |  \n",
      " |  __iter__(...)\n",
      " |      x.__iter__() <==> iter(x)\n",
      " |  \n",
      " |  next(...)\n",
      " |      x.next() -> the next value, or raise StopIteration\n",
      " |  \n",
      " |  ----------------------------------------------------------------------\n",
      " |  Data and other attributes defined here:\n",
      " |  \n",
      " |  __new__ = <built-in method __new__ of type object>\n",
      " |      T.__new__(S, ...) -> a new object with type S, a subtype of T\n",
      "\n"
     ]
    }
   ],
   "source": [
    "from itertools import combinations\n",
    "help(combinations)"
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
  "anaconda-cloud": {},
  "kernelspec": {
   "display_name": "Python [default]",
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
   "version": "2.7.11"
  }
 },
 "nbformat": 4,
 "nbformat_minor": 1
}
