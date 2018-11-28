#include <bits/stdc++.h>
using namespace std;
#if defined(ILIKEGENTOO)
void E(){}template<class A,class...B>void E(A _,B...$){cerr<<' '<<_;E($...);}
#define E($...) E(#$,'=',$,'\n')
#else
#define E($...) ;
#endif
#define all(x) begin(x), end(x)
struct ${$(){ios_base::sync_with_stdio(false);cin.tie(nullptr);}}$;

void solve() {
	int n, p;
	cin >> n >> p;
	vector<int> r(n);
	for (auto &rr: r)
		cin >> rr;
	vector<vector<int>> q(n, vector<int>(p));
	for (auto &qa: q)
		for (auto &qb: qa)
			cin >> qb;
	vector<vector<pair<int, int>>> d;
	int qi = 0;
	for (const auto &qa: q) {
		vector<pair<int, int>> da;
		int rr = r[qi];
		++qi;
		for (int qb: qa) {
			pair<int, int> z;
			z.first = (10 * qb + 11 * rr - 1) / (11 * rr);
			z.second = (10 * qb) / (9 * rr);
			if (z.first > z.second) continue;
			assert(z.first > 0);
			da.emplace_back(move(z));
		}
		sort(all(da));
		d.emplace_back(move(da));
	}
	int ans = 0;
	vector<size_t> inds(n);
	while (true) {
		int mn = -1;
		for (int i = 0; i < n; ++i) {
			size_t ind = inds[i];
			if (ind >= d[i].size()) {
				mn = -1;
				break;
			}
			mn = max(mn, d[i][ind].first);
		}
		if (mn < 0) break;
		int bad = -1;
		for (int i = 0; i < n; ++i) {
			size_t ind = inds[i];
			if (mn > d[i][ind].second) bad = i;
		}
		if (bad >= 0) {
			++inds[bad];
			continue;
		}
		++ans;
		for (int i = 0; i < n; ++i)
			++inds[i];
	}
	cout << ans << '\n';
}

int main() {
	int tc;
	cin >> tc;
	for (int ti = 1; ti <= tc; ++ti) {
		cout << "Case #" << ti << ": ";
		solve();
	}
	return 0;
}
