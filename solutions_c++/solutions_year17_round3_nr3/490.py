#define _USE_MATH_DEFINES
#include<bits/stdc++.h>
#define MOD 1000000007
#define INF 0x3f3f3f3f
#define INFL 0x3f3f3f3f3f3f3f3f
#define EPS (1e-12)
#define rep(i,n)for(int i=0;i<(n);i++)
using namespace std;
typedef long long ll;
typedef pair<int, int>P;

double p[50];
int main() {
	int T; scanf("%d", &T);
	for (int cnt = 1; cnt <= T; cnt++) {
		int n, k; scanf("%d%d", &n, &k);
		double u; scanf("%lf", &u);
		rep(i, n)scanf("%lf", &p[i]);
		double l = 0, r = 1;
		rep(i, 500) {
			double t = (l + r) / 2;
			double sum = 0;
			rep(j, n) {
				if (p[j] < t)sum += t - p[j];
			}
			if (sum <= u)l = t;
			else r = t;
		}
		double ans = 1;
		rep(i, n) {
			if (p[i] <= l)ans *= l;
			else ans *= p[i];
		}
		printf("Case #%d: %.12lf\n", cnt, ans);
	}
}