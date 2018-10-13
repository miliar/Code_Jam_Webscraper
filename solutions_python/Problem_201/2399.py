{
 "cells": [
  {
   "cell_type": "code",
   "execution_count": 22,
   "metadata": {
    "collapsed": true
   },
   "outputs": [],
   "source": [
    "import math\n",
    "\n",
    "def get_max_min_stall_distance(n, k):\n",
    "    occupied_stalls_pos_list = [0, (n + 1)]\n",
    "    \n",
    "    for users_count in range(1, (k + 1)):\n",
    "        # calculate the empty space in between\n",
    "        empty_space_list = []\n",
    "        \n",
    "        for occupied_stall_index in range(1, len(occupied_stalls_pos_list)):\n",
    "            empty_space_list.append(occupied_stalls_pos_list[occupied_stall_index] - occupied_stalls_pos_list[occupied_stall_index - 1])\n",
    "            \n",
    "        # find max of empty space\n",
    "        max_space_pos = 0\n",
    "        max_space = empty_space_list[max_space_pos]\n",
    "\n",
    "        for max_space_search_index in range(1, len(empty_space_list)):\n",
    "            if empty_space_list[max_space_search_index] > max_space:\n",
    "                max_space_pos = max_space_search_index\n",
    "                max_space = empty_space_list[max_space_pos]\n",
    "                \n",
    "        # calculate the position current user occupied\n",
    "        current_user_pos = occupied_stalls_pos_list[max_space_pos] + math.ceil(max_space / 2)\n",
    "        \n",
    "        # put the users into the \"occupied_stalls_pos_list\"\n",
    "        occupied_stalls_pos_list.append(current_user_pos)\n",
    "        occupied_stalls_pos_list.sort()        \n",
    "        \n",
    "        if users_count == k:\n",
    "            for last_user_search_index in range(0, len(occupied_stalls_pos_list)):\n",
    "                if occupied_stalls_pos_list[last_user_search_index] == current_user_pos:\n",
    "                    Ls = abs(current_user_pos - occupied_stalls_pos_list[last_user_search_index - 1]) - 1\n",
    "                    Rs = abs(current_user_pos - occupied_stalls_pos_list[last_user_search_index + 1]) - 1\n",
    "            \n",
    "    # calculate the max and min value of stall distance\n",
    "    if Ls > Rs:\n",
    "        min_dist = Rs\n",
    "        max_dist = Ls\n",
    "    else:\n",
    "        min_dist = Ls\n",
    "        max_dist = Rs\n",
    "    \n",
    "    max_min_dist = str(max_dist) + \" \" + str(min_dist)\n",
    "    \n",
    "    return max_min_dist"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 24,
   "metadata": {
    "collapsed": false
   },
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "5\n",
      "4 2\n",
      "Case #1: 1 0\n",
      "5 2\n",
      "Case #2: 1 0\n",
      "6 2\n",
      "Case #3: 1 1\n",
      "1000 1000\n",
      "Case #4: 0 0\n",
      "1000 1\n",
      "Case #5: 500 499\n"
     ]
    }
   ],
   "source": [
    "t = int(input())\n",
    "for i in range(1, t + 1):\n",
    "    stall_input = input().split()\n",
    "    n = int(stall_input[0])\n",
    "    k = int(stall_input[1])\n",
    "    print(\"Case #\" + str(i) + \": \" + str(get_max_min_stall_distance(n, k)))"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 25,
   "metadata": {
    "collapsed": false
   },
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "Case #1: 1 0\n",
      "Case #2: 1 0\n",
      "Case #3: 1 1\n",
      "Case #4: 0 0\n",
      "Case #5: 500 499\n",
      "Time to completion: 0.12810301780700684\n"
     ]
    }
   ],
   "source": [
    "# for testing dataset\n",
    "import time\n",
    "start_time = time.time()\n",
    "\n",
    "# read input from file, and print the output\n",
    "line_count = 0\n",
    "output_file = open('C:\\\\Users\\\\Tan\\\\Dropbox\\\\practice_programming\\\\Competitive Programming\\\\Google Code Jam\\\\2017\\\\Qualification Round\\\\C - Bathroom Stalls\\\\Dataset\\\\Experiment\\\\testing_input-output', 'w')\n",
    "\n",
    "with open(\"C:\\\\Users\\\\Tan\\\\Dropbox\\\\practice_programming\\\\Competitive Programming\\\\Google Code Jam\\\\2017\\\\Qualification Round\\\\C - Bathroom Stalls\\\\Dataset\\\\Experiment\\\\testing_input.txt\") as f:\n",
    "    for line in f:\n",
    "        line = line.rstrip('\\n')\n",
    "        \n",
    "        if line_count == 0:\n",
    "            t = int(line)\n",
    "        else:\n",
    "            stall_input = line.split()\n",
    "            n = int(stall_input[0])\n",
    "            k = int(stall_input[1])\n",
    "            output_line = \"Case #\" + str(line_count) + \": \" + str(get_max_min_stall_distance(n, k))\n",
    "            print(output_line)\n",
    "            output_file.write(output_line + \"\\n\")\n",
    "            \n",
    "        line_count = line_count + 1\n",
    "\n",
    "output_file.close()\n",
    "\n",
    "elapsed_time = time.time() - start_time\n",
    "print(\"Time to completion: \" + str(elapsed_time))"
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
    "# for small dataset 1\n",
    "import time\n",
    "start_time = time.time()\n",
    "\n",
    "# read input from file, and print the output\n",
    "line_count = 0\n",
    "output_file = open('C:\\\\Users\\\\Tan\\\\Dropbox\\\\practice_programming\\\\Competitive Programming\\\\Google Code Jam\\\\2017\\\\Qualification Round\\\\C - Bathroom Stalls\\\\Dataset\\\\', 'w')\n",
    "\n",
    "with open(\"C:\\\\Users\\\\Tan\\\\Dropbox\\\\practice_programming\\\\Competitive Programming\\\\Google Code Jam\\\\2017\\\\Qualification Round\\\\C - Bathroom Stalls\\\\Dataset\\\\\") as f:\n",
    "    for line in f:\n",
    "        line = line.rstrip('\\n')\n",
    "        \n",
    "        if line_count == 0:\n",
    "            t = int(line)\n",
    "        else:\n",
    "            stall_input = line.split()\n",
    "            n = int(stall_input[0])\n",
    "            k = int(stall_input[1])\n",
    "            output_line = \"Case #\" + str(line_count) + \": \" + str(get_max_min_stall_distance(n, k))\n",
    "            print(output_line)\n",
    "            output_file.write(output_line + \"\\n\")\n",
    "            \n",
    "        line_count = line_count + 1\n",
    "\n",
    "output_file.close()\n",
    "\n",
    "elapsed_time = time.time() - start_time\n",
    "print(\"Time to completion: \" + str(elapsed_time))"
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
   "version": "3.5.1"
  }
 },
 "nbformat": 4,
 "nbformat_minor": 0
}
