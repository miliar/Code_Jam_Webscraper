#include <bits/stdc++.h>

#define FOR(i, a, b) for (int i = (int)(a); i < (int)(b); ++i)
#define REP(i, n) FOR(i, 0, n)
#define TRACE(x) cerr << #x << " = " << x << endl
#define _ << " _ " <<

#define x first
#define y second

using namespace std;

typedef long long ll;

const int MAXN = 1100;

void solve() {
  static char num[40];
  scanf("%s", num);
  bool change = true;
  while (change) {
    change = false;
    for (int i = 1; num[i]; ++i) {
      if (num[i-1] <= num[i]) continue;
      change = true;
      for (int j = i; num[j]; ++j)
        num[j] = '9';
      num[i-1]--;
    }
  }
  int i = 0;
  while (num[i] == '0') ++i;
  printf("%s\n", num + i);
}

int main(void) {
  int tests;
  scanf("%d", &tests);
  for (int test = 1; test <= tests; ++test) {
    printf("Case #%d: ", test);
    solve();
  }
  return 0;
}

