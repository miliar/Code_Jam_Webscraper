#define _CRT_SECURE_NO_WARNINGS

#include <cstdio>
#include <cstring>
#include <string>
#include <map>
#include <algorithm>

using namespace std;

using ll = long long;

void solve() {
	int N, P;
	scanf("%d%d", &N, &P);
	int cnt[5];
	for (int i = 0; i < P; ++i) {
		cnt[i] = 0;
	}
	for (int i = 0; i < N; ++i) {
		int t;
		scanf("%d", &t);
		t %= P;
		cnt[t] += 1;
	}
	int ans;
	if (P == 2) {
		ans = cnt[0] + (cnt[1] + 1) / 2;
	}
	if (P == 3) {
		ans = cnt[0];
		int m = min(cnt[1], cnt[2]);
		ans += m;
		int n = max(cnt[1], cnt[2]) - m;
		ans += (n + 2) / 3;
	}
	if (P == 4) {
		ans = cnt[0];
		int m = min(cnt[1], cnt[3]);
		ans += m;
		ans += cnt[2] / 2;
		int left = 0;
		int val = 1;
		if (cnt[3] > cnt[1]) {
			val = 3;
		}
		if (cnt[2] % 2 != 0) {
			left = 2;
			ans += 1;
		}
		int n = cnt[val] - m;
		while (n) {
			if (left == 0) {
				ans += 1;
			}
			left = (left + val) % P;
			--n;
		}
	}
	printf("%d\n", ans);
}

int main() {
	freopen("ain.txt", "r", stdin);
	freopen("aout.txt", "w", stdout);

	int T;
	scanf("%d", &T);
	for (int i = 0; i < T; ++i) {
		fprintf(stderr, "%d\n", i + 1);
		printf("Case #%d: ", i + 1);
		solve();
	}
	return 0;
}