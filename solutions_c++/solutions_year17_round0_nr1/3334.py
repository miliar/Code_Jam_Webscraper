#include <iostream>
#include <vector>
#include <set>
#include <algorithm>
#include <vector>
#include <string>

using namespace std;

#define FILENAME "A-large.in"

int change(string& s, int pos, int k) {
  if (pos + k > s.size()) return 0;
  for (int i = pos; i < pos + k; ++i) {
    if (s[i] == '+') 
      s[i] = '-';
    else
      s[i] = '+';
  }
  return 1;
}

int solve(string& s, int k) {
  int res = 0;
  for (int pos = 0; pos < s.size(); ++pos) {
    int temp = (s[pos] == '-' ? 1 : 0); 
    int flag = 0;
    if (temp) flag = change(s, pos, k);
    res += flag * temp;
  }
  for (size_t i = 0; i < s.size(); ++i) {
    if (s[i] == '-')
      return -1;
  }
  return res;
}

int main() {
  freopen(FILENAME, "r", stdin); freopen("output.txt", "w", stdout);
  int t;
  cin >> t;
  for (int i = 1; i <= t; ++i) {
    string s;
    int k;
    cin >> s >> k;
    cout << "Case #" << i << ": ";
    int ans = solve(s, k);
    if (ans != -1)
      cout << ans << endl;
    else
      cout << "IMPOSSIBLE" << endl;
  }
  return 0;
}