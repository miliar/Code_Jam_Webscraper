#include<iostream>
#include<stdio.h>
#include<string.h>
#include<math.h>
#include<algorithm>
using namespace std;
double eps = 1e-9;
double p[55];
int n;
double f(double x) {
	double ans=0;
	for (int i = 0; i < n; i++) {
		if (p[i] + eps < x)
			ans += x - p[i];
	}
	return ans;
}
int main() {
	//freopen("in.txt", "r", stdin);
	//freopen("out.txt", "w", stdout);
	int t;
	scanf("%d", &t);
	int k;
	double u;
	for (int cas = 1; cas <= t; cas++) {
		printf("Case #%d: ", cas);
		scanf("%d%d", &n, &k);
		scanf("%lf", &u);
		for (int i = 0; i < n; i++) {
			scanf("%lf", &p[i]);
		}
		double mid, l = 0, r = 1;
		for (int i = 0; i <= 50000; i++) {
			mid = (l + r) / 2.0;
			//printf("%.5lf %.5lf\n",mid,f(mid));
			if (f(mid) + eps < u)
				l = mid+eps;
			else
				r = mid-eps;
		}
		double ans=1;
		for(int i=0;i<n;i++)
		{
			if(p[i]+eps<mid)ans*=mid;
			else ans*=p[i];
		}
		printf("%.9lf\n", ans);
	}
	return 0;
}
