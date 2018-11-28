#include <sstream>
#include <string>
#include <vector>
#include <map>
#include <algorithm>
#include <iostream>
#include <utility>
#include <set>
#include <cctype>
#include <queue>
#include <stack>
#include <cstdio>
#include <cstdlib>
#include <cmath>
#include <cstring>

using namespace std;

int main() {
	int T;
	cin >> T;
	for (int t = 1; t <= T; t++) {
		int n;
		int k;
		vector <int> r;
		vector <int> h;
		cin >> n >> k;
		for (int i = 0; i < n; i++) {
			int tmp1, tmp2;
			cin >> tmp1 >> tmp2;
			r.push_back(tmp1);
			h.push_back(tmp2);
		}

		vector <double> area;
		vector <double> circum;

		for (int i = 0; i < n; i++) {
			area.push_back((double)r[i] * r[i] * M_PI);
			circum.push_back((double)r[i] * 2 * M_PI * h[i]);
		}

		for (int i = 0; i < n; i++) {
			for (int j = i + 1; j < n; j++) {
				if (circum[i] < circum[j] ){
					double work = circum[i];
					circum[i] = circum[j];
					circum[j] = work;
					work = area[i];
					area[i] = area[j];
					area[j] = work;
				}
			}
		}

		double ret = 0.0;
		double maxArea = 0.0;
		for (int i = 0; i < k; i++) {
			ret += circum[i];
			maxArea = max(maxArea, area[i]);
		}
		ret += maxArea;

		double mx = 0.0;
		int idx = -1;
		for (int i = 0; i < n; i++) {
			if (mx < area[i]) {
				mx = area[i];
				idx = i;
			}
		}
		double tmp = 0.0;
		if (idx >= k) {
			for (int i = 0; i < k - 1; i++) {
				tmp += circum[i];
			}
			tmp += mx;
			tmp += circum[idx];
		}
		ret = max(ret, tmp);

		cout.precision (15);
		cout << "Case #" << t << ": " << ret << endl;;
	}
}

