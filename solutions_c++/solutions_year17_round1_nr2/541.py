#include <bits/stdc++.h>
using namespace std;
#define FOR(i, n) for(int i = 1; i <= n; i++)
#define REP(i, n) for(int i = 0; i < n; i++)
#define MP make_pair
#define FI first
#define SE second
#define VI vector<int>
#define CLR(x) memset(x, 0, sizeof(x))
#define SZ(x) (x.size())
#ifdef QWERTIER
#define err(x) cerr<<x<<endl;
#else
#define err(x)
#endif
typedef long long LL;


#define N 60
int ind[N][N];
int need[N], cur[N];
int n, m;

bool check(int num, int ind, int j) {
  return num * need[j] * 9 <= ind * 10 && num * need[j] * 11 >= ind * 10;
}
bool check2(int num) {
  vector<pair<int, int> > v;
  FOR (j, n-1) {
    bool f2 = false;
    REP (k, m) {
      if (check(num, ind[j][k], j)) {
        v.push_back(make_pair(j, k));
        f2 = true;
        break;
      }
    }
    if (!f2)
      return false;
  }
  for (auto p : v) {
    ind[p.first][p.second] = 0;
  }
  return true;
}
int main() {
#ifdef QWERTIER
  //freopen("in.txt", "r", stdin);
  freopen("B-large.in", "r", stdin);
  freopen("B-large.out", "w", stdout);
#endif
  int T;
  scanf("%d", &T);
  FOR (kase, T) {
    printf("Case #%d: ", kase);
    scanf("%d%d", &n, &m);
    REP (i, n)
      scanf("%d", &need[i]);
    REP (i, n) {
      REP (j, m) {
        scanf("%d", &ind[i][j]);
      }
      sort(ind[i], ind[i]+m);
    }
    memset(cur, 0, sizeof(cur));
    int ans = 0;
    REP (i, m) {
      //int l = (ind[0][i] / need[0]), r = ((ind[0][i] + need[0] - 1) / need[0]);
      int l =  (10 * ind[0][i] + 11*need[0]-1) /(11*need[0]),
        r = (10*ind[0][i])/(9*need[0]);
      //printf("%d %d\n", l, r);
      if (l == r && r == 0)
        continue;
      for (int j = l; j <= r; j++) {
        if (need[0] * j * 9 <= ind[0][i] * 10 && need[0] * j * 11 >= ind[0][i] * 10) {
          //printf("j:%d\n", j);
          if (check2(j)) {
            //puts("ok");
            ans++;
            ind[0][i] = 0;
            break;
          }
        }
      }
    }
    printf("%d\n", ans);
  }
  return 0;
}
