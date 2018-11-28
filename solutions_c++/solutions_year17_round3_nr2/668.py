#include <iostream>
#include <iomanip>
#include <cmath>
#include <algorithm>
#include <vector>
#include <string>
#include <map>
#include <set>
#include <cassert>
#include <cstdlib>
#include <climits>

using namespace std;

typedef long long ll;
typedef unsigned long long ull;

template <typename T> using V = vector<T>;
typedef vector<int> VI;
typedef vector<VI> VVI;
typedef pair<int, int> Pii;

const double Pi = acos(-1.0);

#define forn(i, n) for (int i = 0; i < int(n); i++)
#define ford(i, n) for (int i = int(n) - 1; i >= 0; i--)
#define fore(i, l, r) for (int i = int(l); i < int(r); i++)
#define correct(x, y, n, m) (0 <= (x) && (x) < (n) && 0 <= (y) && (y) < (m))

int calc(vector<Pii>& v1, vector<Pii>& v2) {
	int st = 
		v1.empty() ? 1 : 
		v2.empty() ? 0 :
		v1[0].first < v2[0].first ? 0 : 1;

	int i = 0, j = 0;
	int cur = st;

	int res = 0;

	while (i < v1.size() || j < v2.size()) {
		if (cur == 0) {
			int i1 = (i + 1) % v1.size();
			int s1 = i + 1 == v1.size() ? v1[i1].first + 24 * 60 : v1[i1].first;

			int j0 = v2.empty() ? - 1 : j % v2.size();
			int s2 = v2.empty() ? INT_MAX :
				j == v2.size() ? v2[j0].first + 24 * 60 : v2[j0].first;

			if (v1[i].second == s1) {
				++i;
			}
			else if (s1 < s2) {
				res += 2;
				++i;
			}
			else {
				++res;
				cur = 1;
				++i;
			}
		}
		else {
			int j1 = (j + 1) % v2.size();
			int s2 = j1 == 0 ? v2[j1].first + 24 * 60 : v2[j1].first;

			int i0 = v1.empty() ? -1 : i % v1.size();
			int s1 = v1.empty() ? INT_MAX :
				i == v1.size() ? v1[i0].first + 24 * 60 : v1[i0].first;

			if (v2[j].second == s2) {
				++j;
			}
			else if (s2 < s1) {
				res += 2;
				++j;
			}
			else {
				++res;
				cur = 0;
				++j;
			}
		}
	}

	return res;
}

void solve() {
	int n1, n2;
	cin >> n1 >> n2;
	V<pair<int, int>> v1(n1), v2(n2);
	int t1 = 12 * 60, t2 = 12 * 60;
	forn(i, n1) {
		cin >> v1[i].first >> v1[i].second; 
		t2 -= v1[i].second - v1[i].first;
	}
	forn(i, n2) {
		cin >> v2[i].first >> v2[i].second;
		t1 -= v2[i].second - v2[i].first;
	}
	sort(v1.begin(), v1.end());
	sort(v2.begin(), v2.end());

	int st =
		v1.empty() ? 1 :
		v2.empty() ? 0 :
		v1[0].first < v2[0].first ? 0 : 1;

	int i = 0, j = 0;
	int cur = st;

	int res = 0;
	vector<int> g1, g2;

	while (i < v1.size() || j < v2.size()) {
		if (cur == 0) {
			int i1 = (i + 1) % v1.size();
			int s1 = i + 1 == v1.size() ? v1[i1].first + 24 * 60 : v1[i1].first;

			int j0 = v2.empty() ? -1 : j % v2.size();
			int s2 = v2.empty() ? INT_MAX :
				j == v2.size() ? v2[j0].first + 24 * 60 : v2[j0].first;

			if (v1[i].second == s1) {
				++i;
			}
			else if (s1 < s2) {
				res += 2;
				g2.push_back(s1 - v1[i].second);
				++i;
			}
			else {
				++res;
				cur = 1;
				++i;
			}
		}
		else {
			int j1 = (j + 1) % v2.size();
			int s2 = j1 == 0 ? v2[j1].first + 24 * 60 : v2[j1].first;

			int i0 = v1.empty() ? -1 : i % v1.size();
			int s1 = v1.empty() ? INT_MAX :
				i == v1.size() ? v1[i0].first + 24 * 60 : v1[i0].first;

			if (v2[j].second == s2) {
				++j;
			}
			else if (s2 < s1) {
				res += 2;
				g1.push_back(s2 - v2[j].second);
				++j;
			}
			else {
				++res;
				cur = 0;
				++j;
			}
		}
	}

	sort(g1.begin(), g1.end());
	sort(g2.begin(), g2.end());
	for (int c : g1) {
		if (t1 < c) break;

		res -= 2, t1 -= c;
		assert(res >= 0);
	}

	for (int c : g2) {
		if (t2 < c) break;

		res -= 2, t2 -= c;
		assert(res >= 0);
	}



	cout << res << endl;
}

int main() {
	ios_base::sync_with_stdio(false), cin.tie(NULL);
	
	int T; cin >> T;
	forn(tc, T) {
		cout << "Case #" << tc + 1 << ": ";
		solve();
	}
}