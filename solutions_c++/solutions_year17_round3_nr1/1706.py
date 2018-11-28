#include <bits/stdc++.h>
using namespace std;

const double pi = 3.141592653589793;

int64_t areaBody(pair<int, int> a) {
	int64_t r = a.first, h = a.second;
	return 2 * r * h;
}
int64_t areaFace(pair<int, int> a) {
	int64_t r = a.first, h = a.second;
	return r * r;
}

#define N 1000
int n, K;
pair<int, int> p[N];
int64_t ans;

bool cmp(pair<int, int> a, pair<int, int> b) {
	return areaBody(a) > areaBody(b);
}


int main() {

	freopen("A-large.in", "r", stdin);
	//freopen("main.in", "r", stdin);
	freopen("main.out", "w", stdout);
	int T; cin >> T;
	cout << setprecision(9) << fixed;
	for (int t = 1; t <= T; ++t) {
		cin >> n >> K;
		for (int i = 0; i < n; ++i) {
			cin >> p[i].first >> p[i].second;
		}
		sort(p, p + n, cmp);
		ans = 0;
		for (int pos = 0; pos < n; ++pos) {
			int64_t res = areaBody(p[pos]) + areaFace(p[pos]);
			int k = K - 1;
			for (int i = 0; i < n && k > 0; ++i) {
				if (i == pos || p[i].first > p[pos].first) {
					continue;
				}
				res += areaBody(p[i]);
				k -= 1;
			}
			if (k > 0) {
				continue;
			}
			ans = max(ans, res);
		}
		cout << "Case #" << t << ": " << double(ans) * pi << "\n";
	}
	fclose(stdout);
}
