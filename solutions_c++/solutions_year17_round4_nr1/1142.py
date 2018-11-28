#include <bits/stdc++.h>

#define FOR(i, a, b) for (int i = (int)(a); i < (int)(b); ++i)
#define REP(i, n) FOR(i, 0, n)
#define TRACE(x) cerr << #x << " = " << x << endl
#define _ << " _ " <<

#define x first
#define y second

using namespace std;

typedef long long ll;

const int MAXN = 1010;

int n, p;
int a[MAXN];

int cnt[MAXN];

char dp[101][101][101][101][4];

char rec(int pos, int a, int b, int c, int d, int ost) {
  if (pos == n) return 0;
  if (a < 0 || b < 0 || c < 0 || d < 0) return -101;
  char &ret = dp[a][b][c][d][ost];
  if (ret != -1) return ret;
  ret = 0;
  if (ost == 0) ret = 1;
  ret += max(max(rec(pos+1, a-1, b, c, d, (ost+0)%4), rec(pos+1, a, b-1, c, d, (ost+1)%4)), 
             max(rec(pos+1, a, b, c-1, d, (ost+2)%4), rec(pos+1, a, b, c, d-1, (ost+3)%4)));
  return ret;
}

void solve() {
  scanf("%d%d", &n, &p);
  REP(i, 5) cnt[i] = 0;
  REP(i, n) {
    int x;
    scanf("%d", &x);
    cnt[x % p]++;
  }
  if (p == 2) {
    printf("%d\n", cnt[0] + (cnt[1]+1)/2);
  } else if (p == 3) {
    int mn = min(cnt[1], cnt[2]);
    int mx = max(cnt[1], cnt[2]);
    printf("%d\n", cnt[0] + mn + (mx-mn+2)/3);
  } else if (p == 4) {
    memset(dp, -1, sizeof dp);
    printf("%d\n", (int)rec(0, cnt[0], cnt[1], cnt[2], cnt[3], 0));    
  }
}

int main(void) {
  int tests;
  scanf("%d", &tests);
  for (int test = 1; test <= tests; ++test) {
    printf("Case #%d: ", test);
    solve();
  }
  return 0;
}

