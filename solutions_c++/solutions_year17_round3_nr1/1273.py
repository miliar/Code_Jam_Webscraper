#include <cstdio>
#include <vector>
#include <string.h>
#include <math.h>
#define feq(x,y) (fabs((x)-(y))<eps)
#define flt(x,y) ((x)<(y)-eps)
#define fgt(x,y) ((x)>(y)+eps)
#define fle(x,y) ((x)<(y)+eps)
#define fge(x,y) ((x)>(y)-eps)
const double inf = 1e40, eps = 1e-9;

using namespace std;

double mymax(long double a, long double b, long double c, long double d) {
	return max(a, max(b, max(c, d)));
}

long double solve() {
	int n, k;
	scanf("%d%d", &n, &k);
	vector< pair<long double, long double> > a; a.clear();
	for (int i = 0; i < n; i++) {
		int r, h;
		scanf("%d%d", &r, &h);
		a.push_back(make_pair(r, h));
	}

	sort(a.begin(), a.end());

	int l;
	long double dp[2][1010]; memset(dp, 0, sizeof(dp));
	for (int i = n - 1; i >= 0; i--) {
		int c = i % 2;
		int p = (i + 1) % 2;
		l = c;
		for (int j = 1; j <= k; j++) {
			dp[c][j] = mymax(dp[c][j - 1], dp[p][j], dp[p][j - 1] + 2 * a[i].first * a[i].second, a[i].first * a[i].first + 2 * a[i].first * a[i].second);
		}
	}

	return dp[l][k] * 3.14159265358979323846264338327950288419716939937510;
}

int main() {
	int T, ca = 0;
	scanf("%d", &T);
	while (T--) {
		long double ans = solve();
		printf("Case #%d: %.9Lf\n", ++ca, ans);
	}
	return 0;
}
