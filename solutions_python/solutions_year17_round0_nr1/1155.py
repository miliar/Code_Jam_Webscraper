{
 "cells": [
  {
   "cell_type": "code",
   "execution_count": 24,
   "metadata": {
    "collapsed": false
   },
   "outputs": [],
   "source": [
    "f = open('A-small-attempt0.in','r')\n",
    "g = open('pan1.txt','w')\n",
    "T = f.readline()\n",
    "for t in range(0,int(T)):\n",
    "    inp_str = f.readline().replace(\"\\n\",\"\")\n",
    "    signs = inp_str.split(\" \")[0]\n",
    "    size = int(inp_str.split(\" \")[1])\n",
    "    signs_list = list(signs)\n",
    "    flips = 0\n",
    "    for i in range(0,len(signs_list)-size+1):\n",
    "        if signs_list[i] == \"-\":\n",
    "            for j in range(0,size):\n",
    "                if signs_list[i+j] == \"+\":\n",
    "                    signs_list[i+j] = \"-\"\n",
    "                else:\n",
    "                    signs_list[i+j] = \"+\"\n",
    "            flips = flips + 1\n",
    "    \n",
    "    if \"-\" in signs_list[-size+1:]:\n",
    "        output = \"IMPOSSIBLE\"\n",
    "    else:\n",
    "        output = str(flips)\n",
    "        \n",
    "    \n",
    "    g.write(\"Case #%i: %s\" % (t+1,output))\n",
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
