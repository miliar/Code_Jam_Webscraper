#include <bits/stdc++.h>
using namespace std;

int solve(string s, int k) {
  int tot = 0;
  for (int i = 0; i < s.length(); i++) {
    if (s[i] == '-') {
      if (i + k - 1 >= s.length()) return -1;
      for (int j = i; j < i + k; j++) {
        s[j] = (s[j] == '-')? '+': '-';
      }
      tot++;
    }
  }
  return tot;
}

int main(void) {
  if (fopen("probAsmall.in", "r")) {
    freopen("probAsmall.in", "r", stdin);
    freopen("probAsmall.out", "w", stdout);
  }
  if (fopen("probAlarge.in", "r")) {
    freopen("probAlarge.in", "r", stdin);
    freopen("probAlarge.out", "w", stdout);
  }
  int t, k;
  string s;
  cin >> t;
  for (int i = 1; i <= t; i++) {
    cin >> s >> k;
    int val = solve(s,k);
    if (val != -1) printf("Case #%d: %d\n", i, solve(s, k));
    else printf("Case #%d: IMPOSSIBLE\n", i);
  }
  return 0;
}
