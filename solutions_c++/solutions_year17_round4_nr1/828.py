#include <bits/stdc++.h>
using namespace std;
#define REP(i, n) for (int i = 0; i < (int) (n); i++)
#define pb push_back
#define mp make_pair
#define fi first
#define se second
#define maximize(a, b) ((a)<(b)?(a)=(b),1:0)
#define minimize(a, b) ((a)>(b)?(a)=(b),1:0)

void input();
void solve(int cs);

int main(int argc, char* argv[]) {
  if (argc == 1) freopen("input.txt", "r", stdin);
  int tc;
  cin >> tc;
  int l = 1, r = tc;
  if (argc > 1) {
    freopen(argv[2], "w", stdout);
    int n = atoi(argv[1]), i = atoi(argv[2]);
    l = tc / n * i + 1;
    r = i+1<n ? tc/n*(i+1) : tc;
  }
  for (int cs = 1; cs <= tc; cs++) {
    input();
    if (cs >= l && cs <= r) solve(cs);
  }
  return 0;
}

const int N = 102;
int n, p;
array<array<array<array<int, 4>, N>, N>, N> f;
array<int, N> r;

void input() {
  cin >> n >> p;
  r.fill(0);
  REP(i, n) {
    int a; cin >> a;
    r[a%p]++;
  }
}

void solve(int cs) {
  cout << "Case #" << cs << ": ";
  int ans = r[0];
  REP(i, N) REP(j, N) REP(k, N) REP(l, 4) f[i][j][k][l] = -(1<<30);
  f[0][0][0][0] = 0;
  REP(i, r[1]+1) REP(j, r[2]+1) REP(k, r[3]+1) REP(t, p) if (f[i][j][k][t] >= 0) {
    maximize(f[i+1][j][k][(t+1)%p], f[i][j][k][t] + (t==0));
    maximize(f[i][j+1][k][(t+2)%p], f[i][j][k][t] + (t==0));
    maximize(f[i][j][k+1][(t+3)%p], f[i][j][k][t] + (t==0));
  }
  ans += f[r[1]][r[2]][r[3]][(r[1]*1 + r[2]*2 + r[3]*3)%p];
  cout << ans << endl;
}

