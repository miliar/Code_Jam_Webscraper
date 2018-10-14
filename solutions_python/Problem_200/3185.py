{
 "cells": [
  {
   "cell_type": "code",
   "execution_count": 2,
   "metadata": {
    "collapsed": false,
    "deletable": true,
    "editable": true
   },
   "outputs": [
    {
     "data": {
      "text/html": [
       "<div>\n",
       "<table border=\"1\" class=\"dataframe\">\n",
       "  <thead>\n",
       "    <tr style=\"text-align: right;\">\n",
       "      <th></th>\n",
       "      <th>n</th>\n",
       "    </tr>\n",
       "  </thead>\n",
       "  <tbody>\n",
       "    <tr>\n",
       "      <th>0</th>\n",
       "      <td>132</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>1</th>\n",
       "      <td>1000</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>2</th>\n",
       "      <td>7</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>3</th>\n",
       "      <td>111111111111111110</td>\n",
       "    </tr>\n",
       "  </tbody>\n",
       "</table>\n",
       "</div>"
      ],
      "text/plain": [
       "                    n\n",
       "0                 132\n",
       "1                1000\n",
       "2                   7\n",
       "3  111111111111111110"
      ]
     },
     "execution_count": 2,
     "metadata": {},
     "output_type": "execute_result"
    }
   ],
   "source": [
    "import pandas as pd\n",
    "import numpy as np\n",
    "test = pd.read_csv(\"test.in\") # don't want first line\n",
    "test.columns = ['n']\n",
    "test"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 81,
   "metadata": {
    "collapsed": false
   },
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "101010\n",
      "99999\n"
     ]
    }
   ],
   "source": [
    "'''Find the largest tidy number smaller than or equal to n'''\n",
    "def find_tidy(n):\n",
    "    digits = list(map(int,str(n)))\n",
    "    if (len(digits)==1):\n",
    "        return(n)\n",
    "    else:\n",
    "        diff = np.diff(digits)\n",
    "        if (sum(diff<0)==0):\n",
    "            return(n)\n",
    "        else:\n",
    "            tidy = np.argmax(diff<0)\n",
    "            diff_rev_tidy = diff[0:tidy][::-1]\n",
    "            is_inc = diff_rev_tidy > 0\n",
    "            #if(len(is_inc) == 0 or sum(1*is_inc) == 0): # no increasing portion in tidy\n",
    "            if (len(is_inc) == 0): # no tidy portion \n",
    "                tidy = 0\n",
    "                flat = 0\n",
    "            elif (sum(1*is_inc)==0): # no increasing portion\n",
    "                flat = tidy\n",
    "            else:\n",
    "                flat = np.argmax(is_inc) # length of any trailing flat's (part of tidy that is non-increasing nor decreasing)\n",
    "            k = len(digits) - tidy + flat - 1\n",
    "            m = ((digits[len(digits) - k - 1])*(10**k)) - 1\n",
    "            #print((digits[len(digits) - k - 1])*(10**k))\n",
    "            #print(\"Tidy: \", tidy)\n",
    "            #print(\"Flat: \", flat)\n",
    "            #print(\"k: \", k)\n",
    "            #print(\"m: \", m)\n",
    "            #print(is_inc)\n",
    "            fixed = list(map(int,str(m)))\n",
    "            #print(fixed)\n",
    "            if (tidy - flat == 0):\n",
    "                joined = fixed\n",
    "            else:\n",
    "                joined = np.concatenate([digits[0:(tidy-flat)],fixed],0)\n",
    "            joined = \"\".join(map(str,joined))\n",
    "            return(joined)\n",
    "n = 101010\n",
    "print(n)\n",
    "print(find_tidy(n))"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 82,
   "metadata": {
    "collapsed": false,
    "deletable": true,
    "editable": true
   },
   "outputs": [
    {
     "data": {
      "text/plain": [
       "'Case #1: 10'"
      ]
     },
     "execution_count": 82,
     "metadata": {},
     "output_type": "execute_result"
    }
   ],
   "source": [
    "'''Format output'''\n",
    "def format_output(i,s):\n",
    "    return(\"Case #\"+str(i)+\": \"+str(s))\n",
    "format_output(1,10)"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 83,
   "metadata": {
    "collapsed": false,
    "deletable": true,
    "editable": true
   },
   "outputs": [
    {
     "data": {
      "text/plain": [
       "0                  Case #1: 129\n",
       "1                  Case #2: 999\n",
       "2                    Case #3: 7\n",
       "3    Case #4: 99999999999999999\n",
       "dtype: object"
      ]
     },
     "execution_count": 83,
     "metadata": {},
     "output_type": "execute_result"
    }
   ],
   "source": [
    "#test.apply(lambda x: format_output(x.index, find_tidy(x['n'])))\n",
    "#test['n'].map(lambda x: find_tidy(x))\n",
    "output = test.apply(lambda x: format_output(x.name + 1, find_tidy(x.n)), axis = 1)\n",
    "output.head()"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 84,
   "metadata": {
    "collapsed": false,
    "deletable": true,
    "editable": true
   },
   "outputs": [
    {
     "data": {
      "text/html": [
       "<div>\n",
       "<table border=\"1\" class=\"dataframe\">\n",
       "  <thead>\n",
       "    <tr style=\"text-align: right;\">\n",
       "      <th></th>\n",
       "      <th>n</th>\n",
       "    </tr>\n",
       "  </thead>\n",
       "  <tbody>\n",
       "    <tr>\n",
       "      <th>0</th>\n",
       "      <td>132</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>1</th>\n",
       "      <td>1000</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>2</th>\n",
       "      <td>7</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>3</th>\n",
       "      <td>111111111111111110</td>\n",
       "    </tr>\n",
       "  </tbody>\n",
       "</table>\n",
       "</div>"
      ],
      "text/plain": [
       "                    n\n",
       "0                 132\n",
       "1                1000\n",
       "2                   7\n",
       "3  111111111111111110"
      ]
     },
     "execution_count": 84,
     "metadata": {},
     "output_type": "execute_result"
    }
   ],
   "source": [
    "output.to_csv(\"test.out\", index = False, header = False)\n",
    "test"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 86,
   "metadata": {
    "collapsed": false,
    "deletable": true,
    "editable": true
   },
   "outputs": [
    {
     "data": {
      "text/plain": [
       "0    Case #1: 129\n",
       "1    Case #2: 999\n",
       "2      Case #3: 7\n",
       "3    Case #4: 299\n",
       "4    Case #5: 899\n",
       "dtype: object"
      ]
     },
     "execution_count": 86,
     "metadata": {},
     "output_type": "execute_result"
    }
   ],
   "source": [
    "# running it\n",
    "filename = \"B-small-attempt0\"\n",
    "input = pd.read_csv(filename + \".in\") # don't want first line\n",
    "input.columns = ['n']\n",
    "output = input.apply(lambda x: format_output(x.name + 1, find_tidy(x.n)), axis = 1)\n",
    "output.to_csv(filename + \".out\", index = False, header = False)\n",
    "output.head()"
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
   "version": "3.5.3"
  }
 },
 "nbformat": 4,
 "nbformat_minor": 2
}
