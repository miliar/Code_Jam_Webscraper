# include <bits/stdc++.h>
using namespace std;

int N, C, M;
int cnt[1200];

int ans;
bool check(int limit) {
	ans = 0;
	int sum = 0;
	for(int i = 1; i <= N; ++i) {
		sum += cnt[i];
		if(sum > i * limit) return false;
		if(cnt[i] > limit) ans += cnt[i] - limit;
	}
	return true;
}

int main() {
	int T, cas = 0; scanf("%d", &T);
	while(T--) {
		scanf("%d%d%d", &N, &C, &M);
		int L = 0, R = M;
		map<int,int> buy;
		memset(cnt, 0, sizeof(cnt));
		for(int i = 0; i < M; ++i) {
			int p, b; scanf("%d%d", &p, &b);
			buy[b] += 1;
			L = max(L, buy[b]);
			cnt[p] += 1;
		}
		L -= 1;
		while(R - L > 1) {
			int mid = (L + R) >> 1;
			check(mid) ? R = mid : L = mid;
		}
		check(R);
		printf("Case #%d: %d %d\n", ++cas, R, ans);
	}
	return 0;
}

