#include <iostream>
#include <vector>
#include <map>
#include <set>
#include <unordered_map>
#include <unordered_set>
#include <algorithm>
#include <utility>
#include <memory>

using namespace std;

int main() {
  freopen("in", "r", stdin);
  freopen("out", "w", stdout);

  int cases; cin >> cases;
  for (int cas = 1; cas <= cases; ++cas) {
    string s; cin >> s;
    int k; cin >> k;
    bool f = false, impos = false;
    int y = 0;
    for (int i = 0; i < s.length(); ++i) {
      if (i >= k && s[i-k] == '!') f = !f;
      if (!f && s[i] == '-' || f && s[i] == '+') {
        if (i + k > s.length()) impos = true;
        f = !f;
        s[i] = '!';
        ++y;
      }
    }
    if (impos)
      cout << "Case #" << cas << ": IMPOSSIBLE" << endl;
    else
      cout << "Case #" << cas << ": " << y << endl;
  }
  return 0;
}
