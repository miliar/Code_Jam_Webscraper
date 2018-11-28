#include <iostream>
#include <cmath>
#include <vector>
#include <limits>
#include <iomanip>
#include <algorithm>

using namespace std;

void split(vector<long double *> v, long double u) {
	vector<long double *> n;
	bool need_rec = false;
	long double avg = 0, max = 0;
	avg += u;
	avg /= v.size();
	for (long double *d : v) {
		if (*d > avg) {
			need_rec = true;
			continue;
		}
		n.push_back(d);
	}
	if (need_rec) {
		split(n, u);
	} else {
		for (long double *d : v) {
			*d = avg;
		}
	}
}

bool compare(long double a, long double b) {
	return a > b;
}

int main(int argc, char *argv[]) {
	int t;
	cin >> t;
	for (int _ = 0; _ < t; ++_) {
		vector<long double> v;
		// vector<long double *> ref;
		int n, k;
		cin >> n >> k;
		long double u;
		cin >> u;
		for (int _ = 0; _ < n; ++_) {
			long double d;
			cin >> d;
			v.push_back(d);
		}
		sort(v.begin(), v.end(), compare);
		int idx = 0;
		while (idx < v.size()) {
			long double sum = 0;
			for (int i = idx + 1; i < v.size(); ++i) {
				sum += v[i];
			}
			sum += u;
			if (sum < v[idx] * (v.size() - idx - 1)) {
				++idx;
				continue;
			}
			sum += v[idx];
			sum /= (v.size() - idx);
			for (int i = idx; i < v.size(); ++i) {
				v[i] = sum;
			}
			break;
		}
		long double prob = 1;
		for (long double &d : v) {
			if (d > 1)
				d = 1;
			prob *= d;
			// cout << d << " ";
		}
		// cout << endl;
		cout << fixed << setprecision(6) <<  "Case #" << _ + 1 << ": " << prob << endl;
	}
}
