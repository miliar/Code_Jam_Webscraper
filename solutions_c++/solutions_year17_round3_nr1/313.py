#include<iostream>
#include<stdio.h>
#include<string.h>
#include<math.h>
#include<algorithm>
const double PI = acos(-1.0);
using namespace std;
struct node {
	double h, r;
} f[1111];
bool cmp1(node a, node b) {
	return a.r > b.r;
}
bool cmp2(node a, node b) {
	return a.h * a.r > b.h * b.r;
}
int main() {
	//freopen("in.txt","r",stdin);
	//freopen("out.txt","w",stdout);
	int t;
	scanf("%d", &t);
	int n, k;
	for (int cas = 1; cas <= t; cas++) {
		printf("Case #%d: ", cas);
		scanf("%d%d", &n, &k);
		for (int i = 1; i <= n; i++) {
			scanf("%lf%lf", &f[i].r, &f[i].h);
		}
		double ans = 0;
		for (int i = 1; i <= n - k + 1; i++) {
			sort(f + 1, f + n + 1, cmp1);
			double cnt = 0;
			cnt += PI * f[i].r * f[i].r;
			sort(f + i + 1, f + n + 1, cmp2);
			for (int j = i; j <= i + k - 1; j++)
				cnt += 2 * PI * f[j].r * f[j].h;
			ans = max(ans, cnt);
		}
		printf("%.10f\n", ans);
	}
	return 0;
}
