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

int G[MAXN], cnt[4];
set<VI> got;
void see(int d, int P, VI &ls) {
  int s = 0;
  REP(i,0,ls.size()) s += ls[i];
  if (ls.size() && s % P == 0) {
    got.insert(ls);
    return;
  }
  if (d == P) return;
  see(d+1, P, ls);
  REP(cc,0,P) {
    ls.push_back(d);
    see(d+1, P, ls);
  }
  REP(i,0,P) ls.pop_back();
}
bool super(VI v1, VI v2) {
  int cnt1[4] = {}, cnt2[4] = {};
  REP(i,0,v1.size()) cnt1[v1[i]]++;
  REP(i,0,v2.size()) cnt2[v2[i]]++;
  bool ok = 1;
  REP(i,0,4) if (cnt1[i] < cnt2[i]) ok = 0;
  return ok;
}

int dp[MAXN][MAXN][MAXN];
int solve(int c1, int c2, int c3) {
  if (dp[c1][c2][c3] != -1) return dp[c1][c2][c3];
  if (c1 == 0 && c2 == 0 && c3 == 0) return 0;
  int ans = 1;
  if (c1 >= 4) { // 1 1 1 1
    ans = max(ans, solve(c1-4, c2, c3) + 1);
  }
  if (c1 >= 2 && c2 >= 1) { // 1 1 2
    ans = max(ans, solve(c1-2, c2-1, c3) + 1);
  }
  if (c1 >= 1 && c3 >= 1) { // 1 3
    ans = max(ans, solve(c1-1, c2, c3-1) + 1);
  }
  if (c2 >= 2) { // 2 2
    ans = max(ans, solve(c1, c2-2, c3) + 1);
  }
  if (c2 >= 1 && c3 >= 2) { // 2 3 3
    ans = max(ans, solve(c1, c2-1, c3-2) + 1);
  }
  if (c3 >= 4) { // 3 3 3 3
    ans = max(ans, solve(c1, c2, c3-4) + 1);
  }
  return dp[c1][c2][c3] = ans;
}

int main() {
  freopen("input", "r", stdin);
  freopen("output", "w", stdout);

  VI ls;
  see(1, 4, ls);
  vector<VI> vs;
  for (set<VI>::iterator r = got.begin(); r!=got.end(); r++) vs.push_back(*r);
  int n = vs.size();
  int bad[50] = {};
  REP(i,0,n) {
    REP(j,0,n) {
      if (i == j) continue;
      if (super(vs[i], vs[j])) {
        bad[i] = 1;
      }
    }
  }
  REP(i,0,n) {
    if (bad[i]) continue;
    REP(j,0,vs[i].size()) cerr << vs[i][j] << " ";
    cerr << endl;
  }

  int cs;
  cin >> cs;
  FILL(dp, -1);
  REP(csn, 1, cs + 1) {
    printf("Case #%d: ", csn);
    //cerr << csn << endl;
    int N, P;
    cin >> N >> P;
    FILL(cnt, 0);
    REP(i,0,N) {
      scanf("%d", G+i);
      cnt[G[i] % P]++;
    }
    int ans = 0;
    if (P == 2) {
      ans = cnt[0] + (cnt[1]+1) / 2;
    } else if (P == 3) {
      int d = min(cnt[1], cnt[2]);
      int r = max(cnt[1], cnt[2]) - d;
      ans = cnt[0] + d + (r + 2) / 3;
    } else {
      ans = cnt[0] + solve(cnt[1], cnt[2], cnt[3]);
    }
    cout << ans << endl;
  }
  return 0;
}
