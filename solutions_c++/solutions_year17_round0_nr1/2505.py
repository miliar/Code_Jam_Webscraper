#include <iostream>
#include <string>
#include <vector>
#include <stdio.h>
#include <string.h>

#define REP(i, n) for (int (i) = 0; (i) < (n); ++(i))

using namespace std;

int flip(string& s, int pos, int len) {
  int delta = 0;

  REP(j, len) {
    int i = j + pos;
    if (s[i] == '-') {
      s[i] = '+';
      delta++;
    } else {
      s[i] = '-';
      delta--;
    }
  }

  return delta;
}

void solve() {
  string s;
  int len;
  cin >> s >> len;
  int cur = 0;
  for (char c : s) if (c == '+') ++cur;
  int cnt = 0;
  for (int i = 0; i + len <= s.size(); ++i) {
    if (s[i] == '-') {
      cur += flip(s, i, len);
      cnt += 1;
    }
  }
  if (cur == s.size()) {
    printf("%d\n", cnt);
  } else {
    printf("IMPOSSIBLE\n");
  }
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
