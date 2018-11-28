#include <cstdio>
#include <algorithm>
using namespace std;

typedef long long i64;

i64 p[20], n;
int T, a[20];

int main() {
	freopen("B.in", "r", stdin);
	scanf("%d", &T);

	p[0] = 1;
	for (int i = 1; i <= 19; ++i)
		p[i] = p[i - 1] * 10;

	for (int id = 1; id <= T; ++id) {
		scanf("%lld", &n);
		int l = 0;
		while (n > 0) {
			a[l++] = n % 10;
			n /= 10;
		}

		i64 cur = 0, ans = 0;
		for (int i = l - 1; i >= 0; --i) {
			if (i != l - 1 && a[i] < a[i + 1]) break;
			cur = cur * 10 + a[i];
			if (a[i] != 0 && a[i] != a[i + 1]) {
				ans = max(ans, (cur - 1) * p[i] + (p[i] - 1));
			}
			if (i == 0)
				ans = max(ans, cur);
		}

		printf("Case #%d: %lld\n", id, ans);
	}

	return 0;
}
