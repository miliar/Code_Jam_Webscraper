#include <iostream>
#include <string>
#include <vector>
#include <stdio.h>
#include <string.h>

#define REP(i, n) for (int (i) = 0; (i) < (n); ++(i))

typedef long long LL;

using namespace std;

string str(LL x) {
  if (!x) return "0";
  string res;
  while (x) {
    res += '0' + x % 10;
    x /= 10;
  }
  reverse(res.begin(), res.end());
  return res;
}

LL toLL(string s) {
  LL x = 0;
  REP(i, s.size()) {
    x *= 10;
    x += s[i] - '0';
  }
  return x;
}

LL solve(LL x) {
  string s = str(x);
  REP(i, s.size()) {
    if (i && s[i - 1] > s[i]) {
      for(int j = i; j < s.size(); ++j) s[j] = '0';
      return solve(toLL(s) - 1);
    }
  }
  return x;
}

void solve() {
  LL x;
  cin >> x;
  cout << solve(x) << endl;
}

int main() {
  int T;
  scanf("%d", &T);
  REP(i, T) {
    printf("Case #%d: ", i + 1);
    solve();
  }  

  return 0;
}
