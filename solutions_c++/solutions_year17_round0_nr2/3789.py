#include <iostream>
#include <stdio.h>

#define LL long long

using namespace std;

const int MXN = 25;

int T, a[MXN], r[MXN];
LL n;
inline LL getnum() {
	LL tot = 0;
	for(int i = 1; i <= 20; i++) {
		tot = tot * 10 + r[i]; //
	}
	return tot;
}
inline void solve() {
	scanf("%d", &T);
	for(int ii = 1; ii <= T; ii++) {
		scanf("%lld", &n);
		LL tmp = n;
		for(int i = 20; i >= 1; i--) {
			a[i] = tmp % 10;
			tmp /= 10;
		}
		LL maxn = 0LL;
		//for(int i = 0; i <= 19; i++) printf("%d ", a[i]); printf("\n");
		for(int i = 1; i <= 20; i++) r[i] = 0; ///
		bool ok = 0;
		for(int i = 1; i <= 20; i++) {
			if(a[i] > r[i - 1]) {
				r[i] = a[i] - 1;
				for(int j = i + 1; j <= 20; j++) r[j] = 9; //
				//printf("%lld\n", getnum());
				maxn = max(maxn, getnum());
			}
			if(a[i] >= r[i - 1]) {
				r[i] = a[i];
			}
			else {ok = 1; break;} ////
		}
		if(!ok) maxn = max(maxn, n); //
		printf("Case #%d: %lld\n", ii, maxn);
	}
}
int main() {
	freopen("B.in", "r", stdin);
	freopen("B.out", "w", stdout);
	solve();
	return 0;
}
