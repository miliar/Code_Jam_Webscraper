#include <iostream>
#include <vector>
#include <map>
#include <set>
#include <unordered_map>
#include <unordered_set>
#include <algorithm>
#include <utility>
#include <memory>
#include <cstdint>

using namespace std;

int main() {
  freopen("in", "r", stdin);
  freopen("out", "w", stdout);

  int cases; cin >> cases;
  for (int cas = 1; cas <= cases; ++cas) {
    string s; cin >> s;
    int b = 0, a = 0;
    for (int i = 1; i < s.length(); ++i) {
      if (s[i-1] < s[i]) a = b = i;
      else if (s[i-1] == s[i]) ++a;
      else if (s[i-1] > s[i]) break;
    }
    if (a != s.length() - 1) {
      s[b] -= 1;
      for (int i = b + 1; i < s.length(); ++i) s[i] = '9';
    }
    if (s[0] == '0') s = string(s.begin() + 1, s.end());
    cout << "Case #" << cas << ": " << s << endl;
  }
  return 0;
}
