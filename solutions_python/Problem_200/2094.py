{
 "cells": [
  {
   "cell_type": "markdown",
   "metadata": {
    "toc": "true"
   },
   "source": [
    "# Table of Contents\n",
    " <p><div class=\"lev1 toc-item\"><a href=\"#General-purpose-Functions\" data-toc-modified-id=\"General-purpose-Functions-1\"><span class=\"toc-item-num\">1&nbsp;&nbsp;</span>General-purpose Functions</a></div><div class=\"lev1 toc-item\"><a href=\"#Round-1\" data-toc-modified-id=\"Round-1-2\"><span class=\"toc-item-num\">2&nbsp;&nbsp;</span>Round 1</a></div><div class=\"lev2 toc-item\"><a href=\"#Oversized-Pancake-Flipper\" data-toc-modified-id=\"Oversized-Pancake-Flipper-21\"><span class=\"toc-item-num\">2.1&nbsp;&nbsp;</span>Oversized Pancake Flipper</a></div><div class=\"lev3 toc-item\"><a href=\"#Problem-Description\" data-toc-modified-id=\"Problem-Description-211\"><span class=\"toc-item-num\">2.1.1&nbsp;&nbsp;</span>Problem Description</a></div><div class=\"lev3 toc-item\"><a href=\"#Solution\" data-toc-modified-id=\"Solution-212\"><span class=\"toc-item-num\">2.1.2&nbsp;&nbsp;</span>Solution</a></div><div class=\"lev2 toc-item\"><a href=\"#Tidy-Numbers\" data-toc-modified-id=\"Tidy-Numbers-22\"><span class=\"toc-item-num\">2.2&nbsp;&nbsp;</span>Tidy Numbers</a></div><div class=\"lev3 toc-item\"><a href=\"#Problem-Description\" data-toc-modified-id=\"Problem-Description-221\"><span class=\"toc-item-num\">2.2.1&nbsp;&nbsp;</span>Problem Description</a></div><div class=\"lev3 toc-item\"><a href=\"#Solution\" data-toc-modified-id=\"Solution-222\"><span class=\"toc-item-num\">2.2.2&nbsp;&nbsp;</span>Solution</a></div>"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 1,
   "metadata": {
    "collapsed": true,
    "init_cell": true,
    "run_control": {
     "frozen": false,
     "read_only": false
    }
   },
   "outputs": [],
   "source": [
    "from __future__ import print_function, division\n",
    "import numpy as np\n",
    "import pandas as pd"
   ]
  },
  {
   "cell_type": "markdown",
   "metadata": {},
   "source": [
    "# General-purpose Functions"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 186,
   "metadata": {
    "collapsed": true,
    "init_cell": true
   },
   "outputs": [],
   "source": [
    "def write_example_file(problem_name, example_text):\n",
    "    \"\"\"\n",
    "    Writes an example input file.\n",
    "    :param problem_name: name of the problem (name of the example file will be problem_name + '.input.ex')\n",
    "    :param example_text: (str) text to write to the example file\n",
    "    \"\"\"\n",
    "    outfile_name = problem_name + '.input.ex'\n",
    "    with open(outfile_name, 'w') as out_file:\n",
    "        out_file.write(example)\n",
    "\n",
    "\n",
    "def read_input(problem_name, extension, col_names=None, verbose=True):\n",
    "    \"\"\"\n",
    "    Reads in input from the file problem_name + '.input.' + extension.\n",
    "    It is assumed that the input file contains the number of cases on the first line and that all other lines \n",
    "    contain the same number of input data points with spaces delimiting columns.\n",
    "    :param problem_name: (str) name of the problem\n",
    "    :param extension: (str) extension of the input file, i.e. which file size to load (generally: ex, small, large)\n",
    "    :param col_names: (list[str]) names to give to the columns of the inputs dataframe; should match in number the \n",
    "                      columns in the input data file (except the file's first line). col_names may be None to use default names.\n",
    "    :param verbose: whether to print information such as the number of cases and the first few lines of the input\n",
    "    :returns: (n_cases, inputs)\n",
    "              - n_cases: (int) number of cases for the problem\n",
    "              - inputs: (pd.DataFrame) \n",
    "    \"\"\"\n",
    "    input_file_name = problem_name + \".input.\" + extension\n",
    "    with open(input_file_name) as in_file:\n",
    "        n_cases = int(in_file.readline())\n",
    "    inputs = pd.read_csv(input_file_name, sep=\" \", skiprows=1, header=None, names=col_names)\n",
    "    \n",
    "    if verbose:\n",
    "        print(\"# cases: {}\".format(n_cases))\n",
    "        print(inputs.head())\n",
    "    \n",
    "    return n_cases, inputs\n",
    "\n",
    "\n",
    "def write_output(inputs, solver, problem_name, extension, verbose=True):\n",
    "    \"\"\"\n",
    "    Applies solver row-wise to inputs and writes to disk a file with the returned solution for each case.\n",
    "    The format if the solutions file is, for each row: Case #x: y, where x is the row number (1-indexed)\n",
    "    and y is the value returned by solver for that row. The name of the output file is \n",
    "    problem_name + '.output.' + extension.\n",
    "    :param inputs: (pd.DataFrame) each row should contain all of the necessary inputs\n",
    "                   (properly named) for the solver function for that case\n",
    "                   Generally, inputs is the dataframe returned by read_input\n",
    "    :param solver: a function that can be applied row-wise to inputs to produce the output Series\n",
    "    :param problem_name:\n",
    "    :param extension:\n",
    "    :param verbose: (bool) whether to print information such as the head of the outputs dataframe\n",
    "    \"\"\"\n",
    "    \n",
    "    output = pd.DataFrame(inputs.apply(solver, axis=1), columns=['solution'])\n",
    "    output.insert(0, 'case', \"Case\")\n",
    "    output.insert(1, 'number', output.index + 1)\n",
    "    output.number = output.number.apply(lambda case_num: \"#{}:\".format(case_num))\n",
    "    \n",
    "    if verbose:\n",
    "        print(output.head())\n",
    "    \n",
    "    output_file_name = problem_name + '.output.' + extension\n",
    "    output.to_csv(output_file_name, sep=\" \", header=None, index=None, quoting=3) # 3 == csv.QUOTE_NONE (have to import csv)"
   ]
  },
  {
   "cell_type": "markdown",
   "metadata": {},
   "source": [
    "# Round 1"
   ]
  },
  {
   "cell_type": "markdown",
   "metadata": {
    "heading_collapsed": true
   },
   "source": [
    "## Oversized Pancake Flipper"
   ]
  },
  {
   "cell_type": "markdown",
   "metadata": {
    "hidden": true
   },
   "source": [
    "### Problem Description\n",
    "\n",
    "Last year, the Infinite House of Pancakes introduced a new kind of pancake. It has a happy face made of chocolate chips on one side (the \"happy side\"), and nothing on the other side (the \"blank side\").\n",
    "\n",
    "You are the head cook on duty. The pancakes are cooked in a single row over a hot surface. As part of its infinite efforts to maximize efficiency, the House has recently given you an oversized pancake flipper that flips exactly K consecutive pancakes. That is, in that range of K pancakes, it changes every happy-side pancake to a blank-side pancake, and vice versa; it does not change the left-to-right order of those pancakes.\n",
    "\n",
    "You cannot flip fewer than K pancakes at a time with the flipper, even at the ends of the row (since there are raised borders on both sides of the cooking surface). For example, you can flip the first K pancakes, but not the first K - 1 pancakes.\n",
    "\n",
    "Your apprentice cook, who is still learning the job, just used the old-fashioned single-pancake flipper to flip some individual pancakes and then ran to the restroom with it, right before the time when customers come to visit the kitchen. You only have the oversized pancake flipper left, and you need to use it quickly to leave all the cooking pancakes happy side up, so that the customers leave feeling happy with their visit.\n",
    "\n",
    "Given the current state of the pancakes, calculate the minimum number of uses of the oversized pancake flipper needed to leave all pancakes happy side up, or state that there is no way to do it.\n",
    "\n",
    "Input\n",
    "\n",
    "The first line of the input gives the number of test cases, T. T test cases follow. Each consists of one line with a string S and an integer K. S represents the row of pancakes: each of its characters is either + (which represents a pancake that is initially happy side up) or - (which represents a pancake that is initially blank side up).\n",
    "\n",
    "Output\n",
    "\n",
    "For each test case, output one line containing Case #x: y, where x is the test case number (starting from 1) and y is either IMPOSSIBLE if there is no way to get all the pancakes happy side up, or an integer representing the the minimum number of times you will need to use the oversized pancake flipper to do it.\n",
    "\n",
    "Limits\n",
    "\n",
    "1 ≤ T ≤ 100.\n",
    "Every character in S is either + or -.\n",
    "2 ≤ K ≤ length of S.\n",
    "Small dataset\n",
    "\n",
    "2 ≤ length of S ≤ 10.\n",
    "Large dataset\n",
    "\n",
    "2 ≤ length of S ≤ 1000.\n",
    "Sample\n",
    "\n",
    "\n",
    "Input \n",
    " \t\n",
    "Output \n",
    " \n",
    "3\n",
    "---+-++- 3\n",
    "+++++ 4\n",
    "-+-+- 4\n",
    "\n",
    "Case #1: 3\n",
    "Case #2: 0\n",
    "Case #3: IMPOSSIBLE\n",
    "In Case #1, you can get all the pancakes happy side up by first flipping the leftmost 3 pancakes, getting to ++++-++-, then the rightmost 3, getting to ++++---+, and finally the 3 pancakes that remain blank side up. There are other ways to do it with 3 flips or more, but none with fewer than 3 flips.\n",
    "\n",
    "In Case #2, all of the pancakes are already happy side up, so there is no need to flip any of them.\n",
    "\n",
    "In Case #3, there is no way to make the second and third pancakes from the left have the same side up, because any flip flips them both. Therefore, there is no way to make all of the pancakes happy side up."
   ]
  },
  {
   "cell_type": "markdown",
   "metadata": {
    "hidden": true
   },
   "source": [
    "### Solution\n",
    "Convert to a bit string and then just twiddle the bits in a given range? Should be a very fast operation then"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 121,
   "metadata": {
    "collapsed": false,
    "hidden": true
   },
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "3\r\n",
      "---+-++- 3\r\n",
      "+++++ 4\r\n",
      "-+-+- 4"
     ]
    }
   ],
   "source": [
    "## write out a tiny example file\n",
    "problem_name = 'pancake_flipper'\n",
    "example = \"\"\"3\n",
    "---+-++- 3\n",
    "+++++ 4\n",
    "-+-+- 4\"\"\"\n",
    "write_example_file(problem_name, example)\n",
    "! cat pancake_flipper.input.ex"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 125,
   "metadata": {
    "collapsed": false,
    "hidden": true
   },
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "# cases: 100\n",
      "                                         pancake_seq  flipper_size\n",
      "0                                           ---+-++-             3\n",
      "1                                              +++++             4\n",
      "2                                              -+-+-             4\n",
      "3  ++-++-++-++-++-++-++-++-++-++-++-++-++-++-++-+...             3\n",
      "4  -++++----++-++--+++----++-+++----+--++--++-+-+...            25\n",
      "\n",
      "[5 rows x 2 columns]\n"
     ]
    }
   ],
   "source": [
    "problem_name = 'pancake_flipper'\n",
    "# extension = 'ex'\n",
    "# extension = 'small'\n",
    "extension = 'large'\n",
    "col_names = ['pancake_seq', 'flipper_size']\n",
    "\n",
    "n_cases, inputs = read_input(problem_name, extension, col_names)"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 110,
   "metadata": {
    "collapsed": true,
    "hidden": true
   },
   "outputs": [],
   "source": [
    "happy_side = '+'\n",
    "blank_side = '-'\n",
    "flipper = {happy_side: blank_side, blank_side: happy_side}\n",
    "flip = flipper.get\n",
    "\n",
    "def count_flips(input_row):\n",
    "    \"\"\"\n",
    "    Counts the number of flips necessary to get all of the pancakes happy side up.\n",
    "    :param input_row: a row from the input dataframe; must contain columns:\n",
    "                       - 'flipper_size' (int): size of the pancake flipper\n",
    "                       - 'pancake_seq' (str): happy_side or blank_side for each pancake\n",
    "    :returns: minimum number of flips or 'IMPOSSIBLE' if the problem is not solvable\n",
    "    \"\"\"\n",
    "    flipper_size = input_row.flipper_size\n",
    "    pancake_seq = list(input_row.pancake_seq)\n",
    "    \n",
    "    n_flips = 0\n",
    "    for pancake_idx in xrange(len(pancake_seq) - flipper_size + 1):\n",
    "        pancake = pancake_seq[pancake_idx]\n",
    "        if pancake == happy_side:\n",
    "            continue\n",
    "        else:\n",
    "            # change p + next k-1\n",
    "            for flip_idx in xrange(pancake_idx, pancake_idx + flipper_size):\n",
    "                pancake_seq[flip_idx] = flip(pancake_seq[flip_idx])\n",
    "            n_flips += 1\n",
    "\n",
    "    if all(map(lambda pancake: pancake == happy_side, pancake_seq)):\n",
    "        return n_flips\n",
    "    else:\n",
    "        return \"IMPOSSIBLE\""
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 130,
   "metadata": {
    "collapsed": false,
    "hidden": true
   },
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "   case number    solution\n",
      "0  Case    #1:           3\n",
      "1  Case    #2:           0\n",
      "2  Case    #3:  IMPOSSIBLE\n",
      "3  Case    #4:  IMPOSSIBLE\n",
      "4  Case    #5:  IMPOSSIBLE\n",
      "\n",
      "[5 rows x 3 columns]\n"
     ]
    }
   ],
   "source": [
    "write_output(inputs, count_flips, problem_name, extension)"
   ]
  },
  {
   "cell_type": "markdown",
   "metadata": {},
   "source": [
    "## Tidy Numbers"
   ]
  },
  {
   "cell_type": "markdown",
   "metadata": {},
   "source": [
    "### Problem Description\n",
    "Tatiana likes to keep things tidy. Her toys are sorted from smallest to largest, her pencils are sorted from shortest to longest and her computers from oldest to newest. One day, when practicing her counting skills, she noticed that some integers, when written in base 10 with no leading zeroes, have their digits sorted in non-decreasing order. Some examples of this are 8, 123, 555, and 224488. She decided to call these numbers tidy. Numbers that do not have this property, like 20, 321, 495 and 999990, are not tidy.\n",
    "\n",
    "She just finished counting all positive integers in ascending order from 1 to N. What was the last tidy number she counted?\n",
    "\n",
    "Input\n",
    "\n",
    "The first line of the input gives the number of test cases, T. T lines follow. Each line describes a test case with a single integer N, the last number counted by Tatiana.\n",
    "\n",
    "Output\n",
    "\n",
    "For each test case, output one line containing Case #x: y, where x is the test case number (starting from 1) and y is the last tidy number counted by Tatiana.\n",
    "\n",
    "Limits\n",
    "\n",
    "1 ≤ T ≤ 100.\n",
    "Small dataset\n",
    "\n",
    "1 ≤ N ≤ 1000.\n",
    "Large dataset\n",
    "\n",
    "1 ≤ N ≤ 1018.\n",
    "Sample\n",
    "\n",
    "\n",
    "Input \n",
    " \t\n",
    "Output \n",
    " \n",
    "4\n",
    "132\n",
    "1000\n",
    "7\n",
    "111111111111111110\n",
    "\n",
    "Case #1: 129\n",
    "Case #2: 999\n",
    "Case #3: 7\n",
    "Case #4: 99999999999999999\n"
   ]
  },
  {
   "cell_type": "markdown",
   "metadata": {},
   "source": [
    "### Solution"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 131,
   "metadata": {
    "collapsed": false
   },
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "4\r\n",
      "132\r\n",
      "1000\r\n",
      "7\r\n",
      "111111111111111110"
     ]
    }
   ],
   "source": [
    "problem_name = \"tidy_numbers\"\n",
    "example = \"\"\"4\n",
    "132\n",
    "1000\n",
    "7\n",
    "111111111111111110\"\"\"\n",
    "\n",
    "write_example_file(problem_name, example)\n",
    "! cat tidy_numbers.input.ex"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 179,
   "metadata": {
    "collapsed": false
   },
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "# cases: 100\n",
      "      n\n",
      "0   132\n",
      "1  1000\n",
      "2     7\n",
      "3   491\n",
      "4   592\n",
      "\n",
      "[5 rows x 1 columns]\n"
     ]
    }
   ],
   "source": [
    "problem_name = 'tidy_numbers'\n",
    "# extension = 'ex'\n",
    "extension = 'small'\n",
    "# extension = 'large'\n",
    "\n",
    "n_cases, inputs = read_input(problem_name, extension, col_names=['n'])"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 180,
   "metadata": {
    "collapsed": true
   },
   "outputs": [],
   "source": [
    "def is_tidy(number):\n",
    "    \"\"\"\n",
    "    A number is tidy if its digits are non-decreasing (read left to right)\n",
    "    :param number: the number to check for tidiness\n",
    "    :returns: True if number is tidy else False\n",
    "    \"\"\"\n",
    "    digits_list = map(int, list(str(number))) # convert to list of digits\n",
    "    for i in xrange(1, len(digits_list)):\n",
    "        if digits_list[i] < digits_list[i - 1]:\n",
    "            return False\n",
    "    return True\n",
    "\n",
    "\n",
    "def find_last_tidy_naive(input_row):\n",
    "    \"\"\"\n",
    "    WARNING: this is a very slow way to do this\n",
    "    Returns the largest tidy number less than or equal to input_row.n\n",
    "    \"\"\"\n",
    "    for i in xrange(input_row.n, 0, -1):\n",
    "        if is_tidy(i):\n",
    "            return i"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 181,
   "metadata": {
    "collapsed": true
   },
   "outputs": [],
   "source": [
    "def find_last_tidy(input_row):\n",
    "    \"\"\"\n",
    "    Returns the largest tidy number less than or equal to input_row.n\n",
    "    \"\"\"\n",
    "    digits = np.array(list(str(input_row.n))).astype(int) # convert to array of integers\n",
    "    for digit_idx in xrange(len(digits) - 1, 0, -1):\n",
    "        if digits[digit_idx] < digits[digit_idx - 1]: # decrease! not tidy!!\n",
    "            digits[digit_idx - 1] -= 1\n",
    "            digits[digit_idx:] = 9\n",
    "    digits = digits[np.where(digits > 0)] # drop leading 0 if extant\n",
    "    last_tidy_num = int(''.join(digits.astype(str)))\n",
    "    return last_tidy_num"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 187,
   "metadata": {
    "collapsed": false
   },
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "   case number  solution\n",
      "0  Case    #1:       129\n",
      "1  Case    #2:       999\n",
      "2  Case    #3:         7\n",
      "3  Case    #4:       489\n",
      "4  Case    #5:       589\n",
      "\n",
      "[5 rows x 3 columns]\n"
     ]
    }
   ],
   "source": [
    "write_output(inputs, find_last_tidy, problem_name, extension)"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 184,
   "metadata": {
    "collapsed": false
   },
   "outputs": [
    {
     "data": {
      "text/plain": [
       "('tidy_numbers', 'small')"
      ]
     },
     "execution_count": 184,
     "metadata": {},
     "output_type": "execute_result"
    }
   ],
   "source": [
    "problem_name, extension"
   ]
  },
  {
   "cell_type": "markdown",
   "metadata": {},
   "source": [
    "##"
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
   "version": "2.7.6"
  },
  "latex_envs": {
   "bibliofile": "biblio.bib",
   "cite_by": "apalike",
   "current_citInitial": 1,
   "eqLabelWithNumbers": true,
   "eqNumInitial": 0
  },
  "toc": {
   "colors": {
    "hover_highlight": "#DAA520",
    "running_highlight": "#FF0000",
    "selected_highlight": "#FFD700"
   },
   "moveMenuLeft": true,
   "nav_menu": {
    "height": "156px",
    "width": "252px"
   },
   "navigate_menu": true,
   "number_sections": true,
   "sideBar": true,
   "threshold": 4,
   "toc_cell": true,
   "toc_section_display": "block",
   "toc_window_display": false
  }
 },
 "nbformat": 4,
 "nbformat_minor": 2
}
