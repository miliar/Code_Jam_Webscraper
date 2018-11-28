#include <iostream>
#include <vector>
#include <cmath>
#include <queue>
#include <set>

using namespace std;
typedef pair<int,int> pii;

int n,p,T;
int need[55];
vector<pii> makes[55];
int ind[55];

int main() {
	ios::sync_with_stdio(0);
	cin >> T;
	for(int t = 1; t <= T; ++t) {
		cout << "Case #" << t << ": ";
		cin >> n >> p;
		for(int i = 0; i < n; ++i)
			cin >> need[i];
		for(int i = 0; i < n; ++i) {
			makes[i].clear();
			for(int j = 0; j < p; ++j) {
				int d = need[i];
				int k;
				cin >> k;
				int lo = ceil(10.0*k/(11.0*d));
				int hi = floor(10.0*k /(9.0*d));
				if(hi >= lo) {
					makes[i].push_back(pii(lo,hi));
				}
			}
			sort(makes[i].begin(),makes[i].end());
			ind[i] = 0;
		}
		bool ok = true;
		for(int i = 0; i < n; ++i) {
			ok &= makes[i].size() != 0;
		}
		if(!ok) {
			cout << "0\n";
			continue;
		}
		int ans = 0;
		while(1) {
			int mn = 0;
			int mx = 0;
			for(int i = 1; i < n; ++i) {
				if(makes[i][ind[i]].first > makes[mx][ind[mx]].first)
					mx = i;
				if(makes[i][ind[i]].second < makes[mn][ind[mn]].second)
					mn = i;
			}
			if(makes[mx][ind[mx]].first <= makes[mn][ind[mn]].second) {
				++ans;
				bool ok = true;
				for(int i = 0; i < n; ++i) {
					if(++ind[i] == makes[i].size())
						ok = false;
				}
				if(!ok) break;
			} else {
				if(++ind[mn] == makes[mn].size())
					break;
			}
		}
		cout << ans << endl;
	}
	return 0;
}