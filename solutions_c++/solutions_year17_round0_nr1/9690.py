#include <algorithm>
#include <cstdlib>
#include <cstdio>
#include <iostream>
#include <cmath>
#include <cstring>

using namespace std;

int main() {
	int n, m, l, ans = 0, a[2000];
	cin >> n;
	string s;
	for (int i = 0; i < n; i++) {
		ans = 0;
		cin >> s;
		cin >> m;
		l = s.length();
		for (int j = 0; j < l; j++)
			if (s[j] == '+')
				a[j] = 0;
			else
				a[j] = 1;
		for (int j = 0; j < l - m + 1; j++) {
			if (a[j]) {
				ans++;
				for (int k = 0; k < m; k++) a[j + k] = 1 - a[j + k];
			}
		}
		bool f = true;
		for (int j = l - m + 1; j < l; j++) {
			if (a[j]) f = false;
		}
		if (f)
			cout << "Case #" << (i + 1) << ": " << ans << endl;
		else
			cout << "Case #" << (i + 1) << ": " << "IMPOSSIBLE" << endl;
	}
}