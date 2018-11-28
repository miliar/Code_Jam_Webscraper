#include <bits\stdc++.h>
using namespace std;
const int N = 1010;
int T, cas, n, C, m;
int cnt[N], pos[N];

int calc(int y) {
	int sum = 0, ret = 0;
	for (int i = 1; i <= n; i++) {
		sum += pos[i];
		if(sum > i*y) return -1;
		if(pos[i] > y) ret += pos[i] - y;
	}
	return ret;
}

int main() {
	freopen("B-large.in", "r", stdin);
	freopen("B.out", "w", stdout);
	scanf("%d", &T);
	int pi, bi;
	for (cas = 1; cas <= T; cas++) {
		scanf("%d%d%d", &n, &C, &m);
		memset(cnt, 0, sizeof(cnt));
		memset(pos, 0, sizeof(pos));
		for (int i = 0; i < m; i++) {
			scanf("%d%d", &pi, &bi);
			cnt[bi]++;
			pos[pi]++;
		}
		int l = 0, r = m;
		for (int i = 0; i <= C; i++) l = max(l, cnt[i]);
		while(l < r) {
			int mid = (l + r) >> 1;
			if(calc(mid) != -1) r = mid;
			else l = mid+1;
		}
		printf("Case #%d: %d %d\n", cas, l, calc(l));
	}
	return 0;
}