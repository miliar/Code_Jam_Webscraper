#include <bits/stdc++.h>

#define eb emplace_back
#define pb push_back
#define mp make_pair
#define fi first
#define se second
#define INF 0x3f3f3f3f

using namespace std;

typedef long long ll;
typedef pair<int, int> pii;
typedef vector<int> vi;
const int N = 100010;

int d, n; 
int k[N], s[N];
bool ok (double vel) {
	double tempo = d / vel;
	for (int i = 0; i < n; i++) {
		double t2 = (d - k[i]) / (1. * s[i]);
		if (t2 > tempo) return false;
	}
	return true;
}
int main (void) {
	int t; scanf("%d", &t);
	while (t--) {
		scanf("%d %d", &d, &n);
		for (int i = 0; i < n; i++) {
			scanf("%d %d", k+i, s+i);
		}

		double lo = 0, hi = 1000000000000000000., ans;
		for (int it = 1000; it; it--) {
			double mid = (lo + hi) / 2;
			if (ok(mid)) {
				ans = mid;
				lo = mid;
			} else {
				hi = mid;
			}
		}
		static int ca = 1;
		printf("Case #%d: %.9lf\n", ca++, ans);
	}
	return 0;
}

