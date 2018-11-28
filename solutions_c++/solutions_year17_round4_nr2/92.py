#include <bits/stdc++.h>
using namespace std;

int TC, N, M, C, P[1005], B[1005], positions[1005];
map<int, int> m;
multiset<int> pos;

int main() {
	scanf("%d", &TC);
	for (int tc = 1; tc <= TC; tc++) {
		scanf("%d%d%d", &N, &C, &M);
		for (int i = 0; i < M; i++) scanf("%d%d", &P[i], &B[i]);
		m.clear();
		for (int i = 0; i < M; i++) m[B[i]]++;
		int mx = 0;
		for (map<int, int>::iterator it = m.begin(); it != m.end(); it++) mx = max(mx, it->second);
		pos.clear();
		for (int i = 0; i < M; i++) pos.insert(P[i]);
		int ans = 0;
		while (pos.size() > 0) {
			for (int p = C; p >= 1; p--) {
				multiset<int>::iterator it = pos.lower_bound(p);
				if (it == pos.end()) continue;
				else pos.erase(it);
			}
			ans++;
		}
		ans = max(ans, mx);
		memset(positions, 0, sizeof(positions));
		int ans2 = 0;
		for (int i = 0; i < M; i++) {
			positions[P[i]]++;
			if (positions[P[i]] <= ans) ans2++;
		}
		printf("Case #%d: %d %d\n", tc, ans, M - ans2);
	}
}
