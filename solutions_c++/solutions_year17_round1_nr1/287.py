#include <cstdio>
#include <vector>
#include <map>
#include <iostream>
#include <algorithm>
#include <string>
using namespace std;
#define REP(i, N) for (int i = 0; i < N; i++)
#define FOR(i, a, b) for (int i = a; i <= b; i++)

int T, R, C;
char B[100][100];
bool row_clear(int i, int j1, int j2) {
  if (i < 0 || i >= R || j1 < 0 || j2 >= C) return false;
  FOR(j, j1, j2)
    if (B[i][j] != '?') {
      return false;
    }
  return true;
}
bool col_clear(int j, int i1, int i2) {
  if (j < 0 || j >= C || i1 < 0 || i2 >= R) return false;
  FOR(i, i1, i2)
    if (B[i][j] != '?')
      return false;
  return true;
}
void row_set(int i, int j1, int j2, char c) {
  if (i < 0 || i >= R || j1 < 0 || j2 >= C) return;
  FOR(j, j1, j2)
    B[i][j] = c;
}
void col_set(int j, int i1, int i2, char c) {
  if (j < 0 || j >= C || i1 < 0 || i2 >= R) return;
  FOR(i, i1, i2)
    B[i][j] = c;
}


struct rect {
  rect() : li(10000), hi(-1), lj(10000), hj(-1) {
  }
  void upd(int i, int j) {
    li = min(li, i);
    hi = max(hi, i);
    lj = min(lj, j);
    hj = max(hj, j);
  }
  bool cont(int i, int j) {
    if (hi == -1) return false;
    return li <= i && i <= hi && li <= j && j <= hj;
  }
  int li, hi, lj, hj;
};
int main() {
  scanf("%d", &T);
  FOR(cn, 1, T) {
    printf("Case #%d:\n", cn);

    scanf("%d%d", &R, &C);
    REP(i, R) scanf("%s", B[i]);
    map<int, rect> MR;
    REP(i, R) REP(j, C) {
      MR[B[i][j]].upd(i, j);
    }
    for (auto p : MR) {
      rect r = p.second;
      FOR(i, r.li, r.hi) FOR(j, r.lj, r.hj)
        B[i][j] = p.first;
    }
    //if (cn != 98) continue;
    //if (cn == 98){    REP(i, R) puts(B[i]); puts("");}
    while (true) {
      bool changed = false;
      REP(i, R) REP(j, C) {
        auto & ps = MR[B[i][j]];
        char pf = B[i][j];
        if (row_clear(ps.li-1, ps.lj, ps.hj)) {
          row_set(ps.li-1, ps.lj, ps.hj, pf);
          ps.li--; changed = true;
        }
        /*
        if (pf == 'G') {
          printf("row_clear(%d, %d, %d) = %d\n", ps.hi+1, ps.lj, ps.hj, row_clear(ps.hi+1, ps.lj, ps.hj, true));
          REP(i, R) puts(B[i]); puts("");
          }*/
        if (row_clear(ps.hi+1, ps.lj, ps.hj)) {
          row_set(ps.hi+1, ps.lj, ps.hj, pf);
          ps.hi++;changed = true;
        }
      }
      if (!changed) break;
    }

    //REP(i, R) puts(B[i]); puts("");
    
    while (true) {
      bool changed = false;
      REP(i, R) REP(j, C) {
        auto & ps = MR[B[i][j]];
        char pf = B[i][j];
        if (col_clear(ps.lj-1, ps.li, ps.hi)) {
          col_set(ps.lj-1, ps.li, ps.hi, pf);
          ps.lj--;changed = true;
        }
        if (col_clear(ps.hj+1, ps.li, ps.hi)) {
          col_set(ps.hj+1, ps.li, ps.hi, pf);
          ps.hj++;changed = true;
        }
      }
      if (!changed) break;
    }
    REP(i, R) puts(B[i]); puts("");
  }
  return 0;
}
