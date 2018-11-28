#include <cstdio>
#include <cstring>
#include <cassert>
#include <iostream>
#include <algorithm>

#define FOR(i, a, b) for (int i = (a); i < (b); ++i)
#define REP(i, n) FOR (i, 0, n)
#define _ << " _ " <<
#define TRACE(x) cerr << #x << " = " << x << endl
#define debug(...) fprintf(stderr, __VA_ARGS__)

// #define TRACE(x)
// #define debug(...)

using namespace std;

typedef long long llint;

int n;
char s[21];

int visited[21][10][2], cookie;

bool dfs(int pos, int lo, bool g, llint val) {
  if (pos == n) {
    printf("%lld\n", val);
    return true;
  }

  if (visited[pos][lo][g] == cookie)
    return false;

  visited[pos][lo][g] = cookie;

  int hi = g ? s[pos]-'0' : 9;
  for (int d = hi; d >= lo; --d) {
    if (dfs(pos+1, d, g && d == hi, val * 10 + d))
      return true;
  }

  return false;
}

void solve(void) {
  scanf("%s", s);
  n = int(strlen(s));

  ++cookie;
  assert(dfs(0, 0, true, 0));
}

int main(void) {
  int t;
  scanf("%d", &t);
  REP (i, t) {
    printf("Case #%d: ", i+1);
    solve();
  }
  return 0;
}
