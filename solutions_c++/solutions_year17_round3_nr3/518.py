//writted by dnvtmf
#include <bits/stdc++.h>
#define INF 1000000007
#define FI first
#define SE second
#define PB push_back
#define VI vector<int>
#define MP make_pair
#define FOR(x, st, ed) for(auto x = (st); x < (ed); ++x)
#define FORE(x, st, ed) for(auto x = (st); x <= (ed); ++x)
#define CLR(arr, val) memset(arr, val, sizeof(arr))
#define INFO(tag, st, ed, x) printf("%s: ", tag); \
	FOR(_i, st, ed) cout << x[_i] << ' '; puts("");
using namespace std;
typedef long long LL;
typedef pair <int, int> PII;
const int NUM = 100010;
int n, m;
double u, p[55];
double dp[55];
double calc(double a[], int k) {
	for(int i = 0; i < 55; ++i)
		dp[i] = 0;
	dp[0] = 1.;
	for(int i = 0; i < n; ++i) {
		if(i == k) continue;
		for(int j = n; j > 0; --j) {
			dp[j] = dp[j] * (1. - a[i]) + dp[j - 1] * a[i];
		}
		dp[0] *= (1. - a[i]);
	}
	return dp[m - 1];
}
double delta[55];
int id[55];
bool cmp(int i, int j) {
	return delta[i] > delta[j];
}
double eps = 1e-9;
inline int sign(double x) {return x < -eps ? -1 : x > eps ? 1 : 0;}
int main() {
#ifdef ACM_TEST
	freopen("in.txt", "r", stdin);
#endif
	int T; scanf("%d", &T);
	for(int cas = 1; cas <= T; ++cas) {
		scanf("%d%d", &n, &m);
		scanf("%lf", &u);
		for(int i = 0; i < n; ++i) {
			scanf("%lf", &p[i]);
		}
		sort(p, p + n);
		for(int i = 0, j; i < n; i = j) {
			for(j = i; j < n && sign(p[i] - p[j]) == 0; ++j);
			if(i == 0) continue;
			if(sign(u - (p[i] - p[i - 1]) * i) >= 0) {
				u -= (p[i] - p[i - 1]) * i;
				for(int k = 0; k < i; ++k)
					p[k] = p[i];
			}
			else {
				u /= i;
				for(int k = 0; k < i; ++k)
					p[k] += u;
				u = 0;
				break;
			}
		}
		if(sign(u) > 0) {
			u /= n;
			for(int i = 0; i < n; ++i)
				p[i] += u;
		}
		double ans = 0.0;
		calc(p, -1);
		for(int i = m; i <= n; ++i)
			ans += dp[i];
		printf("Case #%d: %f\n", cas, ans);
	}
	return 0;
}
