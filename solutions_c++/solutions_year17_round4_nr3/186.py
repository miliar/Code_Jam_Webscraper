#include <algorithm>
#include <cassert>
#include <cstring>
#include <iostream>

using namespace std;

#define FOR(i, a, b) for (int i = (a); i < (b); ++i)
#define REP(i, n) FOR(i, 0, n)
#define TRACE(x) cout << #x << " = " << x << endl
#define _ << " _ " <<

typedef long long llint;

namespace TwoSatSlow {
  const int MAXN = 1000;
 
  vector<int> E[MAXN];
  int bio[MAXN], val[MAXN];
  int n, cookie;

  
  bool dfs(int x, int v) {
    if (val[x] != -1) return val[x] == v;
    val[x] = v;
    bio[x] = cookie;
    for (int y: E[x*2+v])
      if (!dfs(y/2, y&1)) return false;
    return true;
  }
 
  bool solve() {
    REP(i, n) val[i] = -1;
    REP(i, n) {
      cookie++;
      if (!dfs(i, 0)) {
        REP(j, n)
          if (bio[j] == cookie) val[j] = -1;
        cookie++;
        if (!dfs(i, 1)) return false;
      }
    }
    return true;
  }
}

const int MAXN = 55;

char a[MAXN][MAXN];
vector<int> v[MAXN][MAXN];
int bio[MAXN][MAXN];
int cookie;

int main(void) {
  int TC;
  scanf("%d", &TC);
  for (int tp = 1; tp <= TC; ++tp, fflush(stdout)) {
    int N, M;
    scanf("%d %d", &N, &M);
    REP(i, N) scanf("%s", a[i]);
    REP(i, N) REP(j, M) v[i][j].clear();

    vector<pair<int, int>> beams;
    REP(i, N) REP(j, M) {
      if (a[i][j] == '-' || a[i][j] == '|') {
        static int sdx[] = {1, 0, -1, 0};
        static int sdy[] = {0, 1, 0, -1};
        int idx = beams.size();
        beams.push_back({i, j});
        
        REP(k, 4) {
          int dx = sdx[k], dy = sdy[k];
          int x = i + dx, y = j + dy;
          cookie++;
          while (true) {
            if (x >= N || x < 0 || y >= M || y < 0) break;
            if (bio[x][y] == cookie) break;
            if (a[x][y] == '#') break;

            bio[x][y] = cookie;
            v[x][y].push_back(2*idx + (k % 2));

            if (a[x][y] == '\\') {
              swap(dx, dy);
            } else if (a[x][y] == '/') {
              swap(dx, dy);
              dx *= -1;
              dy *= -1;
            }
            x += dx;
            y += dy;
          }
        }
      }
    }
    
    
    TwoSatSlow::n = beams.size();
    REP(i, (int)beams.size()*2) TwoSatSlow::E[i].clear();

    
    bool ok = true;
    REP(i, N) REP(j, M) {
      if (a[i][j] == '|' || a[i][j] == '-') {
        for (int x: v[i][j]) {
          TwoSatSlow::E[x].push_back(x^1);
        }
      } else if (a[i][j] == '.') {
        if (v[i][j].size() == 2) {
          int x = v[i][j][0];
          int y = v[i][j][1];
          TwoSatSlow::E[x^1].push_back(y);
          TwoSatSlow::E[y^1].push_back(x);
        } else if (v[i][j].size() == 1) {
          int x = v[i][j][0];
          TwoSatSlow::E[x^1].push_back(x);
        } else {
          ok = false;
          break;
        }
      }
    }

    if (ok) {
      ok = TwoSatSlow::solve();
    }
    
    printf("Case #%d: ", tp);
    if (ok) {
      puts("POSSIBLE");
      REP(i, (int)beams.size()) {
        a[beams[i].first][beams[i].second] = TwoSatSlow::val[i] ? '-' : '|';
      }
      REP(i, N) puts(a[i]);
    } else {
      puts("IMPOSSIBLE");
    }
  }
  return 0;
}
