#include <cstdio>
#include <cstdlib>
#include <cstring>
#include <cmath>
#include <algorithm>
#include <utility>
#include <queue>

using namespace std;

int n, k;
pair<int, int> p[1111];

#define fst first
#define snd second

typedef long long ll;

bool cmp(const pair<int, int> &a, const pair<int, int> &b) {
	return ((ll)a.fst * a.snd < (ll)b.fst * b.snd);
}

int main() {
	int T;
	scanf("%d", &T);
	for (int kase = 1; kase <= T; ++ kase) {
		scanf("%d%d", &n, &k);
		for (int i = 0; i < n; ++ i) {
			scanf("%d%d", &p[i].fst, &p[i].snd);
		}
		sort(p, p + n, cmp);
		ll res = 0;
		for (int i = 0; i < n; ++ i) {
			ll tmp = (ll)p[i].fst * p[i].snd;
			int r = 1;
			for (int j = n - 1; j >= 0 && r != k; -- j) if (j != i) {
				if (p[j].fst <= p[i].fst) {
					++ r;
					tmp += (ll)p[j].fst * p[j].snd;
				}
			}
			if (r == k) {
				res = max(res, (ll)p[i].fst * p[i].fst + tmp * 2);
			}
		}
		printf("Case #%d: %.12lf\n", kase, acos(-1.0) * res);
	}
	return 0;
}
