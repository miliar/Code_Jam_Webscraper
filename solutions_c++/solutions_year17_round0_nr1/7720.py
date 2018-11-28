#include <algorithm>
#include <cassert>
#include <cmath>
#include <cstdio>
#include <cstdlib>
#include <cstring>
#include <iostream>
#include <map>
#include <set>
#include <stack>
#include <string>
#include <vector>
#include <queue>

using namespace std;

#define TRACE(x) cerr << #x << " " << x << endl
#define FOR(i, a, b) for (int i = (a); i < int(b); ++i)
#define REP(i, n) FOR(i, 0, n)
#define _ << " " <<

#define fst first
#define snd second

typedef long long llint;
typedef pair<int, int> pii;

const int B = 27397, MOD = 1e9 + 7;
const int B1 = 33941, MOD1 = 1e9 + 9;

const int MAXN = 1005;

char s[MAXN];

int t, n, k;

void solve(int t) {
  scanf("%s%d", s, &k);
  n = strlen(s);

  int sol = 0;
  for (int i = 0; i < n - k + 1; ++i) {
    if (s[i] == '-') {
      ++sol;
      for (int j = i; j < i + k; ++j)
        if (s[j] == '-') s[j] = '+'; else s[j] = '-';
    }
  }

  bool ok = true;
  for (int i = 0; i < n; ++i)
    ok &= s[i] == '+';

  if (ok)
    printf("Case #%d: %d\n", t, sol);
  else
    printf("Case #%d: IMPOSSIBLE\n", t);

}

int main(void) {
  scanf("%d", &t);
  for (int i = 0; i < t; ++i)
    solve(i + 1);
  return 0;
}
