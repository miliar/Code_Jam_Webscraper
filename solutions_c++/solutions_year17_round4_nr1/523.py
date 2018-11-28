#include <cstdio>
#include <cstdlib>
#include <cstring>
#include <iostream>
#include <algorithm>
typedef long long ll ;
#define rep(i, a, b) for (int i = a; i <= b; ++ i)
using namespace std ;

int f[105][105][105], h[10];

int main() {
	freopen("a.in", "r", stdin) ;
	freopen("a.out", "w", stdout) ;
	int T, n, p ;
	scanf("%d", &T) ;
	f[0][0][0] = 0 ;
	rep(i, 0, 100) rep(j, 0, 100) rep(k, 0, 100) {
		f[i][j][k] = 0 ;
		if (i) f[i][j][k] = max(f[i][j][k], f[i - 1][j][k]) ;
		if (j) f[i][j][k] = max(f[i][j][k], f[i][j - 1][k]) ;
		if (k) f[i][j][k] = max(f[i][j][k], f[i][j][k - 1]) ;
		// 1 3
		if (i && k) f[i][j][k] = max(f[i][j][k], f[i - 1][j][k - 1] + 1) ;
		// 2 2
		if (j > 1) f[i][j][k] = max(f[i][j][k], f[i][j - 2][k] + 1) ;
		// 1 1 2  
		if (i > 1 && j) f[i][j][k] = max(f[i][j][k], f[i - 2][j - 1][k] + 1) ;
		// 2 3 3
		if (j && k > 1) f[i][j][k] = max(f[i][j][k], f[i][j - 1][k - 2] + 1) ;
		// 1 1 1 1
		if (i > 3) f[i][j][k] = max(f[i][j][k], f[i - 4][j][k] + 1) ;
		if (k > 3) f[i][j][k] = max(f[i][j][k], f[i][j][k - 4] + 1) ;
	}
	rep(cas, 1, T) {
		scanf("%d%d", &n, &p) ;
		rep(i, 0, p - 1) h[i] = 0 ;
		int sum = 0, x;
		rep(i, 1, n) scanf("%d", &x), h[x % p] ++, sum = (sum + x) % p;
		int ret = sum ? 1 : 0 ;
		if (p == 2) ret += h[0] + h[1] / 2; 
		if (p == 3) {
			ret += h[0] ;
			int d = min(h[1], h[2]) ;
			ret += d ; h[1] -= d, h[2] -= d ;
			ret += h[1] / 3 + h[2] / 3 ;
		}
		if (p == 4) {
			ret += h[0] ;
			ret += f[h[1]][h[2]][h[3]] ;
		}
		printf("Case #%d: %d\n", cas, ret) ;
	}
	return 0 ; 
}