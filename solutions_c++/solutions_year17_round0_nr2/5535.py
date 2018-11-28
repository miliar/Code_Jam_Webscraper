#include <iostream>
#include <cstdlib>
#include <cstdio>

using namespace std;

void solve() {
	int a[100], sz = 0;
	long long n;
	cin >> n;
	while (n) {
		a[sz++] = n%10;
		n /= 10;
	}
	int r = 0;
	for (int i = 1; i < sz; i++) {
		if (a[i] > a[i-1]) {
			for (int j = i-1; j >= 0; j--) a[j] = 9;
			int j = i;
			while (j < sz) {
				a[j]--;
				if (a[j] < 0) a[j] += 10;
				else break;
				j++;
			}
		}
	}
	while (a[sz-1] == 0)sz--;
	for (int i = sz-1; i >= 0; i--) cout << a[i];
	cout << endl;
}

int main()
{
	int t;
	cin >> t;
	for (int tt = 1; tt <= t; tt++) {
		cout << "Case #" << tt << ": ";
		solve();
	}
	return 0;
}
