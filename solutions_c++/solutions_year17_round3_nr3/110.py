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


#define eps 1e-8
#define N 100
double a[N];
double tot;
int n, k;
bool all1() {
  FOR (i, n)
    if (fabs(a[i] - 1) > eps)
      return false;
  return true;
}
int main() {
#ifdef QWERTIER
  freopen("C-small-1-attempt0.in", "r", stdin);
  freopen("C-small-1-attempt0.out", "w", stdout);
#endif
  int T;
  scanf("%d", &T);
  FOR (kase, T) {
    scanf("%d%d", &n, &k);
    scanf("%lf", &tot);
    FOR (i, n) {
      scanf("%lf", &a[i]);
    }
    sort(a+1, a+n+1);
    int lst = 1;
    for (int i = 1; i <= n; i++) {
      double bound;
      if (i + 1 > n)
        bound = 1;
      else
        bound = a[i+1];
      double dx = min(bound-a[i], tot/(i-lst+1));
      for (int j = lst; j <= i; j++)
        a[j] += dx;
      tot -= dx * (i-lst+1);
      if (fabs(a[i] - a[i+1]) > eps)
        lst = i + 1;
    }
    double ans = 1;
    FOR (i, n) {
      ans *= a[i];
    }
    printf("Case #%d: %.10f\n", kase, ans);
  }
  return 0;
}
