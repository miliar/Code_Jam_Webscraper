////////////////////////////////////////////////////////////////////////////////
/**
 * @file p1.cpp
 * @date 2017-04-08
 * @author Tiago Lobato Gimenes    (tlgimenes@gmail.com)
 *
 * @copyright Tiago Lobato Gimenes 2016. All rights reserved.
 *
 * @brief
 *
 * This file contains implementation of the correspoding header file, i.e. .hpp,
 * .hh or .h
 */
////////////////////////////////////////////////////////////////////////////////

#include <iostream>
#include <cstdio>

////////////////////////////////////////////////////////////////////////////////

void swap_at(int it, std::string& pancakes, int size) {
  int end = it+size;
  for(int i=it; i < end; i++) {
    pancakes[i] = pancakes[i] == '-' ? '+' : '-';
  }
}

////////////////////////////////////////////////////////////////////////////////

std::string solve(std::string& pancakes, int size) {
  int n = 0;
  
  for(int it=0; it < pancakes.size()-size+1; it++) {
    while(it < pancakes.size()-size+1 && pancakes[it] == '+') it++;

    if(it < pancakes.size()-size+1) {
      n++;
      swap_at(it, pancakes, size);
    }
  }

  for(int it=pancakes.size()-size+1; it < pancakes.size(); it++) {
    if(pancakes[it] == '-') 
      return "IMPOSSIBLE"; 
  }

  return std::to_string(n);
}

////////////////////////////////////////////////////////////////////////////////

int main() {
  int n;

  std::cin >> n;
  for(int i=0; i < n; i++) {
    std::string pancakes;
    int size;
    char c;

    getchar();
    while((c = getchar()) != ' ') pancakes.push_back(c);
    std::cin >> size;

    std::cout << "Case #" << i+1 << ": " << solve(pancakes, size) << std::endl;
  }
  return 0;
}

////////////////////////////////////////////////////////////////////////////////
