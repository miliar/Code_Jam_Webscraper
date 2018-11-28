#include <iostream>
#include <algorithm>
#include <cstdlib>
#include <cstdio>
#include <cstring>
#include <ctime>
#include <cmath>
#include <map>
#include <set>
#include <vector>
#include <queue>
#define LL long long
using namespace std;
#define rep(i, n) for (int i = 0; i < n; i++)
#define kep(i, n) for (int i = 1; i <=n; i++)
#define N 1111

int T, n, d, k, s;
double ans;

void solve() {
	scanf("%d%d", &d, &n);
	rep(i, n) {
		scanf("%d%d", &k, &s);
		if (!i) ans = k * (double)s / (double)(d - k) + (double) s;
		else ans = min(ans, k * (double)s / (double)(d - k) + (double) s);
	}
	printf("%.7f\n", ans);
}

int main() {
	freopen("A-large.in", "r", stdin);
	freopen("A-large.out", "w", stdout);
	scanf("%d", &T);
	kep(_, T) {
		printf("Case #%d: ", _);
		solve();
	}
	return 0;
}
