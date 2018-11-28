#include <cstdio>
#include <cstdlib>
#include <cstring>
#include <cmath>
#include <algorithm>
#include <stack>
#include <queue>
#include <vector>
#include <map>
#include <iostream>
#include <string>
using namespace std;
typedef long long LL;
typedef unsigned long long ULL;
typedef double DB;

const int MaxN = 1e3;
int n;
DB d;
struct Point {
	DB k, s;
}a[MaxN + 5];

bool cmp(Point x, Point y) {
	return x.k < y.k;
}

bool Check(DB x) {
	for(int i = 1; i <= n; i++)
		if((d - a[i].k) / a[i].s > (d / x)) return 0;
	return 1;
}

int main()
{
	freopen("A.in", "r", stdin);
	freopen("A.out", "w", stdout);
	int T, cas = 0;
	scanf("%d", &T);
	while(T--) {
		scanf("%lf%d", &d, &n);
		for(int i = 1; i <= n; i++)
			scanf("%lf%lf", &a[i].k, &a[i].s);
		sort(a + 1, a + n + 1, cmp);
		DB l = 0.00, r = (DB)(1LL << 60), ans = 0.00;
		for(int i = 1; i <= 100; i++) {
			double mid = (l + r) / 2.00;
			if(Check(mid)) ans = mid, l = mid;
			else r = mid;
		}
		printf("Case #%d: ", ++cas);
		printf("%.9lf\n", ans);
	}
	fclose(stdin);
	fclose(stdout);
}
