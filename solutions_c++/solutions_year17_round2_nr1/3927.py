#include <iostream>
#include <algorithm>
#include <cstdio>
#include <cstdlib>
#include <cstring>
#include <cmath>
#include <vector>
#include <string>
#include <fstream>
#include <iomanip>

#define IN_FILE "A-small-attempt0.in"
#define OUT_FILE "out.txt"

using namespace std;

typedef long long ll;
typedef long double ld;

pair<ll, ll> h[1003];
ld dp[1003];

int main() {
	ios::sync_with_stdio(0);
	cout << fixed << setprecision(7);
	ifstream xin(IN_FILE);
	ofstream xout(OUT_FILE);
	cin.rdbuf(xin.rdbuf());
	cout.rdbuf(xout.rdbuf());
	int t;
	int tc = 1;
	cin >> t;
	while (t--) {
		ll d, n;
		cin >> d >> n;
		for (ll i = 0; i < n; i++)
			cin >> h[i].first >> h[i].second;
		sort(h, h + n);
		dp[n - 1] = ((ld)(d - h[n-1].first)) / (h[n-1].second);
		for (ll i = n - 2; i >= 0; i--) {
			ld spd = ((ld)(d - h[i].first)) / (h[i].second);
			if(h[i].second<=h[i+1].second)
				dp[i] = spd;
			else {
				ll bw = h[i + 1].first - h[i].first;
				ld dist = ((ld)(h[i].second*bw)) / (h[i].second - h[i + 1].second);
				ld rdist = h[i].first + dist;
				if (rdist < d)
					dp[i] = dp[i + 1];
				else
					dp[i] = spd;
			}
		}
		ld ans = d/dp[0];
		cout << "Case #" << tc << ": " << ans << "\n";
		tc++;
	}
	system("pause");
	return 0;
}
