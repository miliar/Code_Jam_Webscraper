#include <bits/stdc++.h>
using namespace std;

int ans, c;
int n, m, P[1010], now[1010], B[1010], res[1010], cnt[1010];
int T, t_;

bool judge(int k) {
	ans = 0;
	memset(res, 0, sizeof(res));
	
	for (int i = 1; i <= m; i++) res[P[i]]++;
	for (int i = 1; i <= n; i++) now[i] = k;
	for (int i = n; i >= 1; i--) {
		if (res[i] <= now[i]) {
			res[i] = 0;
		} else {
			res[i] -= now[i];
			now[i] = 0;
			ans += res[i];
			int q = 1;
			while (q < i && res[i]) {
				int just = min(res[i], now[q]);
				res[i] -= just;
				now[q] -= just;
				q++;
			}
			if (res[i]) return false;
		}
	}
	return true;
}

int main() {
	freopen("B.in","r",stdin);
	freopen("B.out","w",stdout);
	for (scanf("%d",&T); T; T--) {
		printf("Case #%d: ",++t_);
		scanf("%d %d %d",&n,&c,&m);
		memset(cnt, 0, sizeof(cnt));
		for (int i = 1; i <= m; i++) {
			scanf("%d %d",&P[i],&B[i]);
			cnt[B[i]]++;
		}
		int L = 0, R;
		for (int i = 1; i <= c; i++)
			L = max(L, cnt[i]);
		R = 1000;
		while (L < R) {
			int mid = (L + R) / 2;
			if (judge(mid)) R = mid;
			else L = mid + 1;
		}
		judge(L);
		printf("%d %d\n",L,ans);
	}
	return 0;
}
