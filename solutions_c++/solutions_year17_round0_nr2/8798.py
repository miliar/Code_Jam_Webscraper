////////////////////////////////////////////////////////////////////////////////
/**
 * @file p2.cpp
 * @date 2017-04-07
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
#include <cstdlib>
#include <string>

////////////////////////////////////////////////////////////////////////////////

unsigned long long int solve(std::string& num) {
  unsigned long long int input = std::stoll(num);
  unsigned long long int diff = 0, pow10 = 1, it, last;

  for(it = num.size()-1; it > 0; it--) {
    if((num[it-1] > num[it]) || (num[it-1] == num[it] && diff > 0)) {
      last = (num[it] - '0') * pow10;
      if(last)
        diff += (diff == 0 ? std::stoll(num.substr(it, num.size())) + 1 : last);
      else 
        diff += (diff == 0 ? std::stoll(num.substr(it, num.size())) + 1 : pow10/10);
    }
    pow10 *= 10;
  }

  return input - diff;
}

////////////////////////////////////////////////////////////////////////////////

int main() {
  std::string num;
  int n;

  std::cin >> n;
  for(int i=0; i < n; i++) {
    std::cin >> num;
    unsigned long long int res = solve(num);
    std::string st = std::to_string(res);
    
    for(int j=st.size()-1; j > 0; j--)
      if(st[j-1] > st[j]) {
        std::cout << "Case #" << i+1 << ": " << res << std::endl;
        std::cout << "Error at: " << j << std::endl;
        exit(EXIT_FAILURE);
      }

    std::cout << "Case #" << i+1 << ": " << res << std::endl;
  }

  return EXIT_SUCCESS;
}

////////////////////////////////////////////////////////////////////////////////
