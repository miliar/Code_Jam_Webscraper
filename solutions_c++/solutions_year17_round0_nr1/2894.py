#include <cstdlib>
#include <cstdio>
#include <cstring>
#include <string>
#include <ctime>
#include <algorithm>
#include <map>
#include <set>
#include <cmath>
#include <vector>
#include <cassert>
#include <iostream>

using namespace std;

const double eps = 1e-9;
const int inf = 1e9 + 23;

const int size = 1000 + 23;

const int N = 4;

//const char[size] s;

void flip (string& s, int n, int k) {
	for (int i = 0; i < k; i++) {
		if (s[n + i] == '+') {
			s[n + i] = '-';
		} else {
			s[n + i] = '+';
		}
	}
}

int main (void){
	freopen("input.txt", "r", stdin);
	freopen("output.txt", "w", stdout);

	int n;

	int t;
	cin >> t;
	for (int it = 0; it < t; it++) {
		cout << "Case #" << it+1 << ": ";
		string kakes;
		int k;
		cin >> kakes;
		cin >> k;
		int d = 0;
		n = kakes.length();
		int ans = 0;
		// cout << "ans = " << ans << endl;
		// cout << "kakes = " << kakes << endl;
		// cout << "k = " << k << endl;
		for (int i = 0; i < n - k + 1; i++) {
			if (kakes[i] == '-') {
				flip(kakes, i, k);
				ans++;
				// cout << "kakses = " << kakes << endl;
			}
			// if ((kakes[i] == '+' && d == 1) || (kakes[i] == '-' && d == 0)) {
			// 	d = 1 - d;
			// 	ans++;
			// }
		}
		bool flag = true;
		for (int i = n - k + 1; i < n; i++) {
			if (kakes[i] == '-') {
				flag = false;
				break;
			}
		}
		if (!flag) {
			cout << "IMPOSSIBLE" << endl;
		} else {
			cout << ans << endl;
		}
	}

	return 0;
}