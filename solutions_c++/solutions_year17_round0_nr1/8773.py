#include <bits/stdc++.h>
typedef long long ll;
using namespace std;

unsigned int dp[1<<11];
unsigned int win;
unsigned int waffler;
unsigned int width;
unsigned int k;

#define INF ((ll)1e8)

unsigned int f(ll m) {
	if (dp[m] != -1)
		return dp[m];

	if (m == win)
		return 0;

	auto &r = dp[m];
	r = INF;

	unsigned int rtmp = INF;
	for (int i = 0; i < width-k+1; i++) {
		unsigned int wafflerpos = waffler << i;
		rtmp = min(rtmp, 1+f(m^wafflerpos));
	}
	r = rtmp;

	return r;
}

ll proc()
{
	string line;
	cin >> line >> k;

	waffler = (1ULL<<k)-1;
	width = line.length();
	win = (1ULL<<width)-1;
	ll mask = 0;
	for (int i = 0; i < line.size(); i++) {
		if (line[i] == '+')
			mask |= (1ULL<<i);
	}
	memset(dp, -1, sizeof(dp));

	return f(mask);
}

int main()
{
	ll T;
	cin >> T;
	for (int i = 1; i <= T; i++) {
		ll res = proc();
		cout << "Case #" << i << ": ";
		if (res==INF) cout << "IMPOSSIBLE" << endl;
		else cout << res << endl;
	}
}
