#include <algorithm>
#include <iostream>
#include <string>
#include <vector>

using namespace std;
using LL = long long;

string er(string s) {
  while (s.size() > 1 && s[0] == '0')
    s.erase(s.begin());
  return s;
}

bool cmp(string a, string b) {
  a = er(a); b = er(b);
  return make_pair(a.size(), a) < make_pair(b.size(), b);
}

bool check(string s) {
  const int n = s.size();
  for (int i = 1; i < n; ++i) {
    if (s[i - 1] > s[i])
      return false;
  }

  return true;
}

string solve(string s) {
  const int n = s.size();
  if (n == 1)
    return s;

  string a(n - 1, '9');
  vector<string> res;
  if (check(s))
    res.push_back(s);
  res.push_back(a);
  for (int d = 0; d < n; ++d) {
    string cur = s;
    if (cur[d] == '0')
      continue;
    cur[d]--;
    fill(cur.begin() + d + 1, cur.end(), '9');
    cur = er(cur);
    if (check(cur))
      res.push_back(cur);
  }

  sort(res.begin(), res.end(), cmp);
  return res.back();
}

int main() {
  //for (int i = 1; i < 500; ++i) {
  //  string s = to_string(i);
  //  cout << s << " : " << solve(s) << endl;
  //}
  int T;
  cin >> T;
  for (int t = 1; t <= T; ++t) {
    cout << "Case #" << t << ": ";
    string s;
    cin >> s;
    cout << solve(s) << endl;
  }
}
