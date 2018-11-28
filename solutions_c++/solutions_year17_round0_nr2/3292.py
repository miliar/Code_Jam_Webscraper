#include <iostream>
#include <vector>
#include <set>
#include <algorithm>
#include <vector>
#include <string>

using namespace std;

#define FILENAME "B-large.in"

bool tidy(string s) {
  int n = s.size(), i;
  if (n < 2) return true;
  for (i = 0; i < n - 1; ++i) {
    if (s[i] > s[i + 1]) {
      break;
    }
  }
  if (i == n - 1) {
    return true;
  }
  return false;
}

string clever (string s) {
  if (tidy(s)) return s;
  int n = s.size(), i;
  for (i = 0; i < n - 1; ++i) {
    if (s[i] > s[i + 1]) {
      break;
    }
  }
  s[i] -= 1;
  for (size_t j = i + 1; j < s.size(); ++j) {
    s[j] = '9';
  }
  return s;
}

string solution(string s) {
  while (tidy(s) == false) {
    s = clever(s);
  }
  int pos;
  for (pos = 0; pos < s.size(); ++pos) {
    if (s[pos] != '0') {
      break;
    }
  }
  string ans = "";
  for (int i = pos; i < s.size(); ++i) {
    ans += s[i];
  }
  return ans;
}

int main() {
  freopen(FILENAME, "r", stdin); freopen("output.txt", "w", stdout);
  int t;
  cin >> t;
  for (int i = 1; i <= t; ++i) {
    string val;
    cin >> val;
    cout << "Case #" << i << ": " << solution(val) << endl;
  }
  return 0;
}