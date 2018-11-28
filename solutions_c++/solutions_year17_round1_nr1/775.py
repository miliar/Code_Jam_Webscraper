#pragma warning (disable:4996)

#include <cstdio>
#include <cstdlib>
#include <ctime>
#include <cmath>
#include <climits>
#include <cstring>
#include <iostream>
#include <algorithm>
#include <vector>
#include <stack>
#include <queue>
#include <string>
#include <set>
#include <map>
#include <unordered_map>

using namespace std;

typedef long long ll;
typedef vector<int> vi;

////

// B
bool cmp(const pair<int, int> &a, const pair<int, int> &b) {
	if (a.second == b.second) return a.first > b.first;
	return a.second > b.second;
}

int main() {
	freopen("A-large.in", "r", stdin);
	freopen("A-l.out", "w", stdout);

	int t, cas = 1;
	cin >> t;
	while (t--) {
		int r, c;
		cin >> r >> c;
		vector<string> mp(r);
		for (int i = 0; i < r; i++) cin >> mp[i];
		int rd = -1;
		for (int i = 0; i < r; i++) {
			int j;
			for (j = 0; j < c; j++) {
				if (mp[i][j] != '?') break;
			}
			if (j < c) {
				rd = i;
				break;
			}
		}
		for (int i = rd; i < r; i++) {
			int j;
			for (j = 0; j < c; j++) {
				if (mp[i][j] != '?') break;
			}
			if (j < c) {
				for (int k = 0; k < j; k++) {
					mp[i][k] = mp[i][j];
				}
				for (int k = j + 1; k < c; k++) {
					if (mp[i][k] == '?') mp[i][k] = mp[i][j];
					else j = k;
				}
			}
			else {
				for (int k = 0; k < c; k++) {
					mp[i][k] = mp[i - 1][k];
				}
			}

		}
		for (int k = 0; k < rd; k++) {
			for (int l = 0; l < c; l++) {
				mp[k][l] = mp[rd][l];
			}
		}
		cout << "Case #" << cas++ << ": \n";
		for (int i = 0; i < r; i++){
			cout << mp[i] << endl;
		}
	}
	return 0;
}

//int main() {
//	freopen("B-large.in", "r", stdin);
//	freopen("B-l.out", "w", stdout);
//
//	int t, cas = 1;
//	cin >> t;
//	while (t--) {
//		int n, p;
//		cin >> n >> p;
//		vi ing(n);
//		for (int i = 0; i < n; i++) cin >> ing[i];
//		vector< vi > pck(n, vi(p));
//		vector< vector< pair<int, int> > > kit(n, vector< pair<int, int> >(p));
//		for (int i = 0; i < n; i++) {
//			for (int j = 0; j < p; j++) {
//				cin >> pck[i][j];
//				kit[i][j].first = ceil(1.0 * pck[i][j] / 1.1 / ing[i]);
//				kit[i][j].second = floor(1.0 * pck[i][j] / 0.9 / ing[i]);
//				if (kit[i][j].first > kit[i][j].second) {
//					kit[i][j].first = -1;
//					kit[i][j].second = -1;
//				}
//			}
//			sort(kit[i].begin(), kit[i].end(), cmp);
//		}
//		int ans = 0;
//		vi cnt(n, 0);
//		for (;;) {
//			int flg = 0;
//			int mxmn = -1, mnmx = 1000005;
//			for (int i = 0; i < n; i++)
//			{
//				if (cnt[i] >= p) {
//					flg = 1;
//					break;
//				}
//				mxmn = max(kit[i][cnt[i]].first, mxmn);
//				mnmx = min(kit[i][cnt[i]].second, mnmx);
//			}
//			if (flg || mnmx <= 0) break;
//			if (mxmn <= mnmx) {
//				ans++;
//				for (int i = 0; i < n; i++) {
//					cnt[i]++;
//				}
//			}
//			else {
//				for (int i = 0; i < n; i++) {
//					if (kit[i][cnt[i]].first > mnmx) cnt[i]++;
//				}
//			}
//
//		}
//		cout << "Case #" << cas++ << ": " << ans << endl;
//	}
//	return 0;
//}