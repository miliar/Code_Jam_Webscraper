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
const double eps = 1e-8;
const int N = 55;

inline int sig(double x) {return (x>eps) - (x<-eps);}

int n, k;
double u;
double p[N];


int main()
{
#ifdef PIT
freopen("C-small-1-attempt0.in", "r", stdin);
freopen("C-small-1-attempt0.out", "w", stdout);
int _time_zlp = clock();
#endif // PIT

    int ic = 1, T;
    for(scanf("%d", &T); ic <= T; ++ic){
        printf("Case #%d: ", ic);
		//printf("Case #%d:\n", ic);
		scanf("%d %d", &n, &k);
		scanf("%lf", &u);
		double pro = 0.0;
		rep(i, 0, n) scanf("%lf", p+i), pro += p[i];
		pro += u;
		if(sig(pro / n - 1.0) >= 0) {
			printf("%f\n", 1.0);
			continue;
		}
		double l = 0.0, r = 1.0, m;
		rep(z, 0, 1000) {
			m = (l + r) * 0.5;
			double x = 0.0;
			rep(i, 0, n) x += max(0.0, m-p[i]);
//if(z < 30)	printf("%d %.6f %.6f %.6f %.6f %.6f\n", z, l, r, m, x, u);
			if(sig(x-u) < 0) l = m;
			else r = m;
		}
//printf("r == %.10f\n", r);
		double pb = 1.0;
		rep(i, 0, n) {
			pb *= max(r, p[i]);
		}
		printf("%.10f\n", pb);
        
    }
#ifdef PIT
debug("Time: %f s\n", double(clock()-_time_zlp)/CLOCKS_PER_SEC);
#endif //PIT
    return 0;
}