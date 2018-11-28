#include <iostream>
#include <cstdio>
#include <cstring>
#include <cstdlib>
#include <algorithm>
using namespace std;
int n, p;
int r[55];
int q[55][55];
int L[55][55], R[55][55];
int c[55],now[55];
int main() {
	freopen("B-large.in", "r", stdin);
	freopen("data.out", "w", stdout);
	int T;
	cin >> T;
	for(int ii = 1; ii <= T; ++ii) {
		scanf("%d%d", &n, &p);
		for(int i = 1; i <= n; ++i)
			scanf("%d", r + i);
		for(int i = 1; i <= n; ++i)
			for(int j = 1; j <= p; ++j)
				scanf("%d", q[i]+j);
		for(int i = 1; i <= n; ++i)
			sort(q[i] + 1, q[i] + p +1);
		for(int i = 1; i <= n; ++i)
			for(int j = 1; j <= p; ++j) {
				R[i][j] = 10 * q[i][j] / (9 * r[i]);
				L[i][j] = 10 * q[i][j] / (11 * r[i]) + (10 * q[i][j] % (11 * r[i]) != 0);
			}
		memset(now, 0, sizeof now);
		int ans = 0;
		for(int i = 1; i <= 1100000; ++i) {
			bool flag = true;
			while(true) {
				for(int j = 1; j <= n; ++j) {
					c[j] = 0;
					for(int k = now[j] + 1; k <= p; ++k)
						if(L[j][k] <= i && R[j][k] >= i) {
							c[j] = k;
							break;
						}
					if(!c[j]) {flag = false; break;}
				}
				if(flag) {
					ans++;
					for(int j = 1; j <= n; ++j)
						now[j] = c[j];
				}
				else break;
			}
		}
		printf("Case #%d: %d\n", ii, ans);
	}
	return 0;
}
