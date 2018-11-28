#include <bits/stdc++.h>

using namespace std;

long long mn = LLONG_MAX, mx = LLONG_MAX;

void ans(long long a, long long b) {
	static int n = 1;
	cout << "Case #" << n++ << ": " << a << ' ' << b << '\n';
}

map<long long, long long> M;
set<long long> S;

void solve(long long rem) {
	if (rem == 0) return;
	long long largest = *(--S.end());
	//~ cout << largest << endl;
	long long k = min(rem, M[largest]);
	rem -= k;
	// cout << "#" << k << endl;
	long long total = largest - 1;
	long long lh = total / 2;
	long long hh = total - lh;
	mx = min(mx, hh);
	mn = min(mx, lh);
	M[lh] += k;
	M[hh] += k;
	S.insert(lh);
	S.insert(hh);
	M[largest] -= k;
	if (!M[largest]) S.erase(largest);
	solve(rem);
}

int main() { ios_base::sync_with_stdio(false);
	int T; cin >> T;
	for (int q = 0; q < T; q++) {
		long long n, k;
		cin >> n >> k;
		mn = mx = LLONG_MAX;
		M.clear();
		M[n]++;
		S.insert(n);
		solve(k);
		ans(mx, mn);
	}
	
	return 0;
}
