{
 "cells": [
  {
   "cell_type": "code",
   "execution_count": 3,
   "metadata": {
    "collapsed": true
   },
   "outputs": [],
   "source": [
    "def alphabetCake(grid):\n",
    "    if not '?' in ''.join(grid):\n",
    "        return grid\n",
    "    gridList = [list(_) for _ in grid]\n",
    "    for rowList in gridList:\n",
    "        if rowList != ['?'] * len(rowList):\n",
    "            while '?' in rowList:\n",
    "                #from right\n",
    "                for i in range(len(rowList) - 1):\n",
    "                    if rowList[i] == '?' and rowList[i + 1] != '?':\n",
    "                        rowList[i] = rowList[i + 1]\n",
    "                        break\n",
    "                #from left\n",
    "                for i in range(1, len(rowList)):\n",
    "                    if rowList[i] == '?' and rowList[i - 1] != '?':\n",
    "                        rowList[i] = rowList[i - 1]\n",
    "                        break\n",
    "    #go down\n",
    "    while ['?'] * len(rowList) in gridList:\n",
    "        for i in range(len(gridList) - 1):\n",
    "            if gridList[i] == ['?'] * len(gridList[0]) and gridList[i + 1] != ['?'] * len(gridList[0]):\n",
    "                gridList[i] = gridList[i + 1]\n",
    "                break\n",
    "        for i in range(1, len(gridList)):\n",
    "            if gridList[i] == ['?'] * len(gridList[0]) and gridList[i - 1] != ['?'] * len(gridList[0]):\n",
    "                gridList[i] = gridList[i - 1]\n",
    "                break\n",
    "    return [''.join(_) for _ in gridList]"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 5,
   "metadata": {
    "collapsed": false
   },
   "outputs": [
    {
     "data": {
      "text/plain": [
       "['EFGH', 'EFGH', 'ABCD', 'ABCD']"
      ]
     },
     "execution_count": 5,
     "metadata": {},
     "output_type": "execute_result"
    }
   ],
   "source": [
    "alphabetCake(['EFGH','????', '????', 'ABCD'] )"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 7,
   "metadata": {
    "collapsed": false
   },
   "outputs": [],
   "source": [
    "inp = open(\"A-large.in\")\n",
    "#inp = open(\"tmp.txt\")\n",
    "out = open(\"output.txt\", 'w')\n",
    "num = int(inp.readline())\n",
    "for i in range(num):\n",
    "    R, C = [int(_) for _ in inp.readline().split(' ')]\n",
    "    grid = []\n",
    "    for j in range(R):\n",
    "        grid.append(inp.readline().strip())\n",
    "    out.write('Case #' + str(i+1) + ': ' + '\\n')\n",
    "    newGrid = alphabetCake(grid)\n",
    "    #print grid, '\\n', newGrid\n",
    "    for j in range(R):\n",
    "        out.write(newGrid[j] + '\\n')\n",
    "        #print grid[j], '   ', newGrid[j]\n",
    "    #print '\\n'\n",
    "inp.close()\n",
    "out.close()"
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
 "nbformat_minor": 0
}
