{
 "cells": [
  {
   "cell_type": "markdown",
   "metadata": {
    "run_control": {
     "frozen": false,
     "read_only": false
    },
    "toc": "true"
   },
   "source": [
    "# Table of Contents\n",
    " <p><div class=\"lev1 toc-item\"><a href=\"#General-purpose-Functions\" data-toc-modified-id=\"General-purpose-Functions-1\"><span class=\"toc-item-num\">1&nbsp;&nbsp;</span>General-purpose Functions</a></div><div class=\"lev1 toc-item\"><a href=\"#Round-1\" data-toc-modified-id=\"Round-1-2\"><span class=\"toc-item-num\">2&nbsp;&nbsp;</span>Round 1</a></div><div class=\"lev2 toc-item\"><a href=\"#Oversized-Pancake-Flipper\" data-toc-modified-id=\"Oversized-Pancake-Flipper-21\"><span class=\"toc-item-num\">2.1&nbsp;&nbsp;</span>Oversized Pancake Flipper</a></div><div class=\"lev3 toc-item\"><a href=\"#Problem-Description\" data-toc-modified-id=\"Problem-Description-211\"><span class=\"toc-item-num\">2.1.1&nbsp;&nbsp;</span>Problem Description</a></div><div class=\"lev3 toc-item\"><a href=\"#Solution\" data-toc-modified-id=\"Solution-212\"><span class=\"toc-item-num\">2.1.2&nbsp;&nbsp;</span>Solution</a></div><div class=\"lev2 toc-item\"><a href=\"#Tidy-Numbers\" data-toc-modified-id=\"Tidy-Numbers-22\"><span class=\"toc-item-num\">2.2&nbsp;&nbsp;</span>Tidy Numbers</a></div><div class=\"lev3 toc-item\"><a href=\"#Problem-Description\" data-toc-modified-id=\"Problem-Description-221\"><span class=\"toc-item-num\">2.2.1&nbsp;&nbsp;</span>Problem Description</a></div><div class=\"lev3 toc-item\"><a href=\"#Solution\" data-toc-modified-id=\"Solution-222\"><span class=\"toc-item-num\">2.2.2&nbsp;&nbsp;</span>Solution</a></div><div class=\"lev2 toc-item\"><a href=\"#Bathroom-Stalls\" data-toc-modified-id=\"Bathroom-Stalls-23\"><span class=\"toc-item-num\">2.3&nbsp;&nbsp;</span>Bathroom Stalls</a></div><div class=\"lev3 toc-item\"><a href=\"#Problem-Description\" data-toc-modified-id=\"Problem-Description-231\"><span class=\"toc-item-num\">2.3.1&nbsp;&nbsp;</span>Problem Description</a></div><div class=\"lev3 toc-item\"><a href=\"#Solution\" data-toc-modified-id=\"Solution-232\"><span class=\"toc-item-num\">2.3.2&nbsp;&nbsp;</span>Solution</a></div><div class=\"lev2 toc-item\"><a href=\"#Fashion-Show\" data-toc-modified-id=\"Fashion-Show-24\"><span class=\"toc-item-num\">2.4&nbsp;&nbsp;</span>Fashion Show</a></div><div class=\"lev3 toc-item\"><a href=\"#Problem-Statement\" data-toc-modified-id=\"Problem-Statement-241\"><span class=\"toc-item-num\">2.4.1&nbsp;&nbsp;</span>Problem Statement</a></div><div class=\"lev1 toc-item\"><a href=\"#Round-2\" data-toc-modified-id=\"Round-2-3\"><span class=\"toc-item-num\">3&nbsp;&nbsp;</span>Round 2</a></div><div class=\"lev2 toc-item\"><a href=\"#Alphabet-Cake\" data-toc-modified-id=\"Alphabet-Cake-31\"><span class=\"toc-item-num\">3.1&nbsp;&nbsp;</span>Alphabet Cake</a></div><div class=\"lev2 toc-item\"><a href=\"#Ratatouille\" data-toc-modified-id=\"Ratatouille-32\"><span class=\"toc-item-num\">3.2&nbsp;&nbsp;</span>Ratatouille</a></div>"
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
   "metadata": {
    "run_control": {
     "frozen": false,
     "read_only": false
    }
   },
   "source": [
    "# General-purpose Functions"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 14,
   "metadata": {
    "code_folding": [],
    "collapsed": true,
    "init_cell": true,
    "run_control": {
     "frozen": false,
     "read_only": false
    }
   },
   "outputs": [],
   "source": [
    "def write_example_file(problem_name, example_text):\n",
    "    \"\"\"\n",
    "    Writes an example input file.\n",
    "    :param problem_name: name of the problem (name of the example file will be problem_name + '.input.ex')\n",
    "    :param example_text: (str) text to write to the example file\n",
    "    \"\"\"\n",
    "    outfile_name = problem_name + '_ex.in'\n",
    "    with open(outfile_name, 'w') as out_file:\n",
    "        out_file.write(example_text)\n",
    "\n",
    "\n",
    "def read_input(problem_name, size, raw=False, col_names=None, verbose=True):\n",
    "    \"\"\"\n",
    "    Reads in input from the file problem_name + '.input.' + extension.\n",
    "    It is assumed that the input file contains the number of cases on the first line and that all other lines \n",
    "    contain the same number of input data points with spaces delimiting columns.\n",
    "    :param problem_name: (str) name of the problem\n",
    "    :param size: (str) which file size to load (generally: ex, small, large)\n",
    "    :param raw: if True, just return the list of strings from the input file: one per row (except n_cases ommitted)\n",
    "    :param col_names: (list[str]) names to give to the columns of the inputs dataframe; should match in number the \n",
    "                      columns in the input data file (except the file's first line). col_names may be None to use default names.\n",
    "    :param verbose: whether to print information such as the number of cases and the first few lines of the input\n",
    "    :returns: (n_cases, inputs)\n",
    "              - n_cases: (int) number of cases for the problem\n",
    "              - inputs: (pd.DataFrame) \n",
    "    \"\"\"\n",
    "    input_file_name = problem_name + \"_\" + size + \".in\"\n",
    "    with open(input_file_name) as in_file:\n",
    "        n_cases = int(in_file.readline())\n",
    "        if raw:\n",
    "            return n_cases, in_file.readlines()\n",
    "    \n",
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
    "    :param size:\n",
    "    :param verbose: (bool) whether to print information such as the head of the outputs dataframe\n",
    "    \"\"\"\n",
    "    \n",
    "    output = pd.DataFrame(inputs.apply(solver, axis=1))\n",
    "    output.insert(0, 'case', \"Case\")\n",
    "    output.insert(1, 'number', output.index + 1)\n",
    "    output.number = output.number.apply(lambda case_num: \"#{}:\".format(case_num))\n",
    "    \n",
    "    if verbose:\n",
    "        print(output.head())\n",
    "        print(output.dtypes)\n",
    "    \n",
    "    output_file_name = problem_name + \"_\" + size + \".out\"\n",
    "    output.to_csv(output_file_name, sep=\" \", header=None, index=None, quoting=3) # 3 == csv.QUOTE_NONE (have to import csv)"
   ]
  },
  {
   "cell_type": "markdown",
   "metadata": {
    "heading_collapsed": true,
    "run_control": {
     "frozen": false,
     "read_only": false
    }
   },
   "source": [
    "# Round 1"
   ]
  },
  {
   "cell_type": "markdown",
   "metadata": {
    "heading_collapsed": true,
    "hidden": true,
    "run_control": {
     "frozen": false,
     "read_only": false
    }
   },
   "source": [
    "## Oversized Pancake Flipper"
   ]
  },
  {
   "cell_type": "markdown",
   "metadata": {
    "hidden": true,
    "run_control": {
     "frozen": false,
     "read_only": false
    }
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
    "hidden": true,
    "run_control": {
     "frozen": false,
     "read_only": false
    }
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
    "hidden": true,
    "run_control": {
     "frozen": false,
     "read_only": false
    }
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
    "hidden": true,
    "run_control": {
     "frozen": false,
     "read_only": false
    }
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
    "hidden": true,
    "run_control": {
     "frozen": false,
     "read_only": false
    }
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
    "hidden": true,
    "run_control": {
     "frozen": false,
     "read_only": false
    }
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
   "metadata": {
    "hidden": true,
    "run_control": {
     "frozen": false,
     "read_only": false
    }
   },
   "source": [
    "## Tidy Numbers"
   ]
  },
  {
   "cell_type": "markdown",
   "metadata": {
    "hidden": true,
    "run_control": {
     "frozen": false,
     "read_only": false
    }
   },
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
   "metadata": {
    "hidden": true,
    "run_control": {
     "frozen": false,
     "read_only": false
    }
   },
   "source": [
    "### Solution"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 131,
   "metadata": {
    "hidden": true,
    "run_control": {
     "frozen": false,
     "read_only": false
    }
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
   "execution_count": 188,
   "metadata": {
    "hidden": true,
    "run_control": {
     "frozen": false,
     "read_only": false
    }
   },
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "# cases: 100\n",
      "                    n\n",
      "0                 132\n",
      "1                1000\n",
      "2                   7\n",
      "3  111111111111111110\n",
      "4             7135689\n",
      "\n",
      "[5 rows x 1 columns]\n"
     ]
    }
   ],
   "source": [
    "problem_name = 'tidy_numbers'\n",
    "# extension = 'ex'\n",
    "# extension = 'small'\n",
    "extension = 'large'\n",
    "\n",
    "n_cases, inputs = read_input(problem_name, extension, col_names=['n'])"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 189,
   "metadata": {
    "collapsed": true,
    "hidden": true,
    "run_control": {
     "frozen": false,
     "read_only": false
    }
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
   "execution_count": 190,
   "metadata": {
    "collapsed": true,
    "hidden": true,
    "run_control": {
     "frozen": false,
     "read_only": false
    }
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
   "execution_count": 191,
   "metadata": {
    "hidden": true,
    "run_control": {
     "frozen": false,
     "read_only": false
    }
   },
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "   case number           solution\n",
      "0  Case    #1:                129\n",
      "1  Case    #2:                999\n",
      "2  Case    #3:                  7\n",
      "3  Case    #4:  99999999999999999\n",
      "4  Case    #5:            6999999\n",
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
   "cell_type": "markdown",
   "metadata": {
    "hidden": true,
    "run_control": {
     "frozen": false,
     "read_only": false
    }
   },
   "source": [
    "## Bathroom Stalls"
   ]
  },
  {
   "cell_type": "markdown",
   "metadata": {
    "hidden": true,
    "run_control": {
     "frozen": false,
     "read_only": false
    }
   },
   "source": [
    "### Problem Description\n",
    "A certain bathroom has N + 2 stalls in a single row; the stalls on the left and right ends are permanently occupied by the bathroom guards. The other N stalls are for users.\n",
    "\n",
    "Whenever someone enters the bathroom, they try to choose a stall that is as far from other people as possible. To avoid confusion, they follow deterministic rules: For each empty stall S, they compute two values LS and RS, each of which is the number of empty stalls between S and the closest occupied stall to the left or right, respectively. Then they consider the set of stalls with the farthest closest neighbor, that is, those S for which min(LS, RS) is maximal. If there is only one such stall, they choose it; otherwise, they choose the one among those where max(LS, RS) is maximal. If there are still multiple tied stalls, they choose the leftmost stall among those.\n",
    "\n",
    "K people are about to enter the bathroom; each one will choose their stall before the next arrives. Nobody will ever leave.\n",
    "\n",
    "When the last person chooses their stall S, what will the values of max(LS, RS) and min(LS, RS) be?\n",
    "\n",
    "Solving this problem\n",
    "\n",
    "This problem has 2 Small datasets and 1 Large dataset. You must solve the first Small dataset before you can attempt the second Small dataset. You will be able to retry either of the Small datasets (with a time penalty). You will be able to make a single attempt at the Large, as usual, only after solving both Small datasets.\n",
    "\n",
    "Input\n",
    "\n",
    "The first line of the input gives the number of test cases, T. T lines follow. Each line describes a test case with two integers N and K, as described above.\n",
    "\n",
    "Output\n",
    "\n",
    "For each test case, output one line containing Case #x: y z, where x is the test case number (starting from 1), y is max(LS, RS), and z is min(LS, RS) as calculated by the last person to enter the bathroom for their chosen stall S.\n",
    "\n",
    "Limits\n",
    "\n",
    "1 ≤ T ≤ 100.\n",
    "1 ≤ K ≤ N.\n",
    "Small dataset 1\n",
    "\n",
    "1 ≤ N ≤ 1000.\n",
    "Small dataset 2\n",
    "\n",
    "1 ≤ N ≤ 106.\n",
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
    "5\n",
    "4 2\n",
    "5 2\n",
    "6 2\n",
    "1000 1000\n",
    "1000 1\n",
    "\n",
    "Case #1: 1 0\n",
    "Case #2: 1 0\n",
    "Case #3: 1 1\n",
    "Case #4: 0 0\n",
    "Case #5: 500 499\n",
    "\n",
    "In Case #1, the first person occupies the leftmost of the middle two stalls, leaving the following configuration (O stands for an occupied stall and . for an empty one): O.O..O. Then, the second and last person occupies the stall immediately to the right, leaving 1 empty stall on one side and none on the other.\n",
    "\n",
    "In Case #2, the first person occupies the middle stall, getting to O..O..O. Then, the second and last person occupies the leftmost stall.\n",
    "\n",
    "In Case #3, the first person occupies the leftmost of the two middle stalls, leaving O..O...O. The second person then occupies the middle of the three consecutive empty stalls.\n",
    "\n",
    "In Case #4, every stall is occupied at the end, no matter what the stall choices are.\n",
    "\n",
    "In Case #5, the first and only person chooses the leftmost middle stall."
   ]
  },
  {
   "cell_type": "markdown",
   "metadata": {
    "hidden": true,
    "run_control": {
     "frozen": false,
     "read_only": false
    }
   },
   "source": [
    "### Solution"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 299,
   "metadata": {
    "hidden": true,
    "run_control": {
     "frozen": false,
     "read_only": false
    }
   },
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "5\r\n",
      "4 2\r\n",
      "5 2\r\n",
      "6 2\r\n",
      "1000 1000\r\n",
      "1000 1"
     ]
    }
   ],
   "source": [
    "problem_name = 'bathroom_stalls'\n",
    "example = \"\"\"5\n",
    "4 2\n",
    "5 2\n",
    "6 2\n",
    "1000 1000\n",
    "1000 1\"\"\"\n",
    "write_example_file(problem_name, example)\n",
    "! cat bathroom_stalls_ex.in"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 303,
   "metadata": {
    "hidden": true,
    "run_control": {
     "frozen": false,
     "read_only": false
    }
   },
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "# cases: 100\n",
      "   n_stalls  n_people\n",
      "0         4         2\n",
      "1         5         2\n",
      "2         6         2\n",
      "3      1000      1000\n",
      "4      1000         1\n",
      "\n",
      "[5 rows x 2 columns]\n"
     ]
    }
   ],
   "source": [
    "# size = 'ex'\n",
    "# size = 'small'\n",
    "size = 'medium'\n",
    "# size = 'large'\n",
    "n_cases, inputs = read_input(problem_name, size, col_names=['n_stalls', 'n_people'])\n",
    "inputs.n_stalls += 2 # n_stalls = n + 2 (including the bodyguard stalls on the ends)"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 304,
   "metadata": {
    "code_folding": [],
    "collapsed": true,
    "hidden": true,
    "run_control": {
     "frozen": false,
     "read_only": false
    }
   },
   "outputs": [],
   "source": [
    "def compute_final_costs(input_row):\n",
    "    \"\"\"\n",
    "    \"\"\"\n",
    "    n_stalls = input_row.n_stalls\n",
    "    n_people = input_row.n_people\n",
    "    \n",
    "    stalls = [0] * n_stalls # 0 means available, 1 means taken\n",
    "    stalls[0] = 1 # guards are already there\n",
    "    stalls[-1] = 1\n",
    "    \n",
    "    # use -infinity for stalls with a person in them so that they'll never be picked\n",
    "    left_costs = np.array([-float('inf')] + range(n_stalls - 2) + [-float('inf')])\n",
    "    right_costs = np.array([-float('inf')] + range(n_stalls - 2 - 1, -1, -1) + [-float('inf')])\n",
    "    \n",
    "    \n",
    "    for person_idx in xrange(n_people): # find this person's stall and put them in\n",
    "        min_costs = np.where(left_costs < right_costs, left_costs, right_costs) # min of left or right\n",
    "        best_stalls = np.where(min_costs == min_costs.max())[0]\n",
    "\n",
    "        if len(best_stalls) == 1:\n",
    "            best_stall = best_stalls[0]\n",
    "        else:\n",
    "            max_costs = np.where(left_costs < right_costs, right_costs, left_costs) # max of left or right\n",
    "            best_stall = best_stalls[np.argmax(max_costs[best_stalls])]\n",
    "        \n",
    "        assert stalls[best_stall] == 0\n",
    "        stalls[best_stall] = 1\n",
    "        \n",
    "        # for the last person, we don't have to put them in, just calculate the costs they saw and return those\n",
    "        if person_idx == n_people - 1:\n",
    "            left_cost = int(left_costs[best_stall])\n",
    "            right_cost = int(right_costs[best_stall])\n",
    "            return sorted([left_cost, right_cost], reverse=True)\n",
    "        \n",
    "        # update left and right costs:\n",
    "        # to update left costs, start at the newly occupied stall and go to the right\n",
    "        # (so that the direction back is left) and change each one to have a new cost\n",
    "        # which is the minimum of its distance from the newly occupied stall and its\n",
    "        # only cost. Once you find an occupied stall, stop, because none of the stalls\n",
    "        # past that need updating; they're closer to that stall than the new one\n",
    "        # do essentially the same for the right costs, in the opposite direction\n",
    "\n",
    "        left_costs[best_stall] = -float('inf')\n",
    "        right_costs[best_stall] = -float('inf')\n",
    "\n",
    "        dist_from_this_stall = 0\n",
    "        for stall_idx in xrange(best_stall + 1, n_stalls):\n",
    "            if stalls[stall_idx] == 1:\n",
    "                break\n",
    "            left_costs[stall_idx] = dist_from_this_stall\n",
    "            dist_from_this_stall += 1\n",
    "\n",
    "        dist_from_this_stall = 0\n",
    "        for stall_idx in xrange(best_stall - 1, -1, -1):\n",
    "            if stalls[stall_idx] == 1:\n",
    "                break\n",
    "            right_costs[stall_idx] = dist_from_this_stall\n",
    "            dist_from_this_stall += 1"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 305,
   "metadata": {
    "hidden": true,
    "run_control": {
     "frozen": false,
     "read_only": false
    }
   },
   "outputs": [
    {
     "ename": "KeyboardInterrupt",
     "evalue": "",
     "output_type": "error",
     "traceback": [
      "\u001b[0;31m---------------------------------------------------------------------------\u001b[0m",
      "\u001b[0;31mKeyboardInterrupt\u001b[0m                         Traceback (most recent call last)",
      "\u001b[0;32m<ipython-input-305-4dfe8dda017a>\u001b[0m in \u001b[0;36m<module>\u001b[0;34m()\u001b[0m\n\u001b[0;32m----> 1\u001b[0;31m \u001b[0mwrite_output\u001b[0m\u001b[0;34m(\u001b[0m\u001b[0minputs\u001b[0m\u001b[0;34m,\u001b[0m \u001b[0mcompute_final_costs\u001b[0m\u001b[0;34m,\u001b[0m \u001b[0mproblem_name\u001b[0m\u001b[0;34m,\u001b[0m \u001b[0msize\u001b[0m\u001b[0;34m)\u001b[0m\u001b[0;34m\u001b[0m\u001b[0m\n\u001b[0m",
      "\u001b[0;32m<ipython-input-295-12d194a1d6ad>\u001b[0m in \u001b[0;36mwrite_output\u001b[0;34m(inputs, solver, problem_name, extension, verbose)\u001b[0m\n\u001b[1;32m     51\u001b[0m     \"\"\"\n\u001b[1;32m     52\u001b[0m \u001b[0;34m\u001b[0m\u001b[0m\n\u001b[0;32m---> 53\u001b[0;31m     \u001b[0moutput\u001b[0m \u001b[0;34m=\u001b[0m \u001b[0mpd\u001b[0m\u001b[0;34m.\u001b[0m\u001b[0mDataFrame\u001b[0m\u001b[0;34m(\u001b[0m\u001b[0minputs\u001b[0m\u001b[0;34m.\u001b[0m\u001b[0mapply\u001b[0m\u001b[0;34m(\u001b[0m\u001b[0msolver\u001b[0m\u001b[0;34m,\u001b[0m \u001b[0maxis\u001b[0m\u001b[0;34m=\u001b[0m\u001b[0;36m1\u001b[0m\u001b[0;34m)\u001b[0m\u001b[0;34m)\u001b[0m\u001b[0;34m\u001b[0m\u001b[0m\n\u001b[0m\u001b[1;32m     54\u001b[0m     \u001b[0moutput\u001b[0m\u001b[0;34m.\u001b[0m\u001b[0minsert\u001b[0m\u001b[0;34m(\u001b[0m\u001b[0;36m0\u001b[0m\u001b[0;34m,\u001b[0m \u001b[0;34m'case'\u001b[0m\u001b[0;34m,\u001b[0m \u001b[0;34m\"Case\"\u001b[0m\u001b[0;34m)\u001b[0m\u001b[0;34m\u001b[0m\u001b[0m\n\u001b[1;32m     55\u001b[0m     \u001b[0moutput\u001b[0m\u001b[0;34m.\u001b[0m\u001b[0minsert\u001b[0m\u001b[0;34m(\u001b[0m\u001b[0;36m1\u001b[0m\u001b[0;34m,\u001b[0m \u001b[0;34m'number'\u001b[0m\u001b[0;34m,\u001b[0m \u001b[0moutput\u001b[0m\u001b[0;34m.\u001b[0m\u001b[0mindex\u001b[0m \u001b[0;34m+\u001b[0m \u001b[0;36m1\u001b[0m\u001b[0;34m)\u001b[0m\u001b[0;34m\u001b[0m\u001b[0m\n",
      "\u001b[0;32m/usr/lib/python2.7/dist-packages/pandas/core/frame.pyc\u001b[0m in \u001b[0;36mapply\u001b[0;34m(self, func, axis, broadcast, raw, reduce, args, **kwds)\u001b[0m\n\u001b[1;32m   3310\u001b[0m                     \u001b[0;32mif\u001b[0m \u001b[0mreduce\u001b[0m \u001b[0;32mis\u001b[0m \u001b[0mNone\u001b[0m\u001b[0;34m:\u001b[0m\u001b[0;34m\u001b[0m\u001b[0m\n\u001b[1;32m   3311\u001b[0m                         \u001b[0mreduce\u001b[0m \u001b[0;34m=\u001b[0m \u001b[0mTrue\u001b[0m\u001b[0;34m\u001b[0m\u001b[0m\n\u001b[0;32m-> 3312\u001b[0;31m                     \u001b[0;32mreturn\u001b[0m \u001b[0mself\u001b[0m\u001b[0;34m.\u001b[0m\u001b[0m_apply_standard\u001b[0m\u001b[0;34m(\u001b[0m\u001b[0mf\u001b[0m\u001b[0;34m,\u001b[0m \u001b[0maxis\u001b[0m\u001b[0;34m,\u001b[0m \u001b[0mreduce\u001b[0m\u001b[0;34m=\u001b[0m\u001b[0mreduce\u001b[0m\u001b[0;34m)\u001b[0m\u001b[0;34m\u001b[0m\u001b[0m\n\u001b[0m\u001b[1;32m   3313\u001b[0m             \u001b[0;32melse\u001b[0m\u001b[0;34m:\u001b[0m\u001b[0;34m\u001b[0m\u001b[0m\n\u001b[1;32m   3314\u001b[0m                 \u001b[0;32mreturn\u001b[0m \u001b[0mself\u001b[0m\u001b[0;34m.\u001b[0m\u001b[0m_apply_broadcast\u001b[0m\u001b[0;34m(\u001b[0m\u001b[0mf\u001b[0m\u001b[0;34m,\u001b[0m \u001b[0maxis\u001b[0m\u001b[0;34m)\u001b[0m\u001b[0;34m\u001b[0m\u001b[0m\n",
      "\u001b[0;32m/usr/lib/python2.7/dist-packages/pandas/core/frame.pyc\u001b[0m in \u001b[0;36m_apply_standard\u001b[0;34m(self, func, axis, ignore_failures, reduce)\u001b[0m\n\u001b[1;32m   3398\u001b[0m             \u001b[0;32mtry\u001b[0m\u001b[0;34m:\u001b[0m\u001b[0;34m\u001b[0m\u001b[0m\n\u001b[1;32m   3399\u001b[0m                 \u001b[0;32mfor\u001b[0m \u001b[0mi\u001b[0m\u001b[0;34m,\u001b[0m \u001b[0mv\u001b[0m \u001b[0;32min\u001b[0m \u001b[0menumerate\u001b[0m\u001b[0;34m(\u001b[0m\u001b[0mseries_gen\u001b[0m\u001b[0;34m)\u001b[0m\u001b[0;34m:\u001b[0m\u001b[0;34m\u001b[0m\u001b[0m\n\u001b[0;32m-> 3400\u001b[0;31m                     \u001b[0mresults\u001b[0m\u001b[0;34m[\u001b[0m\u001b[0mi\u001b[0m\u001b[0;34m]\u001b[0m \u001b[0;34m=\u001b[0m \u001b[0mfunc\u001b[0m\u001b[0;34m(\u001b[0m\u001b[0mv\u001b[0m\u001b[0;34m)\u001b[0m\u001b[0;34m\u001b[0m\u001b[0m\n\u001b[0m\u001b[1;32m   3401\u001b[0m                     \u001b[0mkeys\u001b[0m\u001b[0;34m.\u001b[0m\u001b[0mappend\u001b[0m\u001b[0;34m(\u001b[0m\u001b[0mv\u001b[0m\u001b[0;34m.\u001b[0m\u001b[0mname\u001b[0m\u001b[0;34m)\u001b[0m\u001b[0;34m\u001b[0m\u001b[0m\n\u001b[1;32m   3402\u001b[0m             \u001b[0;32mexcept\u001b[0m \u001b[0mException\u001b[0m \u001b[0;32mas\u001b[0m \u001b[0me\u001b[0m\u001b[0;34m:\u001b[0m\u001b[0;34m\u001b[0m\u001b[0m\n",
      "\u001b[0;32m<ipython-input-304-e9de9997724e>\u001b[0m in \u001b[0;36mcompute_final_costs\u001b[0;34m(input_row)\u001b[0m\n\u001b[1;32m     16\u001b[0m     \u001b[0;32mfor\u001b[0m \u001b[0mperson_idx\u001b[0m \u001b[0;32min\u001b[0m \u001b[0mxrange\u001b[0m\u001b[0;34m(\u001b[0m\u001b[0mn_people\u001b[0m\u001b[0;34m)\u001b[0m\u001b[0;34m:\u001b[0m \u001b[0;31m# find this person's stall and put them in;\u001b[0m\u001b[0;34m\u001b[0m\u001b[0m\n\u001b[1;32m     17\u001b[0m         \u001b[0mmin_costs\u001b[0m \u001b[0;34m=\u001b[0m \u001b[0mnp\u001b[0m\u001b[0;34m.\u001b[0m\u001b[0mwhere\u001b[0m\u001b[0;34m(\u001b[0m\u001b[0mleft_costs\u001b[0m \u001b[0;34m<\u001b[0m \u001b[0mright_costs\u001b[0m\u001b[0;34m,\u001b[0m \u001b[0mleft_costs\u001b[0m\u001b[0;34m,\u001b[0m \u001b[0mright_costs\u001b[0m\u001b[0;34m)\u001b[0m \u001b[0;31m# min of left or right\u001b[0m\u001b[0;34m\u001b[0m\u001b[0m\n\u001b[0;32m---> 18\u001b[0;31m         \u001b[0mbest_stalls\u001b[0m \u001b[0;34m=\u001b[0m \u001b[0mnp\u001b[0m\u001b[0;34m.\u001b[0m\u001b[0mwhere\u001b[0m\u001b[0;34m(\u001b[0m\u001b[0mmin_costs\u001b[0m \u001b[0;34m==\u001b[0m \u001b[0mmin_costs\u001b[0m\u001b[0;34m.\u001b[0m\u001b[0mmax\u001b[0m\u001b[0;34m(\u001b[0m\u001b[0;34m)\u001b[0m\u001b[0;34m)\u001b[0m\u001b[0;34m[\u001b[0m\u001b[0;36m0\u001b[0m\u001b[0;34m]\u001b[0m\u001b[0;34m\u001b[0m\u001b[0m\n\u001b[0m\u001b[1;32m     19\u001b[0m \u001b[0;34m\u001b[0m\u001b[0m\n\u001b[1;32m     20\u001b[0m         \u001b[0;32mif\u001b[0m \u001b[0mlen\u001b[0m\u001b[0;34m(\u001b[0m\u001b[0mbest_stalls\u001b[0m\u001b[0;34m)\u001b[0m \u001b[0;34m==\u001b[0m \u001b[0;36m1\u001b[0m\u001b[0;34m:\u001b[0m\u001b[0;34m\u001b[0m\u001b[0m\n",
      "\u001b[0;31mKeyboardInterrupt\u001b[0m: "
     ]
    }
   ],
   "source": [
    "write_output(inputs, compute_final_costs, problem_name, size)"
   ]
  },
  {
   "cell_type": "markdown",
   "metadata": {
    "hidden": true,
    "run_control": {
     "frozen": false,
     "read_only": false
    }
   },
   "source": [
    "## Fashion Show"
   ]
  },
  {
   "cell_type": "markdown",
   "metadata": {
    "hidden": true,
    "run_control": {
     "frozen": false,
     "read_only": false
    }
   },
   "source": [
    "### Problem Statement"
   ]
  },
  {
   "cell_type": "markdown",
   "metadata": {
    "hidden": true,
    "run_control": {
     "frozen": false,
     "read_only": false
    }
   },
   "source": [
    "You are about to host a fashion show to show off three new styles of clothing. The show will be held on a stage which is in the most fashionable of all shapes: an N-by-N grid of cells.\n",
    "\n",
    "Each cell in the grid can be empty (which we represent with a . character) or can contain one fashion model. The models come in three types, depending on the clothing style they are wearing: +, x, and the super-trendy o. A cell with a + or x model in it adds 1 style point to the show. A cell with an o model in it adds 2 style points. Empty cells add no style points.\n",
    "\n",
    "To achieve the maximum artistic effect, there are rules on how models can be placed relative to each other.\n",
    "\n",
    "Whenever any two models share a row or column, at least one of the two must be a +.\n",
    "Whenever any two models share a diagonal of the grid, at least one of the two must be an x.\n",
    "Formally, a model located in row i0 and column j0 and a model located in row i1 and column j1 share a row if and only if i0 = i1, they share a column if and only if j0 = j1, and they share a diagonal if and only if i0 + j0 = i1 + j1 or i0 - j0 = i1 - j1.\n",
    "\n",
    "For example, the following grid is not legal:\n",
    "\n",
    "...\n",
    "x+o\n",
    ".+.\n",
    "The middle row has a pair of models (x and o) that does not include a +. The diagonal starting at the + in the bottom row and running up to the o in the middle row has two models, and neither of them is an x.\n",
    "\n",
    "However, the following grid is legal. No row, column, or diagonal violates the rules.\n",
    "\n",
    "+.x\n",
    "+x+\n",
    "o..\n",
    "Your artistic advisor has already placed M models in certain cells, following these rules. You are free to place any number (including zero) of additional models of whichever types you like. You may not remove existing models, but you may upgrade as many existing + and x models into o models as you wish, as long as the above rules are not violated.\n",
    "\n",
    "Your task is to find a legal way of placing and/or upgrading models that earns the maximum possible number of style points.\n",
    "\n",
    "Input\n",
    "\n",
    "The first line of the input gives the number of test cases, T. T test cases follow. Each test case begins with one line with two integers N and M, as described above. Then, M more lines follow; the i-th of these lines has a +, x, or o character (the type of the model) and two integers Ri and Ci (the position of the model). The rows of the grid are numbered 1 through N, from top to bottom. The columns of the grid are numbered 1 through N, from left to right.\n",
    "\n",
    "Output\n",
    "\n",
    "For each test case, first output one line containing Case #x: y z, where x is the test case number (starting from 1), y is the number of style points earned in your arrangement, and z is the total number of models you have added and/or substituted in. Then, for each model that you have added or substituted in, output exactly one line in exactly the same format described in the Input section, where the character is the type of the model that you have added or substituted in. These z lines can be in any order.\n",
    "\n",
    "If there are multiple valid answers, you may output any one of them.\n",
    "\n",
    "Limits\n",
    "\n",
    "1 ≤ T ≤ 100.\n",
    "1 ≤ N ≤ 100.\n",
    "1 ≤ Ci ≤ N, for all i.\n",
    "0 ≤ M ≤ N2.\n",
    "No two pre-placed models appear in the same cell.\n",
    "It is guaranteed that the set of pre-placed models follows the rules.\n",
    "Small dataset\n",
    "\n",
    "Ri = 1, for all i. (Any models that are pre-placed are in the top row. Note that you may add/replace models in that row and/or add models in other rows.)\n",
    "Large dataset\n",
    "\n",
    "1 ≤ Ri ≤ N, for all i.\n",
    "Sample\n",
    "\n",
    "\n",
    "Input \n",
    " \t\n",
    "Output \n",
    " \n",
    "3\n",
    "2 0\n",
    "1 1\n",
    "o 1 1\n",
    "3 4\n",
    "+ 2 3\n",
    "+ 2 1\n",
    "x 3 1\n",
    "+ 2 2\n",
    "\n",
    "Case #1: 4 3\n",
    "o 2 2\n",
    "+ 2 1\n",
    "x 1 1\n",
    "Case #2: 2 0\n",
    "Case #3: 6 2\n",
    "o 2 3\n",
    "x 1 2\n",
    "\n",
    "The sample output displays one set of answers to the sample cases. Other answers may be possible. Note that the last sample case would not appear in the Small dataset.\n",
    "\n",
    "In sample case #1, the grid is 2-by-2 and is initially blank. The output corresponds to the following grid. (In these explanations, we will use . to denote a blank cell.)\n",
    "\n",
    "x.\n",
    "+o\n",
    "In sample case #2, the only cell is already occupied by an o model, and it is impossible to add a new model or replace the o model.\n",
    "\n",
    "In sample case #3, the grid looks like this before you place any models:\n",
    "\n",
    "...\n",
    "+++\n",
    "x..\n",
    "The output corresponds to this grid:\n",
    "\n",
    ".x.\n",
    "++o\n",
    "x.."
   ]
  },
  {
   "cell_type": "markdown",
   "metadata": {
    "run_control": {
     "frozen": false,
     "read_only": false
    }
   },
   "source": [
    "# Round 2"
   ]
  },
  {
   "cell_type": "markdown",
   "metadata": {
    "collapsed": true,
    "run_control": {
     "frozen": false,
     "read_only": false
    }
   },
   "source": [
    "## Alphabet Cake"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 12,
   "metadata": {
    "run_control": {
     "frozen": false,
     "read_only": false
    }
   },
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "3\r\n",
      "3 3\r\n",
      "G??\r\n",
      "?C?\r\n",
      "??J\r\n",
      "3 4\r\n",
      "CODE\r\n",
      "????\r\n",
      "?JAM\r\n",
      "2 2\r\n",
      "CA\r\n",
      "KE"
     ]
    }
   ],
   "source": [
    "problem_name = \"alphabet_cake\"\n",
    "write_example_file(problem_name,\n",
    "\"\"\"3\n",
    "3 3\n",
    "G??\n",
    "?C?\n",
    "??J\n",
    "3 4\n",
    "CODE\n",
    "????\n",
    "?JAM\n",
    "2 2\n",
    "CA\n",
    "KE\"\"\")\n",
    "! cat ./alphabet_cake_ex.in"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 55,
   "metadata": {
    "run_control": {
     "frozen": false,
     "read_only": false
    }
   },
   "outputs": [],
   "source": [
    "size = \"large\"\n",
    "n_cases, inputs = read_input(problem_name, size, raw=True)\n",
    "inputs = map(lambda x: x.strip(), inputs)"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "metadata": {},
   "outputs": [],
   "source": [
    "i = 0\n",
    "case_num = 1\n",
    "with open(problem_name + \"_\" + size + \".out\", 'w') as out_file:\n",
    "    while i < len(inputs):\n",
    "        cake_height, cake_width = map(int, inputs[i].split())\n",
    "\n",
    "        cake = pd.DataFrame(map(list, inputs[i + 1 : i + cake_height + 1]))\n",
    "\n",
    "        # fill in row-wise in first (because I like this order)\n",
    "        cake = cake.transpose()\n",
    "        cake.replace(\"?\", np.nan, inplace=True)\n",
    "        cake.ffill(inplace=True)\n",
    "        cake.bfill(inplace=True)\n",
    "\n",
    "        # now fill column-wise as necessary\n",
    "        cake = cake.transpose()\n",
    "        cake.ffill(inplace=True)\n",
    "        cake.bfill(inplace=True)\n",
    "\n",
    "        out_file.write(\"Case #{}:\\n\".format(case_num))\n",
    "        out_file.write(cake.to_string(header=None, index=None).replace(\" \", \"\") + \"\\n\")\n",
    "        \n",
    "\n",
    "        i += cake_height + 1 # skip to next problem\n",
    "        case_num += 1"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "metadata": {},
   "outputs": [],
   "source": [
    "! head -n 20 alphabet_cake_small.out"
   ]
  },
  {
   "cell_type": "markdown",
   "metadata": {
    "run_control": {
     "frozen": false,
     "read_only": false
    }
   },
   "source": [
    "## Ratatouille"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "metadata": {
    "collapsed": true,
    "run_control": {
     "frozen": false,
     "read_only": false
    }
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
   "version": "2.7.12"
  },
  "latex_envs": {
   "LaTeX_envs_menu_present": true,
   "autocomplete": true,
   "bibliofile": "biblio.bib",
   "cite_by": "apalike",
   "current_citInitial": 1,
   "eqLabelWithNumbers": true,
   "eqNumInitial": 0,
   "hotkeys": {
    "equation": "Ctrl-E",
    "itemize": "Ctrl-I"
   },
   "labels_anchors": false,
   "latex_user_defs": false,
   "report_style_numbering": false,
   "user_envs_cfg": false
  },
  "toc": {
   "colors": {
    "hover_highlight": "#DAA520",
    "running_highlight": "#FF0000",
    "selected_highlight": "#FFD700"
   },
   "moveMenuLeft": true,
   "nav_menu": {
    "height": "264px",
    "width": "252px"
   },
   "navigate_menu": true,
   "number_sections": true,
   "sideBar": true,
   "threshold": 4,
   "toc_cell": true,
   "toc_section_display": "block",
   "toc_window_display": false,
   "widenNotebook": false
  }
 },
 "nbformat": 4,
 "nbformat_minor": 2
}
