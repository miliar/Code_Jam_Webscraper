#include <cstdio>
#include <cstring>
#include <cassert>
#include <iostream>
#include <algorithm>

#include <queue>
#include <vector>

#define FOR(i, a, b) for (int i = (a); i < (b); ++i)
#define REP(i, n) FOR (i, 0, n)
#define _ << " _ " <<
#define TRACE(x) cerr << #x << " = " << x << endl
#define debug(...) fprintf(stderr, __VA_ARGS__)

// #define TRACE(x)
// #define debug(...)

using namespace std;

typedef long long llint;

void solve(void) {
  int n, k;
  static char s[15];
  
  scanf("%s%d", s, &k);
  n = int(strlen(s));

  int start = 0;
  REP (i, n) {
    if (s[i] == '-')
      start = start | (1 << i);
  }

  vector<int> dist(1<<n, -1);
  queue<int> q;
  
  dist[start] = 0;
  q.push(start);

  while (!q.empty()) {
    int u = q.front();
    q.pop();

    REP (i, n-k+1) {
      int v = u;
      FOR (j, i, i+k)
	v = v ^ (1 << j);
      if (dist[v] == -1) {
	dist[v] = 1 + dist[u];
	q.push(v);
      }
    }
  }

  if (dist[0] == -1)
    printf("IMPOSSIBLE\n");
  else
    printf("%d\n", dist[0]);
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
