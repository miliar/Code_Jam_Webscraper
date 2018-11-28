#include <bits/stdc++.h>
using namespace std;
int sum[2001], cnt[2001];
int T, n, c, m, x, y;
bool check(int K) {
	int res = 0;
	for (int i=1; i<=n; i++) {
		res += K;
		if (sum[i] > res) return 0;
		res -= sum[i];
	} return 1;
}
int main() {
	freopen("B-large.in", "r", stdin);
	freopen("B-large.out", "w", stdout);
	//freopen("B-large.in", "r", stdin);
	//freopen("B-large.out", "w", stdout);
	scanf("%d", &T);
	for(int i=1; i<=T; i++) {
		memset(cnt, 0, sizeof cnt);
		memset(sum, 0, sizeof sum);
		scanf("%d%d%d", &n, &c, &m);
		int mx = 0; 
		for(int i=0; i<m; i++) {
			scanf("%d%d", &x, &y);
			++sum[x];
			mx = max(mx, ++cnt[y]);
		}
		
		int L = mx - 1, R = m, X = 0;
		while(L+1 < R) {
			int M = (L+R) / 2;
			if (check(M)) R = M; else L = M;
		} R = max(R, mx);
		
		for (int i=1; i<=n; i++)
			if (sum[i] >= R) X += sum[i]-R;
		printf("Case #%d: %d %d\n", i, R, X);
	}
}
