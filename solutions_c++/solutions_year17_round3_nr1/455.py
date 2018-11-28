#include <bits/stdc++.h>

#ifdef PIT
#define debug(...) fprintf(stderr, __VA_ARGS__)
#else
#define debug(...)
#endif

#define rep(i, j, k) for(int i = (int) j; i < (int) k; ++i)
#define sz(x) ((int) (x).size())
#define ll long long
#define mp make_pair
#define pii pair<int, int >
#define fi first
#define se second
#define pb push_back
#define inf 0x3f3f3f3f
#define INF 0x3f3f3f3f3f3f3f3f
#define zero(x) memset((x), (0), sizeof (x))
#define zerox(x, y) memset((x), (y), sizeof (x))

using namespace std;
const int N = 1010;
const double eps = 1e-12;
const double pi = 3.14159265358979323846264338327950;

inline int sig(double x) {return (x>eps) - (x<-eps);}

ll dp[N][N];

int n, k;

struct P {
  ll s, a;

  bool operator<(const P rhs) const {
    if (s == rhs.s)
      return a > rhs.a;
    else
      return s > rhs.s;
  }
} p[N];



int main(int argc, char const *argv[])
{
#ifdef PIT
freopen("A-large.in", "r", stdin);
freopen("A-large.out", "w", stdout);
int _time_zlp = clock();
#endif // PIT

    int ic = 1, T;
    for(scanf("%d", &T); ic <= T; ++ic){
        printf("Case #%d: ", ic);
		//printf("Case #%d:\n", ic);
        scanf("%d %d", &n, &k);
        ll r, h;
        rep(i, 0, n) {
        	scanf("%I64d %I64d", &r, &h);
        	p[i].s = r * r;
            p[i].a = r * h * 2;
        }
        sort(p, p+n);
        zero(dp);
        dp[0][0] = p[0].s + p[0].a;
        rep(i, 1, n) {
          for(int j = 0; j < min(i+1, k);  ++j) {
            if (j == 0)
              dp[i][0] = max(dp[i - 1][0], p[i].s + p[i].a);
            else
              dp[i][j] = max(dp[i - 1][j], dp[i - 1][j - 1] + p[i].a);
          }
        }
    //printf("Case #%lld: %.10f\n", tcase, dp[k - 1][n - 1] * pi);
        double ans = pi * dp[n-1][k-1];
        
        printf("%.12f\n", ans);
    }
#ifdef PIT
debug("Time: %f s\n", double(clock()-_time_zlp)/CLOCKS_PER_SEC);
#endif //PIT
    return 0;
}