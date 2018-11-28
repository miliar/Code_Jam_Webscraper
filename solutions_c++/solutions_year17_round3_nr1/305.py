#include <vector>
#include <algorithm>
#include <iostream>
using namespace std;

using DB = double;
using II = pair<int, int>;
using VII = vector<pair<int, int> >;
const DB PI = 3.1415926535897932384;


DB getSide(II p) {
	return 2.0 * PI * p.first * p.second;
}

bool cmp(II a, II b) {
	return getSide(a) > getSide(b);
}

int main() {
	freopen("A.in", "r", stdin);
	freopen("A.out", "w", stdout);
	int T; cin >> T;
	for (int kase = 1; kase <= T; ++kase) {
		int n, k; cin >> n >> k;
		vector<pair<int, int> > p(n);
		for (int i = 0; i < n; ++i)
			cin >> p[i].first >> p[i].second;
		sort(p.begin(), p.end(), cmp);
		DB ans = 0;
		DB tmp = 0;
		int maxR = 0;
		for (int i = 0; i < k - 1; ++i) {
			tmp += getSide(p[i]);
			maxR = max(maxR, p[i].first);
		}
		for (int i = k - 1; i < n; ++i) {
			ans = max(ans, tmp + getSide(p[i]) + 
					PI * max(maxR, p[i].first) * max(maxR, p[i].first));
		}

		printf("Case #%d: %.12lf\n", kase, ans);
	}

	return 0;
}
