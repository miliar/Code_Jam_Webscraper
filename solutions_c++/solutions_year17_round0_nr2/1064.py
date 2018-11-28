#include <iostream>
#include <string>
#include <stdexcept>

int  char2num(const char c) { return c - '0'; }
char num2char(const int n)  { return '0' + n; }

void solve(std::string &res, const std::string &s) {
  int digits[19] = { 0, };

  int min = 0;
  int end = 0;

  bool bAdjusted = false;

  for (auto c : s) {
    int cur = char2num(c);

    if (bAdjusted) {
      digits[end++] = 9;
    } else if (cur >= min) {
      min = cur;
      digits[end++] = cur;
    } else {
      bool bFound = false;

      for (int i = end - 1; i >= 1; --i) {
        if (digits[i] - 1 >= digits[i - 1]) 
        {
          --digits[i];
          bFound = true;
          break;
        } 
      
        digits[i] = 9;
      }

      if (!bFound) {
        if (digits[0] != 1) {
          digits[0]--;
          bFound = true;
        } else {
          digits[0] = 9;
        }
      }

      min = 9;

      if (bFound) 
        digits[end++] = 9;
      bAdjusted = true;
    }
  }

  for (int i = 0; i < end; ++i) {
    res.push_back(num2char(digits[i]));
  }
}

int main(int argc, char **argv) {
  int T = 0;

  std::cin >> T;

  for (int i = 0; i < T; ++i) {
    std::string N;

    std::cin >> N;

    std::string sol;
    
    solve(sol, N);

    std::cout << "Case #" << (i + 1) << ": " << sol << std::endl;
  }

  return 0;
}
