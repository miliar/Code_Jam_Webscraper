#include <iostream>
#include <vector>
#include <algorithm>
#include <cmath>
#include <cstdio>

using namespace std;

typedef pair<int, int> P;
typedef pair<P, int> Q;

int main() {
	int t;
	cin >> t;
	for (int i = 0; i < t; i++) {
		int ac, aj;
		cin >> ac >> aj;
		vector<Q> aa;
		int st, ed;
		int tc, tj;
		tc = tj = 720;
		for (int j = 0; j < ac; j++) {
			cin >> st >> ed;
			tc -= ed - st;
			aa.push_back(Q(P(st, ed), 0));
		}
		for (int j = 0; j < aj; j++) {
			cin >> st >> ed;
			tj -= ed - st;
			aa.push_back(Q(P(st, ed), 1));
		}

		sort(aa.begin(), aa.end());
		vector<int> cc;
		vector<int> jj;
		int ans = 1;
		for (int j = 1; j < aa.size(); j++) {
			ans++;
			if (aa[j].second == aa[j - 1].second) {
				if (aa[j].second == 0) {
					cc.push_back((aa[j].first).first - (aa[j - 1].first).second);
				}
				else {
					jj.push_back((aa[j].first).first-(aa[j-1].first).second);
				}
				ans++;
			}
		}
		int sz = aa.size();

		if (aa[0].second == aa[sz - 1].second) {
			ans++;
			if (aa[0].second == 0) {
				cc.push_back((aa[0].first).first+1440-(aa[sz-1].first).second);
			}
			else {
				jj.push_back((aa[0].first).first+1440-(aa[sz-1].first).second);
			}
		}
		sort(cc.begin(), cc.end());
		sort(jj.begin(), jj.end());
		for (int j = 0; j < cc.size(); j++) {
			if (tc >= cc[j]) {
				tc -= cc[j];
				ans-=2;
			}
		}
		for (int j = 0; j < jj.size(); j++) {
			if (tj >= jj[j]) {
				tj -= jj[j];
				ans -= 2;
			}
		}
		printf("Case #%d: %d\n", i + 1, max(ans, 2));
	}
	return 0;
}