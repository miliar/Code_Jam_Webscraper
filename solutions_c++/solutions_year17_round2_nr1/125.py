#include<iostream>
#include<cstdio>
#include<cstring>
#include<algorithm>
using namespace std;
int T, n, m;

int main()  {
	freopen("A-large.in", "r", stdin);
	freopen("A-large.out", "w", stdout);
	cin >> T;
	for (int C = 1; C <= T; C++) {
		cin >> m >> n;
		double ans = 1e100;
		for (int i = 1; i <= n; i++) {
			int k, s;
			scanf("%d%d", &k, &s);
			ans = min(ans, m / ((m - k)*1.0 / s));
		}
		printf("Case #%d: %.10lf\n", C, ans);
	}
}