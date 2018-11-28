#include <cstring>
#include <cstdio>
#include <algorithm>

using namespace std;

void solve(int tim) {
	printf("Case #%d: ", tim);
	int d, n, k, s;
	double ans = 0;
	scanf("%d%d", &d, &n);
	for (int i = 1; i <= n; i ++) {
		scanf("%d%d", &k, &s);
		ans = max(ans, 1.0 * (d - k) / s);
	}
	printf("%.8lf\n", d / ans);
}

int main() {
	//freopen("data.in", "r", stdin), freopen("data.out", "w", stdout);
	
	int t;
	scanf("%d", &t);
	for (int i = 1; i <= t; i ++) solve(i);
}