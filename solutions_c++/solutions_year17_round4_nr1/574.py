#include <bits/stdc++.h>
using namespace std;

void test() {
	
	int n, p;
	cin >> n >> p;
	vector<int> mods(4);
	for (int i = 0; i < n; ++i) {
		int x;
		cin >> x;
		mods[x%p]++;
	}
	
	map<array<int, 5>, int> dp;
	dp[{0, 0, 0, 0, 0}] = 0;
	for (int i = 0; i < n; ++i) {
		map<array<int, 5>, int> ne;
		
		for (auto pa : dp) {
			array<int, 5> ar = pa.first;
			int maxi = pa.second;
			
			for (int m = 0; m < p; ++m) {
				if (ar[m] < mods[m]) {
					array<int, 5> nxt = ar;
					nxt[m]++;
					nxt[4] = (ar[4] + m) % p;
					
					int val = maxi + (ar[4] == 0 ? 1 : 0);
					
					ne[nxt] = max(ne[nxt], val);
				}
			}
		}
		
		dp = std::move(ne);
	}
	
	int ans = 0;
	for (auto pa : dp)
		ans = max(ans, pa.second);

	cout << ans;
	
}

int main()
{
	int T;
	cin >> T;
	for (int t = 1; t <= T; ++t) {
		cout << "Case #" << t << ": ";
		test();
		cout << endl;
	}
	return 0;
}
