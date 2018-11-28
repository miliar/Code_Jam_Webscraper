#include <bits/stdc++.h>

using namespace std;

void ans(double a) {
	static int n = 1;
	//~ cout << "Case #" << n++ << ": " << a << '\n';
	printf("Case #%d: %.12f\n", n++, a);
}

void solve(long long rem) {
	
}

int main() { ios_base::sync_with_stdio(false);
	
	freopen("/d/input", "r", stdin);
	freopen("/d/aa", "w", stdout);
	
	
	
	int T; cin >> T;
	for (int q = 0; q < T; q++) {
		int D, n;
		cin >> D >> n;
		
		pair<int, int> arr[n];
		for (int i = 0; i < n; i++) {
			cin >> arr[i].first >> arr[i].second;
		}
		
		sort(arr, arr + n);
		reverse(arr, arr + n);
		
		double mn = 0;
		
		for (int j = 0; j < n; j++) {
			double tm = ((1.0 * D) - arr[j].first) / arr[j].second;
			mn = max(mn, tm);
		}
		
		ans(D / mn);
		
		
	}
	
	
	return 0;
}
