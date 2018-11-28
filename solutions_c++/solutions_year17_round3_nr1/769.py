#include <iostream>
#include <fstream>
#include <cstdio>
#include <vector>
#include <iomanip>
#include <set>
#include <queue>
#include <map>
#include <algorithm>
#include <functional>
#include <list>
#include <cmath>

using namespace std;

typedef long long ll;
typedef pair<ll, ll> ii;

const double PI = atan(1) * 4;

double height(ii a) {
	double r = a.first;
	double h = a.second;
	return 2 * PI * r * h;
}

double area(ii a) {
	double r = a.first;
	double h = a.second;
	return PI * r * r;
}

double surf(ii a) {
	return height(a) + area(a);
}

bool comp(ii a, ii b) {
	return surf(a) > surf(b);
}

int main() {
#ifdef _DEBUG
	freopen("a.in", "r", stdin);
	freopen("a.out", "w", stdout);
#endif
	ios::sync_with_stdio(false);
	
	int T;
	cin >> T;
	for (int t = 1; t <= T; t++) {
		cout << "Case #" << t << ": ";

		ll n, k;
		cin >> n >> k;

		vector<ii> v;
		for (int i = 0; i < n; i++) {
			ll r, h;
			cin >> r >> h;
			v.push_back(ii(r, h));
		}

		double maxRes = 0;
		for (int i = 0; i < (1 << n); i++) {
			double res = 0;
			ll maxr = 0;
			int ii = i;
			int b = 0;
			int cnt = 0;
			while (ii > 0) {
				if ((ii & 1) == 1) {
					res += height(v[b]);
					maxr = max(maxr, v[b].first);
					cnt++;
				}
				ii = ii >> 1;
				b++;
			}
			res += PI * maxr * maxr;
			if (cnt == k) {
				maxRes = max(res, maxRes);
			}
		}

		cout << fixed << setprecision(9) << maxRes << endl;
	}

	return 0;
}