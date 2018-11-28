#include <iostream>
#include <cmath>
#include <vector>
#include <limits>
#include <iomanip>
#include <algorithm>

using namespace std;

long double get_side(pair<int, int> p) {
	return 2 * M_PI * p.first * p.second;
}

long double get_estim(pair<int, int> p) {
	return M_PI * p.first * p.first + get_side(p);
}

bool comp_side(pair<int, int> a, pair<int, int>b) {
	return get_side(a) > get_side(b);	
}

int main(int argc, char *argv[]) {
	int t;
	cin >> t;
	for (int _ = 0; _ < t; ++_) {
		vector<pair<int, int> > v;
		int n, k;
		cin >> n >> k;
		for (int __ = 0; __ < n; ++__) {
			pair<int, int> p;
			// r, h
			cin >> p.first >> p.second;
			v.push_back(p);
		}

		// Sort
		sort(v.begin(), v.end(), comp_side);

		// Find the largest radius in the k largest pie
		int l_rad = 0;
		for (int i = 0; i < k; ++i) {
			if (v[i].first > l_rad) {
				l_rad = v[i].first;
			}
		}

		// Find the smallest
		long double s_val = get_side(v[k - 1]);
		s_val += M_PI * l_rad * l_rad;

		// Try every pair not chosen yet that has larger radius
		int l_idx = k - 1;
		for (int i = k; i < n; ++i) {
			// Radius larger
			if (v[i].first > l_rad) {
				long double n_v = get_estim(v[i]);
				// Worth the trade
				if (n_v > s_val) {
					s_val = n_v;
					l_idx = i;
					l_rad = v[i].first;
				}
			}
		}

		// Swap!!
		v[k - 1] = v[l_idx];

		long double sum = 0;
		for (int i = 0; i < k; ++i) {
			sum += get_side(v[i]);
		}
		sum += M_PI * l_rad * l_rad;


		cout << fixed << setprecision(9) << "Case #" << _ + 1 << ": " << sum << endl;
	}
}
