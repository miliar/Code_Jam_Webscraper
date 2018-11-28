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

const int MOD = 1e9 + 7;
const int MAXN = 1005;

int T, N, M, C;
int A[MAXN], B[MAXN];

inline void init() {
  for (int i = 0; i < N; ++i) {
    A[i] = MOD;
    B[i] = MOD;
  }
}

void solve(int t) {
  scanf("%d%d%d", &N, &C, &M);
  init();
  int la = 0, lb = 0;
  for (int i = 0; i < M; ++i) {
    int p, b;
    scanf("%d%d", &p, &b); --p;
    if (b == 1)
      A[la++] = p;
    else
      B[lb++] = p;
  }

  sort(A, A + la);
  sort(B, B + lb);

  int len = max(la, lb);
  for (int i = 0; i < len; ++i) {
    if (A[i] != B[i]) continue;
    for (int j = 0; j < len; ++j) {
      if (A[j] != B[i] && A[i] != B[j]) {
        swap(A[i], A[j]);
        break;
      }
    }
  }

  int ret = 0, sol = 0;
  for (int i = 0; i < len; ++i) {
    ret += A[i] == B[i] && (A[i] != 0);
    ++sol;
    sol += A[i] == B[i] && (A[i] == 0);
  }
  printf("Case #%d: %d %d\n", t, sol, ret);
}

int main(void) {
  scanf("%d", &T);
  for (int t = 0; t < T; ++t)
    solve(t + 1);
  return 0;
}
