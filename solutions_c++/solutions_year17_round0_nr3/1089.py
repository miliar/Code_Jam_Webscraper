#include <bits/stdc++.h>
using namespace std;

#ifdef HELTHAZAR
	#define DEBUG true
#else
	#define DEBUG false
#endif

#define dout if (DEBUG) cout

void solve() {
	long long n, k;
	cin >> n >> k;

	map<long long, long long> mp;
	mp[n] = 1;
	long long cnt = 0;

	while (cnt < k) {
		long long cur = mp.rbegin()->first;
		long long curCnt = mp.rbegin()->second;

		long long minLR = (cur - 1) / 2;
		long long maxLR = cur - 1 - minLR;

		cnt += curCnt;
		if (cnt >= k) {
			cout << maxLR << " " << minLR;
			return;
		}

		mp.erase(cur);
		mp[minLR] += curCnt;
		mp[maxLR] += curCnt;
	}
}

int main() {
	int test;
	cin >> test;
	for (int t = 1; t <= test; t++) {
		//printf("Case #%d: ", t);
		cout << "Case #" << t << ": ";
		solve();
		cout << endl;
		//printf("\n");
	}
}
