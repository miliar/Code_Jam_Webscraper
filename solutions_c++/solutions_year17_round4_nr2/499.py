#include <cstdio>
#include <cstdlib>
#include <cstring>
#include <iostream>
#include <algorithm>
typedef long long ll ;
#define rep(i, a, b) for (int i = a; i <= b; ++ i)
const int N = 100005 ;
using namespace std ;

int T, n, c, m, a[N], sum[N];

int main() {
	freopen("a.in", "r", stdin) ;
	freopen("a.out", "w", stdout) ;
	scanf("%d", &T) ;
	rep(cas, 1, T) {
		scanf("%d%d%d", &n, &c, &m) ;
		memset(a, 0, sizeof(a)) ;
		memset(sum ,0, sizeof(sum)) ;
		int x, y;
		rep(i, 1, m) scanf("%d%d", &y, &x) , ++ a[x], ++ sum[y] ;
		int ans1 = 0, ans2 = 0 ;
		rep(i, 1, c) ans1 = max(ans1, a[i]) ;
		rep(i, 1, n) {
			sum[i] += sum[i - 1] ;
			ans1 = max(ans1, (sum[i] - 1) / i + 1) ;
		}
		rep(i, 1, n) ans2 += max(sum[i] - sum[i - 1] - ans1, 0) ;
		printf("Case #%d: %d %d\n", cas, ans1, ans2) ;
	}
	return 0 ;
}