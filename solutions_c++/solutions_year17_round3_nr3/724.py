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
		double u;
		cin >> n >> k >> u;
		vector <double> p;
		for (int i = 0; i < n; i++) {
			double tmp;
			cin >> tmp;
			p.push_back(tmp);
		}

		//while (u > 0.0 && p[0] < 1.0) {
		//	sort(p.begin(), p.end());
		//	double diff = 0.0;
		//	int count = -1;
		//	for (int i = 1; i < n; i++) {
		//		if (p[i] > p[i - 1]) {
		//			diff = p[i] - p[i - 1];
		//			count = i;
		//			break;
		//		}
		//	}
		//	if (count < 0) {
		//		count = n;
		//		diff = 1.0 - p[0];
		//	}

		//	if (diff * count > u) {
		//		diff = u / count;
		//		for (int i = 0; i < count; i++) {
		//			p[i] = max(p[i] + diff, 1.0);
		//		}
		//		u = 0.0;
		//	} else {
		//		u -= diff * count;
		//		for (int i = 0; i < count; i++) {
		//			p[i] = max(p[i] + diff, 1.0);
		//		}
		//	}
		//}
		//sort(p.begin(), p.end());

		sort(p.begin(), p.end());
		double l = 0.0;
		double r = 1.0;
		double mid;
		for (int k = 0; k < 1000; k++) {
			mid = (l + r) / 2;
			double sum = 0.0;
			for (int i = 0; i < n; i++) {
				sum += max(0.0, mid - p[i]);
			}
			//cout << sum << ", " << u << " : " << mid <<  endl;
			if (sum < u) {
				l = mid;
			} else {
				r = mid;
			}
		}

		double ret = 1.0;
		for (int i = 0; i < n; i++) {
			ret *= max(p[i], mid);
			//cout << p[i] << ",";
		}
		//cout << endl;

		cout.precision (15);
		cout << "Case #" << t << ": " << ret << endl;;
	}
}

