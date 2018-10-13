{
 "cells": [
  {
   "cell_type": "code",
   "execution_count": 116,
   "metadata": {
    "collapsed": false
   },
   "outputs": [],
   "source": [
    "f = open('B-small-attempt1.in','r')\n",
    "g = open('t.txt','w')\n",
    "T = f.readline()\n",
    "for t in range(0,int(T)):\n",
    "    N = list(f.readline().replace(\"\\n\",\"\"))\n",
    "    #if \"0\" in N:\n",
    "        #N = list(\"9\"*(len(N)-1))\n",
    "    #else:\n",
    "    for i in range(0,len(N)-1):\n",
    "        if int(N[i])>int(N[i+1]):\n",
    "            j = i-1\n",
    "            while j!=-1 and int(N[j])==int(N[j+1]):\n",
    "                j = j-1\n",
    "            N[j+1] = str(int(N[j+1])-1)\n",
    "            for k in range(j+2,len(N)):\n",
    "                N[k] = \"9\"\n",
    "            break\n",
    "    g.write(\"Case #%i: %s\" % (t+1,\"\".join(N).lstrip(\"0\")))\n",
    "    if t!=int(T)-1:\n",
    "        g.write(\"\\n\")"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 91,
   "metadata": {
    "collapsed": false
   },
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "364560034560406\n"
     ]
    }
   ],
   "source": [
    "print(\"000364560034560406\".lstrip(\"0\"))"
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
