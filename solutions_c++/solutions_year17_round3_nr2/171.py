#include <iostream>
#include <stdio.h>
#include <vector>
#include <string>
#include <math.h>
#include <algorithm>
#include <map>
#include <set>
#include <set>

#define sz(x) ((int)x.size())
#define all(x) (x).begin(), (x).end()
#define pb(x) push_back(x)
#define mp(x, y) make_pair(x, y)

typedef long long int64;

using namespace std;

void solve() {
	int n = 24 * 60;
	int n1, n2;
	cin >> n1 >> n2;
	vector<int> position(n, 0);
	for (int i = 0; i < n1; ++i) {
		int x, y;
		cin >> x >> y;
		for (int t = x; t < y; ++t) position[t] = 1;
	}
	for (int i = 0; i < n2; ++i) {
		int x, y;
		cin >> x >> y;
		for (int t = x; t < y; ++t) position[t] = 2;
	}
	int inf = 1000000;
	int k = n / 2;
	int ans = inf;
	for (int start = 1; start <= 2; ++start) {
		vector<vector<int>> dp1(k + 1, vector<int>(k + 1, inf)), dp2(k + 1, vector<int>(k + 1, inf));
		if (start == 1) {
			dp1[0][0] = 0;
		} else {
			dp2[0][0] = 0;
		}
		for (int i = 0; i <= k; ++i) {
			for (int j = 0; j <= k; ++j) {
				if (i == 0 && j == 0) continue;
				int l = i + j - 1;
				if (position[l] != 1 && j > 0) {
					dp2[i][j] = min(dp2[i][j], dp1[i][j - 1] + 1);
					dp2[i][j] = min(dp2[i][j], dp2[i][j - 1]);
				}
				if (position[l] != 2 && i > 0) {
					dp1[i][j] = min(dp1[i][j], dp2[i - 1][j] + 1);
					dp1[i][j] = min(dp1[i][j], dp1[i - 1][j]);
				}
			}
		}
		if (start == 1) {
		    ans = min(ans, dp1[k][k]);
			ans = min(ans, dp2[k][k] + 1);
		} else {
		    ans = min(ans, dp1[k][k] + 1);
			ans = min(ans, dp2[k][k]);	
		}
			
	}
	cout << ans << endl;
}

int main() {
    int tests;
    cin >> tests;
    for (int test = 1; test <= tests; ++test) {
        cout << "Case #" << test << ": ";
        solve();
    }
    return 0;
}
