#include <cmath>
#include <cstdio>
#include <cstdlib>
#include <cstring>
#include <iostream>
#include <algorithm>
typedef long long ll ;
#define rep(i, a, b) for (int i = a; i <= b; ++ i) 
using namespace std; 

int T, n, k ;
struct poi {
	double r, h; 
} a[1005] ;

bool cmpr(poi a, poi b) {
	return a.r < b.r ;
}

bool cmph(poi a, poi b) {
	return a.h > b.h ;
}

double calc(double x, double y) {
	double ret = M_PI * x * x ;
	return ret + y ;
}

int main() {
	freopen("a.in", "r", stdin) ;
	freopen("a.out", "w", stdout) ;
	scanf("%d", &T) ;
	rep(cas, 1, T) {
		scanf("%d%d", &n, &k) ;
		rep(i, 1, n) scanf("%lf%lf", &a[i].r, &a[i].h) ;
		rep(i, 1, n) a[i].h *= M_PI * a[i].r * 2.0 ;
		sort(a + 1, a + n + 1, cmpr) ;
		double ans = 0 ;
		rep(i, k, n) {
			double x = a[i].r, y = a[i].h ;
			sort(a + 1, a + i, cmph) ;
			rep(j, 1, k - 1) y += a[j].h ;
			ans = max(ans, calc(x, y)) ;
		}
		printf("Case #%d: %.9lf\n", cas, ans) ;
	} 
	return 0 ;
}