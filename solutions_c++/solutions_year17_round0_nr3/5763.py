#include <iostream>
#include <cstdlib>
#include <cstdio>

using namespace std;

void solve(long long n, long long k) {
	int a[2000000]={0};
	long long mx2, mx, sl, sr;
	a[0] = a[n+1] = 1;
	int id;
	while (k--) {
		mx2 = 0, mx = 0;
		id = 0;
		for (int i = 1; i <= n; i++) {
			if (a[i]) continue;
			sl = sr = 0;
			while (a[i-1-sl] == 0) sl++;
			while (a[i+1+sr] == 0) sr++;
			if (min(sl,sr) > mx || (min(sl,sr) == mx && max(sl,sr) > mx2)) mx = min(sl,sr), mx2 = max(sl,sr), id = i;
		}
		a[id] = 1;
	}
	cout << mx2 << " " << mx << endl;
	//cout << mx << " " << mx2 << " " << id << endl;
}

void test() {
	int n = 1000;
	for (int k = 1; k <= n; k++) {
		//cout << n << " " << k << " => ";
		solve(n,k);
	}

	exit(0);
}

int main()
{
	//test();

	int t;
	cin >> t;
	for (int tt = 1; tt <= t; tt++) {
		cout << "Case #" << tt << ": ";
		long long n, k;
		cin >> n >> k;
		solve(n,k);
	}
	return 0;
}
