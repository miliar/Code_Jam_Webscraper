#include <bits/stdc++.h>

#define ll long long
#define mp make_pair
#define fi first
#define se second
#define pb push_back
#define ld double

using namespace std;

const int nm = 110;

int n, p;
int a[nm];
int cnt[10];

void solve(int test) {
	printf("Case #%d: ", test);
	scanf("%d%d", &n, &p);
	memset(cnt, 0, sizeof(cnt));
	int sum = 0;
	for (int i = 1; i <= n; ++i) {
		scanf("%d", &a[i]);
		cnt[a[i] % p]++;
		sum = (sum + a[i]) % p;
	}
	if (p == 2) {
		printf("%d\n", cnt[0] + cnt[1] / 2 + 1 - (sum == 0));
		return;
	}
	if (p == 3) {
		int res = 0;
		for (int i = 0; i * 3 <= cnt[1]; ++i) {
			for (int j = 0; j <= cnt[1] - i * 3 && j <= cnt[2]; ++j) {
				res = max(res, i + j + (cnt[2] - j) / 3);
			}
		}
		printf("%d\n", cnt[0] + res + 1 - (sum == 0));
		return;
	}
	if (p == 4) {
		int res = 0;
		for (int i = 0; 2 * i <= cnt[1] && i <= cnt[2]; ++i) {
			for (int j = 0; j <= cnt[1] - 2 * i && j <= cnt[3]; ++j) {
				for (int k = 0; k <= cnt[2] - i && 2 * k <= cnt[3] - j; ++k) {
					res = max(res, i + j + k + (cnt[1] - 2 * i - j) / 4 + (cnt[2] - i - k) / 2 + (cnt[3] - j - 2 * k) / 4);
				}
			}
		}
		printf("%d\n", cnt[0] + res + 1 - (sum == 0));
		return;
	}
	printf("-1\n");
}

int main() {
#ifdef LOCAL
	freopen("A-large.in", "r", stdin);
	freopen("output.txt", "w", stdout);
#endif
	int t;
	scanf("%d", &t);
	for (int i = 1; i <= t; ++i) {
		solve(i);
	}
}
