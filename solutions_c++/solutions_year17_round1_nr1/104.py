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
#define MAXN 30

int N, M;
char g[MAXN][MAXN], ans[MAXN][MAXN];
int main() {
  freopen("input", "r", stdin);
  freopen("output", "w", stdout);
  int cs;
  cin >> cs;
  REP(csn, 1, cs + 1) {
    printf("Case #%d:\n", csn);
    //cerr << csn << endl;
    vector<PII> pos;
    cin >> N >> M;
    int rcol = -1;
    REP(i,0,N) {
      scanf("%s", g[i]);
      REP(j,0,M) {
        if (g[i][j] != '?') {
          pos.push_back(PII(j,i));
          rcol = max(rcol, j);
        }
      }
    }
    sort(pos.begin(), pos.end());
    int K = pos.size(), lastCol = -1;
    FILL(ans, 0);
    REP(i,0,K) {
      int j = i;
      while (j < K && pos[j].first == pos[i].first) j++;
      int col = pos[i].first, lastRow = -1;
      int finCol = col == rcol ? M-1 : col;
      REP(t,i,j) {
        char ch = g[pos[t].second][pos[t].first];
        int finRow = t == j-1 ? N-1 : pos[t].second;
        REP(r,lastRow+1, finRow+1) {
          REP(c,lastCol+1, finCol+1) {
            ans[r][c] = ch;
          }
        }
        lastRow = finRow;
      }
      lastCol = col;
      i = j - 1;
    }
    REP(i,0,N) cout << ans[i] << endl;
  }
  return 0;
}
