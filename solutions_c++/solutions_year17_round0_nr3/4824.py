#define _CRT_SECURE_NO_WARNINGS
#include <iostream>
#include <vector>
#include <stdio.h>
#include <set>
#include <algorithm>
#include <string.h>
#include <assert.h>
#include <time.h>
#include <string>
#include <queue>
#include <random> 
#include <map>
#include <numeric>
using namespace std;
typedef long long li;
#define mp make_pair
#define sz(a) (int)a.size()

void solve() {
	int tests;
	cin >> tests;
	for (int t = 0; t < tests; t++){
		int n, k;
		cin >> n >> k;

		map<int, set<int>> s;
		s[n].insert(1);

		int ans1 = 0, ans2 = 0;
		for (int i = 0; i < k; i++) {

			map<int, set<int>>::iterator it = s.begin();

			int l = 1e9, r = 1e9, mid = 1e9, len = 1e9;

			ans1 = -1;
			ans2 = -1;

			{
				int l1 = (*(it->second).begin());
				int len1 = it->first;

				int r1 = l1 + len1 - 1;
				int mid1 = (l1 + (r1 - l1) / 2);
				int ans11 = min(mid1 - l1, r1 - mid1);
				int ans12 = max(mid1 - l1, r1 - mid1);

				if (ans11 > ans1 || (ans11 == ans1 && ans12 > ans2) ||
					(ans11 == ans1 && ans12 == ans2 && l1 < l)) {
					l = l1, r = r1, mid = mid1, ans1 = ans11, ans2 = ans12;
					len = len1;
				}
			}

			
			if (s.size() > 1) {
				it++;
				int l1 = (*(it->second).begin());
				int len1 = it->first;

				int r1 = l1 + len1 - 1;
				int mid1 = (l1 + (r1 - l1) / 2);
				int ans11 = min(mid1 - l1, r1 - mid1);
				int ans12 = max(mid1 - l1, r1 - mid1);

				if (ans11 > ans1 || (ans11 == ans1 && ans12 > ans2) ||
					(ans11 == ans1 && ans12 == ans2 && l1 < l)) {
					l = l1, r = r1, mid = mid1, ans1 = ans11, ans2 = ans12;
					len = len1;
				}
			}
			
			if (s.size() > 2) {
				it++;
				int l1 = (*(it->second).begin());
				int len1 = it->first;

				int r1 = l1 + len1 - 1;
				int mid1 = (l1 + (r1 - l1) / 2);
				int ans11 = min(mid1 - l1, r1 - mid1);
				int ans12 = max(mid1 - l1, r1 - mid1);

				if (ans11 > ans1 || (ans11 == ans1 && ans12 > ans2) ||
					(ans11 == ans1 && ans12 == ans2 && l1 < l)) {
					l = l1, r = r1, mid = mid1, ans1 = ans11, ans2 = ans12;
					len = len1;
				}
			}

			if (s.size() > 3) {
				it++;
				int l1 = (*(it->second).begin());
				int len1 = it->first;

				int r1 = l1 + len1 - 1;
				int mid1 = (l1 + (r1 - l1) / 2);
				int ans11 = min(mid1 - l1, r1 - mid1);
				int ans12 = max(mid1 - l1, r1 - mid1);

				if (ans11 > ans1 || (ans11 == ans1 && ans12 > ans2) ||
					(ans11 == ans1 && ans12 == ans2 && l1 < l)) {
					l = l1, r = r1, mid = mid1, ans1 = ans11, ans2 = ans12;
					len = len1;
				}
			}


			s[len].erase(l);

			if (s[len].empty()) {
				s.erase(len);
			}

			if (mid - l > 0) {
				s[mid - l].insert(l);
			}
			if (r - mid > 0) {
				s[r - mid].insert(mid + 1);
			}
		}
		cout << "Case #" << t + 1 << ": " << ans2 << " " << ans1 << endl;
	}
}

int main() {
	freopen("C-small-2-attempt0.in", "r", stdin);
	freopen("output.txt", "w", stdout);
	cout.sync_with_stdio(false);
	cin.tie(0);
	srand(time(NULL));
	solve();
	return 0;
}