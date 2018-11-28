#include <algorithm>
#include <iostream>
#include <map>
#include <set>
#include <sstream>
#include <string>
#include <vector>
#include <utility>

using namespace std;

bool iscorrect(unsigned long long n) {
  vector<int> digits;

  while (n > 0) {
    digits.push_back(n % 10);
    n /= 10;
  }

  reverse(digits.begin(), digits.end());

  for (size_t i = 0; i < digits.size() - 1; ++i) {
    int& a = digits[i];
    int& b = digits[i+1];
    if (a > b)
      return false;
  }

  return true;
}

unsigned long long bf(unsigned long long n) {
  while (!iscorrect(n)) {
    n--;
  }

  return n;
}

int main() {
  int T=0;
  cin >> T;

  for (int test = 1; test <= T; ++test) {
    unsigned long long n = 0;
    cin >> n;

    vector<int> digits;

    while (n > 0) {
      digits.push_back(n % 10);
      n /= 10;
    }

    reverse(digits.begin(), digits.end());

    bool is_ok = false;
    while (!is_ok) {
      is_ok = true;
      for (size_t i = 0; i < digits.size() - 1; ++i) {
        int& a = digits[i];
        int& b = digits[i+1];

        if (a > b) {
          is_ok = false;
          if (a == 1) {
            if (i == 0) {
              digits.resize(digits.size() - 1);
              for (size_t j = 0; j < digits.size(); ++j)
                digits[j] = 9;
            } else {
              a = 0;
            }
          } else {
            a--;
            for (size_t j = i + 1; j < digits.size(); ++j)
              digits[j] = 9;
          }

          break;
        }
      }
    }

    cout << "Case #" << test << ": ";
    for (auto i : digits)
      cout << i;
    cout << endl;
  }
}
