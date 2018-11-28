#define _CRT_SECURE_NO_WARNINGS
#include <iostream>
#include<iomanip>
#include <cassert>
#include<algorithm>
#include <map>
#include<string>
#include<vector>
#include<set>
#include <queue>
using namespace std;

#define forn(i, n) for(int i = 0; i < int(n); ++i)
#define sz(a) int(a.size())
#define mp make_pair
typedef long long li;
const int INF = 1e9;

li toLI(string s) {
	li ans = 0;
	for (int i = 0; i < s.length(); i++) {
		ans *= 10LL;
		ans += (s[i] - '0');
	}
	return ans;
}
void solve() {
	int tests;
	cin >> tests;
	for (int t = 0; t < tests; t++) {
		int n, k;
		cin >> n >> k;
		map<int, set<int>> v;
		int ans1, ans2;
		v[n].insert(1);
		for (int i = 0; i < k; i++) {
			ans1 = -1;
			ans2 = -1;
			int l = INF;
			map<int, set<int>>::iterator it = v.begin();
			int len = -1;
			for (int j = 0; j < 4 && it != v.end(); j++) {
				int tlen = it->first;;
				int tl = *it->second.begin();
				int tr = tl + tlen - 1;
				int point = (tl + tr) / 2;
				int tans1 = point - tl;
				int tans2 = -point + tr;
				if (ans1 < min(tans1, tans2)) {
					ans1 = min(tans1, tans2);
					ans2 = max(tans2, tans1);
					len = tlen;
					l = tl;
				}
				if (ans1 == min(tans1, tans2) && ans2 < max(tans2, tans1)) {
					ans1 = min(tans1, tans2);
					ans2 = max(tans2, tans1);
					len = tlen;
					l = tl;
				}
				if (ans1 == min(tans1, tans2) && ans2 == max(tans2, tans1) && l > tl) {
					ans1 = min(tans1, tans2);
					ans2 = max(tans2, tans1);
					len = tlen;
					l = tl;
				}
				it++;
			}
			v[len].erase(l);
			if (v[len].empty()) {
				v.erase(len);
			}
			int r = l + len - 1;
			int point = (l + r) / 2;
			if (point - l > 0) {
				v[point - l].insert(l);
			}
			if (r - point > 0) {
				v[r - point].insert(point + 1);
			}
		}
		cout << "Case #" << t +1<< ": " << ans2 << " " << ans1 << endl;
	}
}

int main() {
	cout << setprecision(15) << fixed;
	freopen("input.txt", "r", stdin);
	freopen("output.txt", "w", stdout);


	solve();

	return 0;
}