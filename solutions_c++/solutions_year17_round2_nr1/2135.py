#include <bits/stdc++.h>
using namespace std;

int getint() {
	char c = ' ';
	for(; c < '0' || c > '9'; c = getchar());
	int ret = 0;
	for(; c >= '0' && c <= '9'; c = getchar()) ret = ret * 10 + c - '0';
	return ret;
}

#define INF (1000000001)

const int N = 10100;
int n, d, k[N], s[N];

void solve() {
	double ans = 0.;
	for(int i = 0; i < n; ++i) ans = max(ans, (d - k[i]) * 1. / s[i]);
	printf("%.6lf\n", d / ans);
}

int main() {
	int testcases = getint();
	for(int testindex = 1; testindex <= testcases; ++testindex) {
		printf("Case #%d: ", testindex);
		d = getint();
		n = getint();
		for(int i = 0; i < n; ++i) k[i] = getint(), s[i] = getint();
		solve();
	}
	return 0;
}

