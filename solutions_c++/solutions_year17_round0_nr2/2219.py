#include <bits/stdc++.h>
#define vec vector
#define sz(c) int(c.size())
#define FOR(i, a, b) for (int i = a; i < (b); ++i)
#define DOWN(i, a, b) for(int i = (a) - 1; i >= (b); --i)
using namespace std;
typedef long long ll;
typedef pair<int,int> pii;
typedef vec<int> vi;

void solve(int testcase) {
  cout << "Case #" << testcase << ": ";
  string s;
  cin >> s;
  int br = -1;
  for (int i = 0; i < sz(s) - 1; ++i) {
    if (s[i] > s[i + 1]) {
      br = i;
      break;
    }
  }
  if (br == -1) {
    cout << s << "\n";
    return;
  }
  for (int i = br + 1; i < sz(s); ++i) {
    s[i] = '9';
  }
  while (br > 0 && s[br - 1] == s[br]) {
    s[br] = '9';
    br -= 1;
  }
  assert(s[br] != '0');
  if (s[br] == '1') {
    assert(br == 0);
    cout << s.substr(1) << "\n";
  } else {
    s[br] = char(s[br] - 1);
    cout << s << "\n";
  }
}

int main() {
  ios_base::sync_with_stdio(false);
  cin.tie(0);

  int testcases;
  cin >> testcases;
  FOR(testcase, 1, testcases + 1) {
    cerr << "Case " << testcase << "/" << testcases << endl;
    solve(testcase);
  }

  return 0;
}
