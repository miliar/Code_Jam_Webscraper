#include <cstdio>
#include <cstdlib>
#include <cstring>
#include <iostream>
#include <algorithm>
typedef long long ll;
#define rep(i, a, b) for (int i = a; i <= b; ++ i) 
#define per(i, a, b) for (int i = a; i >= b; -- i)
const int S = 24 * 60, inf = 1000000007;
using namespace std; 

int n, m, A[S + 5], B[S + 5], f[S + 5][S + 5], bit[2][S + 5][S + 5];

void put(int a, int b, int x, int y) {
	if (!x) return ;
	for ( ; x <= S; x += x & (- x))
		bit[a][b][x] = min(bit[a][b][x], y) ;
}

int get(int a, int b, int x) {
	int ret = inf ;
	for ( ; x; x -= x & (- x))
		ret = min(ret, bit[a][b][x]) ;
	return ret ;
}

void solve() {
	int x, y ;
	rep(i, 0, S) A[i] = B[i] = 0; 
	scanf("%d%d", &n, &m) ;
	rep(i, 1, n) {
		scanf("%d%d", &x, &y) ;
		rep(j, x + 1, y) A[j] = 1;
	}
	rep(i, 1, m) {
		scanf("%d%d", &x, &y) ;
		rep(j, x + 1, y) B[j] = 1;
	}
	rep(i, 1, S) A[i] += A[i - 1], B[i] += B[i - 1] ;
	rep(i, 0, S) rep(j, 0, S / 2) f[i][j] = inf ;
	f[0][0] = 0;
	rep(i, 0, S) rep(j, 0, S) bit[0][i][j] = bit[1][i][j] = inf ;
	put(0, 0, S, 0), put(1, 0, S, 0) ;
	rep(i, 1, S) {
		int st = min(i, S / 2) ;
		int l = i ;
		per(j, i - 1, 0) if (A[j] == A[i]) l = j ;
		rep(j, 0, st)
			f[i][j] = min(f[i][j], get(0, i - j, S - max(l, i - j)) + 1);
		l = i ;
		per(j, i - 1, 0) if (B[j] == B[i]) l = j ;
		rep(j, 0, st)
			f[i][j] = min(f[i][j], get(1, j, S - l) + 1);
		rep(j, 0, st) 
			put(0, i - j, S - i, f[i][j]) ,
			put(1, j, S - i, f[i][j]) ;
		/*rep(j, 0, st) {
			per(k, i - 1, 0) if (i - k <= j && A[i] == A[k])
				f[i][j] = min(f[i][j], f[k][j - i + k] + 1) ; 
			else break ;
			per(k, i - 1, 0) if (B[i] == B[k])
				f[i][j] = min(f[i][j], f[k][j] + 1) ;
			else break ;
		} */
	}
	printf("%d\n", (f[S][S / 2] & 1) ? f[S][S / 2] - 1 : f[S][S / 2]) ;
}

int main() {
	freopen("a.in", "r", stdin) ;
	freopen("a.out", "w", stdout) ;
	int T ;
	scanf("%d", &T) ;
	rep(cas, 1, T) {
		printf("Case #%d: ", cas) ;
		solve() ;
	}
	return 0;
}