{
 "cells": [
  {
   "cell_type": "code",
   "execution_count": 2,
   "metadata": {
    "collapsed": true
   },
   "outputs": [],
   "source": [
    "class Node:\n",
    "    def __init__(self):\n",
    "        self.parent = None\n",
    "        self.left = None\n",
    "        self.right = None\n",
    "        self.value = None\n",
    "        \n",
    "    def __init__(self, parent, left, right, value):\n",
    "        self.parent = parent\n",
    "        self.left = left\n",
    "        self.right = right\n",
    "        self.value = value"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 3,
   "metadata": {
    "collapsed": true
   },
   "outputs": [],
   "source": [
    "def find_max_node(node):\n",
    "    if node.left == None and node.right == None:\n",
    "        return node\n",
    "    elif node.left.value >= node.right.value:\n",
    "        node = node.left\n",
    "    else:\n",
    "        node = node.right\n",
    "    return find_max_node(node)\n",
    "\n",
    "def update_max_parents(node):\n",
    "    if node == None:\n",
    "        return\n",
    "    node.value = max(node.left.value, node.right.value)\n",
    "    update_max_parents(node.parent)\n",
    "\n",
    "class Tree:\n",
    "    def __init__(self, init_size):\n",
    "        self.root = Node(None, None, None, init_size)\n",
    "        \n",
    "    def insert_user(self):\n",
    "        # get max interval length\n",
    "        max_ = self.root.value\n",
    "        Ls = (max_-1) // 2\n",
    "        Rs = max_ // 2\n",
    "        \n",
    "        # split interval\n",
    "        max_node = find_max_node(self.root)\n",
    "        \n",
    "        # create 2 new nodes\n",
    "        left = Node(max_node, None, None, Ls)\n",
    "        right = Node(max_node, None, None, Rs)\n",
    "        max_node.left = left\n",
    "        max_node.right = right\n",
    "        \n",
    "        # update max and parents\n",
    "        max_node.value = Ls if Ls >= Rs else Rs\n",
    "        update_max_parents(max_node.parent)\n",
    "        \n",
    "        # return Ls and Rs\n",
    "        return (Ls, Rs)"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 14,
   "metadata": {
    "collapsed": true
   },
   "outputs": [],
   "source": [
    "N = 1000\n",
    "K = 1\n",
    "tree = Tree(N)"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 15,
   "metadata": {
    "collapsed": false
   },
   "outputs": [],
   "source": [
    "last_output = None\n",
    "for i in range(K):\n",
    "    last_output = tree.insert_user()"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 16,
   "metadata": {
    "collapsed": false
   },
   "outputs": [
    {
     "data": {
      "text/plain": [
       "(499, 500)"
      ]
     },
     "execution_count": 16,
     "metadata": {},
     "output_type": "execute_result"
    }
   ],
   "source": [
    "last_output"
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
  },
  {
   "cell_type": "code",
   "execution_count": 27,
   "metadata": {
    "collapsed": true
   },
   "outputs": [],
   "source": [
    "import csv\n",
    "# get data\n",
    "csvfile = open(\"stalls0.in\", 'r')\n",
    "reader = csv.reader(csvfile, delimiter=' ')\n",
    "input_ = list(reader)"
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
    "# parse data\n",
    "T = int(input_[0][0])\n",
    "data = input_[1:]"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 31,
   "metadata": {
    "collapsed": false
   },
   "outputs": [],
   "source": [
    "store = []\n",
    "for line in data:\n",
    "    N = int(line[0])\n",
    "    K = int(line[1])\n",
    "    tree = Tree(N)\n",
    "    last_output = None\n",
    "    for i in range(K):\n",
    "        last_output = tree.insert_user()\n",
    "    y = max(last_output)\n",
    "    z = min(last_output)\n",
    "    store.append((y, z))"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 34,
   "metadata": {
    "collapsed": false
   },
   "outputs": [
    {
     "ename": "TypeError",
     "evalue": "Can't convert 'int' object to str implicitly",
     "output_type": "error",
     "traceback": [
      "\u001b[0;31m---------------------------------------------------------------------------\u001b[0m",
      "\u001b[0;31mTypeError\u001b[0m                                 Traceback (most recent call last)",
      "\u001b[0;32m<ipython-input-34-faa0ede16a90>\u001b[0m in \u001b[0;36m<module>\u001b[0;34m()\u001b[0m\n\u001b[1;32m      4\u001b[0m     \u001b[0;32mif\u001b[0m \u001b[0mi\u001b[0m \u001b[0;34m!=\u001b[0m \u001b[0;36m0\u001b[0m\u001b[0;34m:\u001b[0m\u001b[0;34m\u001b[0m\u001b[0m\n\u001b[1;32m      5\u001b[0m         \u001b[0mtarget\u001b[0m\u001b[0;34m.\u001b[0m\u001b[0mwrite\u001b[0m\u001b[0;34m(\u001b[0m\u001b[0;34m'\\n'\u001b[0m\u001b[0;34m)\u001b[0m\u001b[0;34m\u001b[0m\u001b[0m\n\u001b[0;32m----> 6\u001b[0;31m     \u001b[0mtarget\u001b[0m\u001b[0;34m.\u001b[0m\u001b[0mwrite\u001b[0m\u001b[0;34m(\u001b[0m\u001b[0;34m'Case #'\u001b[0m \u001b[0;34m+\u001b[0m \u001b[0mstr\u001b[0m\u001b[0;34m(\u001b[0m\u001b[0mi\u001b[0m\u001b[0;34m+\u001b[0m\u001b[0;36m1\u001b[0m\u001b[0;34m)\u001b[0m \u001b[0;34m+\u001b[0m \u001b[0;34m': '\u001b[0m \u001b[0;34m+\u001b[0m \u001b[0mstore\u001b[0m\u001b[0;34m[\u001b[0m\u001b[0mi\u001b[0m\u001b[0;34m]\u001b[0m\u001b[0;34m[\u001b[0m\u001b[0;36m0\u001b[0m\u001b[0;34m]\u001b[0m \u001b[0;34m+\u001b[0m \u001b[0;34m\" \"\u001b[0m \u001b[0;34m+\u001b[0m \u001b[0mstore\u001b[0m\u001b[0;34m[\u001b[0m\u001b[0mi\u001b[0m\u001b[0;34m]\u001b[0m\u001b[0;34m[\u001b[0m\u001b[0;36m1\u001b[0m\u001b[0;34m]\u001b[0m\u001b[0;34m)\u001b[0m\u001b[0;34m\u001b[0m\u001b[0m\n\u001b[0m",
      "\u001b[0;31mTypeError\u001b[0m: Can't convert 'int' object to str implicitly"
     ]
    }
   ],
   "source": [
    "# write to file\n",
    "target = open(\"stalls.out\", 'w')\n",
    "for i in range(len(store)):\n",
    "    if i != 0:\n",
    "        target.write('\\n')\n",
    "    target.write('Case #' + str(i+1) + ': ' + str(store[i][0]) + \" \" + str(store[i][1])"
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
   "version": "3.5.3"
  }
 },
 "nbformat": 4,
 "nbformat_minor": 0
}
