/** \file

 Limits

1 ≤ T ≤ 100.
Every character in S is either + or -.
2 ≤ K ≤ length of S.
Small dataset: 2 ≤ length of S ≤ 10.
Large dataset: 2 ≤ length of S ≤ 1000.


3
---+-++- 3
+++++ 4
-+-+- 4

Case #1: 3
Case #2: 0
Case #3: IMPOSSIBLE

*/

#include "codejam.hh"

#define maxS 1000
struct Case : CaseBase {
  bool s[maxS];
  U S, K;
  U y;
  void read() {
    S = 0;
    while (getbool(s[S], '+', '-'))
      ++S;
    K = GETU;
    assert(K >= 2);
    assert(K <= S);
  }
  void print() {
    PUTU(y);
  }
  void show1() {
    cerr << "y: ";
    REP(i, S) cerr << (S ? '+' : '-');
  }
  void solve() {
    y = 0;
    U i = 0, e = S - K;
    for (; i <= e; ++i)
      y += flipped(i);
    for (; i < S; ++i)
      if (!s[i])
        return setImpossible(y);
  }
  void flip(U i) {
    U m = i + K;
    assert(m <= S);
    for (; i < m; ++i)
      s[i] = !s[i];
  }
  bool flipped(U i) {
    bool need = !s[i];
    if (need)
      flip(i);
    return need;
  }
};

CASES_MAIN(Case)
