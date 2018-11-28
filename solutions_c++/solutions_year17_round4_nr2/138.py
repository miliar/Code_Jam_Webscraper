#include <bits/stdc++.h>

#define debug(x) cout << #x << " = " << x << endl
#define fori(i, ini, lim) for(int i = int(ini); i < int(lim); i++)
#define ford(i, ini, lim) for(int i = int(ini); i >= int(lim); i--)

using namespace std;

typedef long long ll;
typedef pair<int, int> ii;

const int MAX = 1e3 + 5;
int seat_app[MAX], guy_app[MAX];
int n, c, m;

inline bool good(int rides) {
	int f = 0;
	fori(i, 1, n + 1) {
		f += rides;
		if(seat_app[i] > f) {
			return false;
		}
		f -= seat_app[i];
	}
	return true;
}

int main() {
	int t;
	scanf("%d", &t);
	int kase = 1;
	while(t--) {
		scanf("%d %d %d", &n, &c, &m);
		memset(seat_app, 0, sizeof seat_app);
		memset(guy_app, 0, sizeof guy_app);
		int left = 0;
		fori(i, 1, m + 1) {
			int p, g;
			scanf("%d %d", &p, &g);
			seat_app[p]++;
			guy_app[g]++;
			left = max(left, guy_app[g]);
		}
		int right = 100000;
		int best = -1;
		while(left <= right) {
			int mid = (left + right) / 2;
			if(good(mid)) {
				best = mid;
				right = mid - 1;
			}
			else {
				left = mid + 1;
			}
		}
		int swaps = 0;
		int f = 0;
		fori(i, 1, n + 1) {
			f += best;
			if(seat_app[i] > best) {
				swaps += seat_app[i] - best;
			}
			f -= seat_app[i];
		}
		printf("Case #%d: %d %d\n", kase++, best, swaps);
	}

	return 0;
}

