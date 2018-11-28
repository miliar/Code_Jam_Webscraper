#include<iostream>
#include<stdio.h>
#include<string.h>
#include<math.h>
#include<algorithm>
#include<stdlib.h>
#include<queue>
#include<stack>
#include<map>
#include<set>
#include<vector>
const double PI = acos(-1.0);
const double e = exp(1.0);
#define ll __int64
template<class T> T gcd(T a, T b) {
	return b ? gcd(b, a % b) : a;
}
template<class T> T lcm(T a, T b) {
	return a / gcd(a, b) * b;
}
#define inf 0x7fffffff
using namespace std;
/*

 */
double a[55];
int n;
double f(double x) {
	double ans = 0;
	for (int i = 0; i < n; i++) {
		if (a[i] < x)
			ans += x - a[i];
	}
	return ans;
}
int main() {
	freopen("1.txt", "r", stdin);
	freopen("2.txt", "w", stdout);
	int t;
	scanf("%d", &t);
	int k;
	double u;
	for (int cas = 1; cas <= t; cas++) {
		printf("Case #%d: ", cas);
		scanf("%d%d", &n, &k);
		scanf("%lf", &u);
		for (int i = 0; i < n; i++) {
			scanf("%lf", &a[i]);
		}
		double mid, l = 0, r = 1;
		for (int i = 0; i <= 100; i++) {
			mid = (l + r) / 2.0;

			if (f(mid) < u)
				l = mid;
			else
				r = mid;
		}
		double ans = 1;
		for (int i = 0; i < n; i++) {
			if (a[i] < mid)
				ans *= mid;
			else
				ans *= a[i];
		}
		printf("%.10f\n", ans);
	}
	return 0;
}
