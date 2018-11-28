#include <bits/stdc++.h>
using namespace std;
#define ll long long
#define f(i, x, n) for(int i = x; i < (int)(n); ++i)

int n, k;
double dp[51], u, x[50];

bool ok(double m){
	double t = u;
	f(i, 0, k)t -= max(0.0, m - x[i]);
	return t >= 0.0;
}

int main(){
	freopen("main.in", "r", stdin);
	freopen("main.out", "w", stdout);
	int t;
	scanf("%d", &t);
	f(tc, 1, t + 1){
		printf("Case #%d: ", tc);
		scanf("%d%d%lf", &n, &k, &u);
		f(i, 1, n + 1)dp[i] = 0.0;
		dp[0] = 1.0;
		f(i, 0, n)scanf("%lf", x + i);
		sort(x, x + n);
		reverse(x, x + n);
		double l = 0.0, r = 1.0;
		f(i, 0, 100){
			double m = (l + r) / 2.0;
			if (ok(m))l = m;
			else r = m;
		}
		f(i, 0, k)x[i] = max(x[i], l);
		f(i, 0, n)for (int j = n - 1; j >= 0; --j)dp[j + 1] += dp[j] * x[i], dp[j] *= (1.0 - x[i]);
		double an = 0.0;
		f(i, k, n + 1)an += dp[i];
		printf("%.7lf\n", an);
	}
}