#include <bits/stdc++.h>

using namespace std;

int main() {
	int tc;

	cin >> tc;

	for (int t = 1; t <= tc; ++t) {
		long long n, k;
		long long mins, maxs;
		priority_queue<long long> mm;

		cin >> n >> k;
		
		long long ls = (n-1)/2;
		long long rs = n/2;
		mins = ls < rs ? ls : rs;
		maxs = ls > rs ? ls : rs;
		mm.push(maxs);
		mm.push(mins);

		for (int i = 2; i <= k && (maxs or mins); ++i) {
			maxs = mm.top()/2;
			mins = (mm.top()-1)/2;
			mm.pop();

			mm.push(maxs);
			mm.push(mins);
		}

		cout << "Case #" << t << ": " << maxs << ' ' << mins << '\n';
	}
}