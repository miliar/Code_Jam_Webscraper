#include <bits/stdc++.h>
using namespace std;
/*int solve(vector<int> a, int m) {
	vector<int> p;
	int n = a.size();
	for (int i = 0; i < n; ++ i) p.push_back(i);
	int ans = 0;
	do {
		int res = 0, mo = 0;
		for (int i = 0; i < n; ++ i) {
			if (mo == 0) res ++;
			mo = (mo + a[p[i]]) % m;
		}
		ans = max(ans, res);
	} while (next_permutation(p.begin(), p.end()));
	return ans;
}*/
int main() {
	int T;
	scanf("%d", &T);
	int zzz = 0;
	while (T --) {
		int n, m;
		//n = 8, m = rand() % 3 + 2;
		scanf("%d%d", &n, &m);
		vector<int> a;
		int cnt[4] = {0, 0, 0, 0};
		for (int i = 1; i <= n; ++ i) {
			int x;
			scanf("%d", &x);
			cnt[x % m] ++;
			a.push_back(x);
		}
		//int duipai = solve(a, m);
		int ans = 0;
		if (m == 2) {
			ans = (cnt[1] + 1) / 2 + cnt[0];
		}
		else if (m == 3) {
			ans = cnt[0] + min(cnt[1], cnt[2]) + (max(cnt[1], cnt[2]) - min(cnt[1], cnt[2]) + 2) / 3;
		}
		else {
			ans = cnt[0] + min(cnt[1], cnt[3]) + cnt[2] / 2;
			int left1 = max(cnt[1], cnt[3]) - min(cnt[1], cnt[3]);
			int left2 = cnt[2] % 2;
			vector<int> rem;
			for (int i = 0; i < left2; ++ i) rem.push_back(2);
			for (int i = 0; i < left1; ++ i) rem.push_back(1);
			int mo = 0;
			for (int i : rem) {
				if (mo == 0) ans ++;
				mo = (mo + i) % 4;
			}
		}
		printf("Case #%d: %d\n", ++ zzz, ans);
		//assert(ans == duipai);
	}
}

