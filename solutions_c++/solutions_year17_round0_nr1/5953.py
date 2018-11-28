#!/usr/bin/env cppsh

#include <iostream>
#include <string>

using namespace std;

class Solution
{
public:
  int make_happy(const std::string& str, int k) {
    std::string s(str);
    return helper(s, k, s.find_first_of("-"), 0);
  }

  int helper(std::string& str, int k, int pos, int flips) {
    if (str.find_first_of("-", pos) == std::string::npos)
      return flips;

    // flip k pancakes starting from pos
    for (int i = 0; i < k; ++i) {
      if (pos + i == str.size())
        return -1;
      str[pos + i] = (str[pos + i] == '-')? '+' : '-';
    }
    return helper(str, k, str.find_first_of("-", pos), flips + 1);
  }
};

int main(int argc, char *argv[])
{
  Solution soln;
  int T;
  scanf("%d\n", &T);
  for (int t = 1; t <= T; ++t) {
    char buf[1024] = { 0 };
    int k;
    scanf("%s %d\n", buf, &k);
    int flips = soln.make_happy(std::string(buf), k);
    if (flips >= 0)
      printf("Case #%d: %d\n", t, flips);
    else
      printf("Case #%d: IMPOSSIBLE\n", t);
  }
  
  return 0;
}
