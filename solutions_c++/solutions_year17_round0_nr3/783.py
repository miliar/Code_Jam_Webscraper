#include <bits/stdc++.h>
typedef long long int i64;
using namespace std;

int main() {
	int t;
	i64 n, k, a[2], b[2], f = 0, mx, mn;
	cin >> t;
	for(int test = 1; test <= t; test++) {
		cin >> n >> k;
		a[0] = n; b[0] = n;
		a[1] = 1; b[1] = 0; f = 0;
		while(f + a[1] + b[1] < k) {
			f = f + a[1] + b[1];
			if(a[0] & 1) {
				a[0] = a[0] / 2;
				b[0] = b[0] / 2;
				a[1] = a[1] * 2 + b[1];
			} else {
				a[0] = (a[0] - 1) / 2;
				b[0] = b[0] / 2;
				b[1] = b[1] * 2 + a[1];
			}
		}
		if(f + b[1] < k) {
			mx = a[0] / 2;
			mn = (a[0] - 1) / 2;
		} else {
			mx = b[0] / 2;
			mn = (b[0] - 1) / 2;
		}
		cout << "Case #" << test << ": " << mx << " " << mn << endl;
	}
	return 0;
}