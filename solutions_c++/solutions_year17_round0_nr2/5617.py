#include <iostream>
#include <string>
#include <vector>
#include <queue>
#include <unordered_set>
#include <algorithm>

using namespace std;

inline string vtos(std::vector<bool> b) {
  string s;
  for (int i = 0; i < b.size(); ++i) {
    s.push_back(b[i] ? '+' : '-');
  }
  return s;
}

inline void p(int t, string r) {
  cout << "Case #" << t << ": " << r << endl;
}


inline string solve(string s) {
  if (s.length() == 1) {
    return s;
  }
  // Find breach of rules
  int i = 0;
  for (; i < s.length() - 1 && s[i] <= s[i + 1]; ++i);
  if (i == s.length() - 1 && s[i - 1] <= s[i]) {
    return s;
  }
  for (int j = i + 1; j < s.length(); ++j) {
    s[j] = '9';
  }
  // Fix same-digit
  s[i] -= 1;
  while (i > 0 && s[i] < s[i - 1]) {
    s[i - 1] -= 1;
    s[i] = '9';
    --i;
  }
  if (i == 0 && s[i] == '0') {
    s.erase(s.begin());
  }
  return s;
}

int main() {
  int t;
  string s;

  cin >> t;
  for (int i = 1; i <= t; ++i) {
    cin >> s;
    string r = solve(s);
    p(i, r);
  }

  return 0;
}
