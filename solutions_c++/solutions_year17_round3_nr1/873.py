#include <bits/stdc++.h>

#define sz(z) (int)z.size()
#define fo(i,a,b) for (auto (i) = (a); (i) < (b); (i)++)
#define mp make_pair
#define pb push_back

using namespace std;

#define DEBUG

#ifdef DEBUG
#define D(x...) printf(x)
#else
#define D(x...) 
#endif

typedef long long ll;
typedef pair<int,int> ii;

struct pk {
	ll r, h;
	bool operator < (const pk &other) const {
		return r < other.r;
	}
};

#define PI 3.141592653589793238462643383279 

// index, taken
long double dp[1234][1234];
long double bt[1234];

int main() {
	int t;
	scanf("%d\n", &t);
	for (int _ = 1; _ <= t; _++) {
		printf("Case #%d: ", _);
		int n, K;
		scanf("%d%d",&n,&K);
		vector <pk> v;
		fo(i,0,n) {
			int a, b;
			scanf("%d %d", &a, &b);
			v.pb({a, b});
		}
		sort(v.begin(), v.end());
		long double ans = 0;
		fo(i,0,1234) fo(j,0,1234) dp[i][j] = 0, bt[i] = 0;
		dp[1][0] = PI*2*v[0].r*v[0].h;
		fo(i,1,K+1) {
			fo(j,0,n) bt[j] = 0;
			fo(j,0,n) {
				if (j) bt[j] = bt[j-1];
				if (dp[i-1][j] > bt[j]) {
					bt[j] = dp[i-1][j];
				}
			}
			dp[i][0] = PI*2*v[0].r*v[0].h;
			fo(j,1,n) {
				if (j) {
					dp[i][j] = bt[j-1] + PI*2*v[j].r*v[j].h;
				}
			}
		}
		fo(i,0,n) {
			ans = max(ans, dp[K][i] + PI*v[i].r*v[i].r);
		}
		printf("%.12Lf\n", ans);
	}
	
	return 0;
}
