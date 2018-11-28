#include <bits/stdc++.h>
using namespace std;

const int N = 1e3 + 10;

struct node {
	int r, h;
} A[N];

int comp(node a, node b) {
	return a.r > b.r || (a.r == b.r && a.h > b.h);
}

int comp2(node a, node b) {
	return a.r * 1ll * a.h > b.r * 1ll * b.h;
}

const long double PI = 2. * acos(0.);

int main() {
	int t;
	scanf("%d", &t);
	for(int tc = 1; tc <= t; ++tc) {
		int n, k;
		scanf("%d %d", &n, &k);
		for(int i = 1; i <= n; ++i) {
			scanf("%d %d", &A[i].r, &A[i].h);
		}

		long long mx = 0;
		for(int i = 1; i <= n; ++i) {
			sort(A + 1, A + n + 1, comp);
			long long curr = A[i].r * 1ll * (A[i].r + 2 * A[i].h);
			int num = 1;
			sort(A + i + 1, A + n + 1, comp2);
			for(int j = i + 1; j <= n && num < k; ++j, ++num) {
				curr += A[j].r * 2ll * A[j].h;
			}
			mx = max(mx, curr);
		}
		double ans = PI * mx;
		printf("Case #%d: %.9lf\n", tc, ans);
	}
}