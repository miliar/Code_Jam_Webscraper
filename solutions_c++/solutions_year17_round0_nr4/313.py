#include <iostream>
#include <cstdio>
#include <cmath>
#include <cstring>
#include <algorithm>
#include <string>
#include <vector>
#include <stack>
#include <queue>
#include <set>
#include <map>
#include <sstream>
#include <complex>
#include <ctime>
#include <cassert>
#include <functional>

using namespace std;

typedef long long ll;
typedef vector<int> VI;
typedef pair<int,int> PII;

#define REP(i,s,t) for(int i=(s);i<(t);i++)
#define FILL(x,v) memset(x,v,sizeof(x))

const int INF = (int)1E9;
#define MAXN 105

int origX[MAXN][MAXN], origA[MAXN][MAXN], nowX[MAXN][MAXN], nowA[MAXN][MAXN];
bool outside(int x, int y, int N) {
  return x < 0 || x >= N || y < 0 || y >= N;
}
int main() {
  freopen("input", "r", stdin);
  freopen("output", "w", stdout);
  int cs;
  cin >> cs;
  REP(csn, 1, cs + 1) {
    printf("Case #%d: ", csn);
    cerr << csn << endl;
    int N, M;
    cin >> N >> M;
    FILL(origX, 0); FILL(origA, 0);
    REP(i,0,M) {
      char s[2];
      int x, y;
      scanf("%s%d%d", s, &x, &y); x--; y--;
      if (s[0] == '+') origA[x][y] = 1;
      else if (s[0] == 'x') origX[x][y] = 1;
      else origA[x][y] = origX[x][y] = 1;
    }
    memcpy(nowX, origX, sizeof(nowX));
    memcpy(nowA, origA, sizeof(nowA));
    REP(i,0,N) {
      REP(j,0,N) {
        bool ok = 1;
        REP(k,0,N) if (nowX[k][j] || nowX[i][k]) { ok = 0; break; }
        if (ok) nowX[i][j] = 1;
      }
    }
    vector<PII> order;
    REP(s,0,N) {
      REP(x,0,N-s) order.push_back(PII(x-s, x+s));
      REP(y,s+1,N) order.push_back(PII(N-1-s-y, N-1-s+y));
    }
    REP(oi,0,order.size()) {
      int a = order[oi].first, b = order[oi].second;
      int nx = (a + b) / 2, ny = b - nx;
      if (outside(nx, ny, N)) continue;
      bool ok = 1;
      REP(k,0,2*N-1) {
        if ((a + k) % 2) continue;
        int x = (a + k) / 2, y = k - x;
        if (outside(x, y, N)) continue;
        if (nowA[x][y]) { ok = 0; break; }
      }
      REP(k,-(N-1),N) {
        if ((k + b) % 2) continue;
        int x = (k + b) / 2, y = b - x;
        if (outside(x, y, N)) continue;
        if (nowA[x][y]) { ok = 0; break; }
      }
      if (ok) nowA[nx][ny] = 1;
    }
    int score = 0, cnt = 0;
    REP(i,0,N) {
      REP(j,0,N) {
        score += nowA[i][j] + nowX[i][j];
        cnt += (nowA[i][j] ^ origA[i][j]) || (nowX[i][j] ^ origX[i][j]);
      }
    }
    printf("%d %d\n", score, cnt);
    REP(i,0,N) {
      REP(j,0,N) {
        if ((nowA[i][j] ^ origA[i][j]) || (nowX[i][j] ^ origX[i][j])) {
          printf("%c %d %d\n", nowA[i][j] && nowX[i][j] ? 'o' : (nowA[i][j] ? '+' : 'x'),  i+1, j+1);
        }
      }
    }
  }
  return 0;
}
