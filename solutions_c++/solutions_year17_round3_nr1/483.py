#include <bits/stdc++.h>
#define ll long long
using namespace std;

const int N = 1005;
const long double pi = acos(-1.0);

int n, k, id[N];
ll r[N], h[N];

bool cmp(int i, int j) {
	return (long double)2 * pi * r[i] * h[i] > (long double)pi * 2 * r[j] * h[j];
}

int main() {
	freopen("A-large.in", "r", stdin);
	freopen("2.txt", "w", stdout); 
	int T, cas = 0;
	scanf("%d", &T);
	while (T--) {
		scanf("%d %d", &n, &k);
		for (int i = 1; i <= n; i++) scanf("%I64d %I64d", r + i, h + i), id[i] = i;
		sort(id + 1, id + 1 + n, cmp);
		long double tmp, H, ans = 0;
		for (int i = 1; i <= n; i++) {
			tmp = 0; 
			tmp += pi * r[i] * r[i] + 2 * pi * r[i] * h[i];
			int K = k - 1;
			for (int j = 1; j <= n; j++) {
				if (K && i != id[j] && r[id[j]] <= r[i]) {
					K--;
					tmp += 2 * pi * r[id[j]] * h[id[j]];
				}
			}
			if (tmp > ans && K == 0) ans = tmp;
		}
		printf("Case #%d: %.10f\n", ++cas, (double)ans);
	}
}
