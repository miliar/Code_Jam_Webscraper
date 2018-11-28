/******************************************
*    AUTHOR:         BHUVNESH JAIN        *
*    INSTITUITION:   BITS PILANI, PILANI  *
******************************************/
#include <bits/stdc++.h>
using namespace std;
 
typedef long long LL; 
typedef long double LD;
typedef pair<int,int> pii;
typedef pair<LL, LL> pll;

int main() {
	ios_base::sync_with_stdio(false);
	int t, n, k, x, y;
	cin >> t;
	for(int T = 1; T <= t; ++T) {
		cout << "Case #" << T << ": ";

		string s, a, b;
		cin >> s >> k;
		n = s.length();
		a = s;
		b = s;
		x = 0;
		for(int i = 0; i <= n-k; ++i) {
			if (a[i] == '-') {
				for(int j = i; j <= i+k-1; ++j) {
					if (a[j] == '-') {
						a[j] = '+';
					}
					else {
						a[j] = '-';
					}
				}
				x += 1;
			}
		}
		reverse(b.begin(), b.end());
		y = 0;
		for(int i = 0; i <= n-k; ++i) {
			if (b[i] == '-') {
				for(int j = i; j <= i+k-1; ++j) {
					if (b[j] == '-') {
						b[j] = '+';
					}
					else {
						b[j] = '-';
					}
				}
				y += 1;
			}
		}

		for(int i = 0; i < n; ++i) {
			if (a[i] == '-') {
				x = INT_MAX;
				break;
			}
		}
		for(int i = 0; i < n; ++i) {
			if (b[i] == '-') {
				y = INT_MAX;
				break;
			}
		}
		if (x == INT_MAX && y == INT_MAX) {
			cout << "IMPOSSIBLE\n";
		}
		else {
			cout << min(x, y) << "\n";
		}
	}
	return 0;
}