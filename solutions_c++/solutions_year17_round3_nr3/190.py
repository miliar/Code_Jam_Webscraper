#include <cstdio>
#include <cstdlib>
#include <cstring>
#include <iostream>
#include <algorithm>
typedef long long ll;
#define rep(i, a, b) for (int i = a; i <= b; ++ i)
using namespace std;
int T, n;
double m, a[100];
int main() {
	freopen("a.in", "r", stdin) ;
	freopen("a.out", "w", stdout) ;
	scanf("%d", &T) ;
	rep(cas, 1, T) {
		scanf("%d%d", &n, &n) ;
		scanf("%lf", &m) ;
		rep(i, 1, n) scanf("%lf", &a[i]) ;
		++ n, a[n] = 1 ;
		sort(a + 1, a + n + 1) ;
		rep(i, 2, n) if (a[i - 1] != a[i]) {
			double ret = (i - 1) * (a[i] - a[i - 1]) ; 
			if (ret <= m) {
				rep(j, 1, i - 1) a[j] = a[i] ;
				m -= ret ; 
				continue ;
			}
			rep(j, 1, i - 1) a[j] += m / (i - 1) ;
			break ;
		}
		double ans = 1;
		rep(i, 1, n) ans *= a[i] ;
		printf("Case #%d: %.6lf\n", cas, ans) ;
	} 
	return 0 ;
}