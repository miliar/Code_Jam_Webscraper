#include<cstdio>
#include<cstring>
#include<algorithm>
#include<iostream>
using namespace std;

int T, n, k;
double a[1100];
double x;
int main() {
	freopen("in.txt","r",stdin);
	freopen("out.txt","w",stdout);
	int cas = 0;
	scanf("%d", &T);
	while (T--) {
		scanf("%d%d", &n, &k);
		scanf("%lf", &x);
		for (int i = 1; i <= n; i++) scanf("%lf", &a[i]);	
		double l = 0, r = 1;
		for (int t = 0; t <= 100; t++) {
			double mid = (l+r)/2;
			double tmp = 0;
			for (int i = 1; i <= n; i++) if (a[i] < mid) tmp += mid-a[i];	
			if (tmp < x) l = mid;
			else r = mid;
		}
		double res = 1;
		for (int i = 1; i <= n; i++) if (a[i] < l) res *= l;
		else res *= a[i];
		printf("Case #%d: ", ++cas);
		printf("%.8f\n", res);
	}
}

