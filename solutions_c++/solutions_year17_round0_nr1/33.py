#include <iostream>
#include <iomanip>
#include <cmath>
#include <algorithm>
#include <cstring>
#include <string>
#include <vector>
#include <set>
#include <stack>
#include <queue>

using namespace std;



int main() {
	int t;
	cin >> t;
	for (int tt = 1; tt <= t; tt ++) {
		string s;
		int k;
		cin >> s >> k;
		int n = s.length();
		int cnt = 0;
		for (int i = 0; i <= n-k; i ++) {
			if (s[i] == '-') {
				cnt ++;
				for (int j = i; j < i+k; j ++) {
					if (s[j] == '-') s[j] = '+';
					else s[j] = '-';
				}
			}
		}
		bool flag = true;
		for (int i = 0; i < n; i ++) {
			if (s[i] == '-') {
				flag = false;
			}
		}
		cout << "Case #" << tt << ": ";
		if (flag) cout << cnt << endl;
		else cout << "IMPOSSIBLE" << endl;

	}

	return 0;
}

