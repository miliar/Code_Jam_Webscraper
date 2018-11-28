#include <iostream>
#include <cstdio>
#include <string>
#include <vector>
#include <algorithm>
#include <queue>
#include <set>
#include <map>

using namespace std;

int main() {
	int T;
	cin >> T;
	for (int t = 1; t <= T; t++) {
		long long N, K;

		cin >> N >> K;

		map<long long, long long> mp;

		mp[-N] = 1;

		long long cnt = 1;
		long long cntBefore = 0;

		while (cnt < K) {
			cntBefore = cnt;

			vector<pair<long long, long long> > v;
			for (map<long long, long long>::iterator it = mp.begin(); it != mp.end(); it++) {
				v.push_back(make_pair(-(it->first), it->second));
			}
			mp.clear();

			for (int i = 0; i < v.size(); i++) {
				long long v1 = v[i].first / 2;
				long long v2 = ((v[i].first + 1) / 2) - 1;
				if (v[i].first == 0)
					v1 = 0, v2 = 0;

				if (!mp.count(-v1))
					mp[-v1] = 0;
				mp[-v1] += v[i].second;

				if (!mp.count(-v2))
					mp[-v2] = 0;
				mp[-v2] += v[i].second;


				cnt += 2 * v[i].second;
			}
		}

		long long cntLastState = cntBefore;
		long long val = -1;

		for (map<long long, long long>::iterator it = mp.begin(); it != mp.end(); it++) {
			if (cntLastState + it->second >= K) {
				val = - it->first;
				break;
			}
			cntLastState += it->second;
		}

		printf("Case #%d: %lld %lld\n", t, val / 2, (val + 1) / 2 - 1);
	}
	return 0;
}