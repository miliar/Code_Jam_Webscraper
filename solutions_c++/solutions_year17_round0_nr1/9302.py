#include <algorithm>
#include <iomanip>
#include <ios>
#include <iostream>
#include <string>
#include <vector>

using std::cin;
using std::cout;
using std::domain_error;
using std::endl;
using std::istream;
using std::min;
using std::setprecision;
using std::streamsize;
using std::string;
using std::vector;

bool is_flipped_properly(const string& s) {
  for (string::size_type i = 0; i < s.size(); i++) {
    if (s[i] != '+') {
      return false;
    }
  }
  return true;
}

string& flip(string& s, int start, int end) {
  if (s.size() < end) {
    end = s.size();
  }

  for (int i = start; i < end; ++i) {
    if (s[i] == '+') {
      s[i] = '-';
    } else {
      s[i] = '+';
    }
  }
  return s;
}

int main() {
  int t;
  cin >> t;
  for (int i = 1; i <= t; ++i) {
    string s;
    int k;
    cin >> s >> k;

    int num_flips = 0;
    for (int j = 0; j < s.size() - k + 1; ++j) {
      if (s[j] == '-') {
        s = flip(s, j, j + k);
        ++num_flips;
      }
    }

    if (is_flipped_properly(s)) {
      cout
        << "Case #" << i << ": "
        << num_flips
        << endl;
    } else {
      cout
        << "Case #" << i << ": "
        << "IMPOSSIBLE"
        << endl;
    }
  }
  return 0;
}
