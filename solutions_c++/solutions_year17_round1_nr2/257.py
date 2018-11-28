#include <iostream>
#include <iomanip>
#include <cmath>
#include <algorithm>
#include <string>
#include <cstring>
#include <vector>
#include <set>
#include <queue>
#include <map>

using namespace std;

int close_to(double x) {
	int ans = (int)(x + 0.5);
//	if (abs(x - ans) > 0.1) return -1;
	return ans;
}

bool close_(double x, double cand) {
	return cand * 0.9 <= x && x <= cand * 1.1;
}

int main() {
	int t;
	cin >> t;
	for (int tt = 1; tt <= t; tt ++) {
		cout << "Case #" << tt << ": ";
		int n, p;
		cin >> n >> p;
		int r[50];
		double q[50][50];
		set<int> s;
		for (int i = 0; i < n; i ++) cin >> r[i];
		for (int i = 0; i < n; i ++) for (int j = 0; j < p; j ++) cin >> q[i][j];
		for (int i = 0; i < n; i ++) {
			for (int j = 0; j < p; j ++) {
				q[i][j] /= r[i];
				if (close_to(q[i][j]) != -1) s.insert(close_to(q[i][j]));
			}
			sort(begin(q[i]), begin(q[i]) + p);
		}
/*		for (int i = 0; i < n; i ++) {
			for (int j = 0; j < p; j ++) {
				cout << q[i][j] << ' ';
			}
			cout << endl;
		}
*/		int pointer[50];
		for (int i = 0; i < n; i ++) pointer[i] = 0;
		int ans = 0;
//		int cnt = 0;
		for (int cand = 1; cand <= 1000000; cand ++) {
//			int cand = *(s.begin());
//			cout << "cand: " << cand << endl;
			bool valid = true;
			for (int i = 0; i < n; i ++) {
				while (pointer[i] < p && q[i][pointer[i]] < (double)(cand)*0.9  /*&& !close_(q[i][pointer[i]], cand)*/) pointer[i] ++;
//				cout << pointer[i] << q[i][pointer[i]] << cand << endl;
				if (pointer[i] == p || !close_(q[i][pointer[i]], cand)) valid = false;
			}
//			if (!valid) s.erase(cand);
			if (valid) {
				ans ++;
				cand --;
				for (int i = 0; i < n; i ++) pointer[i] ++;
			}
//			cnt ++;
		}
		cout << ans << endl;
	}
	return 0;
}

