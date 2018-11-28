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

int T, N, P;

void solve2(int t) {
  int d0 = 0, d1 = 0;
  for (int i = 0; i < N; ++i) {
    int x;
    scanf("%d", &x);
    if (x % 2 == 0) ++d0; else ++d1;
  }
  printf("Case #%d: %d\n", t, d0 + d1/2 + (d1 & 1));
}

void solve3(int t) {
  int d[3];
  d[0] = d[1] = d[2] = 0;
  for (int i = 0; i < N; ++i) {
    int x;
    scanf("%d", &x);
    ++d[x%3];
  }
  int b = 2 * min(d[1], d[2]);
  int sol = d[0] + b / 2 + (b & 1);
  int ost = max(d[1], d[2]) - min(d[1], d[2]);
  sol += ost / 3 + (ost % 3 != 0);
  printf("Case #%d: %d\n", t, sol);
}

void solve(int t) {
  scanf("%d%d", &N, &P);
  if (P == 2) solve2(t);
  if (P == 3) solve3(t);
}

int main(void) {
  scanf("%d", &T);
  for (int t = 0; t < T; ++t)
    solve(t + 1);
  return 0;
}
