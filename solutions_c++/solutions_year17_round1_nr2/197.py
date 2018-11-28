#include <bits/stdc++.h>

using namespace std;

typedef pair<int,int> ii;

int m, n;

vector < ii > Q[55];
int R[55], cnt[55];

int main() {
	int _T;
	cin >> _T;
	for(int _t = 1; _t <= _T; _t++) {
		cout << "Case #" << _t << ": ";
		cin >> n >> m;
		for(int i=0; i<n; i++)
			cin >> R[i];
		int maxm = 0;
		for(int i=0; i<n; i++) {
			Q[i].clear();
			for(int j=0; j<m; j++) {
				int u;
				cin >> u;
				int l = (u * 100 - 1) / (R[i] * 110) + 1;
				int r = (u * 100) / (R[i] * 90);
				if (l <= r) {
					Q[i].push_back(ii(r, l));
					maxm = max(maxm, r);
				}
				//cout << "%%%" << l << " " << r << endl;
			}
			sort(Q[i].begin(), Q[i].end());
		}
		for(int i=0; i<n; i++)
			cnt[i] = 0;
		int res = 0;
		for(int i=1; i<=maxm; i++) {
			bool flag = 1;
			while (1) {
					for(int j=0; j<n; j++) {
					while (cnt[j] < Q[j].size() && Q[j][cnt[j]].first < i)
						cnt[j]++;
					if (cnt[j] == Q[j].size()) {
						flag = 0;
						break;
					}
					if (Q[j][cnt[j]].second > i) {
						flag = 0;
						break;
					}
				}
				if (flag) {
					res++;
					for(int j=0; j<n; j++)
						cnt[j]++;
				}
				else break;
			}
			
		}
		cout << res << "\n";
	}
	return 0;
}