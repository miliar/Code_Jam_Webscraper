#include <bits/stdc++.h>
using namespace std;
#define eb emplace_back
#define emp emplace
#define fi first
#define se second
#define INF 0x3f3f3f3f
typedef long long ll;
typedef pair<int,int> ii;

int n, k;

bool cmp(tuple<double, double, int> a, tuple<double, double, int> b) {
	return get<1>(a)*get<0>(a) < get<1>(b)*get<0>(b);
}

int main(void) {
	ios_base::sync_with_stdio(false);
	int t;
	cin >> t;

	int cnt = 1;
	while (t--) {
		vector<tuple<double, double, int>> v, w;
		cin >> n >> k;

		for (int i = 0; i < n; i++) {
			double a, b;
			cin >> a >> b;
			v.eb(a, b, i);
		}

		w = v;
		sort(v.rbegin(), v.rend());
		sort(w.rbegin(), w.rend(), cmp);


		double ans = 0;
		for (int i = 0; i < n; i++) {
			double aux = acos(-1) * get<0>(v[i]) * get<0>(v[i]) + acos(-1) * 2 * get<0>(v[i]) * get<1>(v[i]);
			int id = get<2>(v[i]);
			int got = 0;
			for (int j = 0; j < n; j++) {
				if (got == k-1) break;
				if (get<2>(w[j]) != id and get<0>(w[j]) <= get<0>(v[i])) {
					aux += 2*acos(-1)*get<0>(w[j])*get<1>(w[j]);
					got++;
				}
			}
			if (got == k-1) {
				ans = max(ans, aux);
			}
		}

		cout << setprecision(7) << fixed;
		cout << "Case #" << cnt++ << ": " << ans << endl;
	}

	return 0;
}
