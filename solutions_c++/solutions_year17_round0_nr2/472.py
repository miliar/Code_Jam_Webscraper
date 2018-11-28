#include <bits/stdc++.h>

using namespace std;

map<pair<int, int>, int64_t> DP1;
map<tuple<int, int, int>, int64_t> DP2;

int64_t tidy(int len, int last) {
	if (len == 0)
		return 1;
	auto key = make_pair(len, last);
	if (DP1.count(key))
		return DP1[key];
	int64_t ans = 0;
	for (int next = 0; next < 10; ++next) if (next >= last) {
		ans += tidy(len-1, next);
	}
	return DP1[key] = ans;
}


vector<int> NUM;

int64_t tidy(int i, int last, bool lt) {
	if (i == NUM.size())
		return 1;
	auto key = make_tuple(i, last, lt);
	if (DP2.count(key))
		return DP2[key];
	int64_t ans = 0;
	for (int next = 0; next < 10; ++next) if (next >= last) {
		if (!lt && next > NUM[i])
			continue;
		ans += tidy(i+1, next, lt || next < NUM[i]);
	}
	return DP2[key] = ans;
}

int64_t count(const string &s) {
	DP1.clear();
	DP2.clear();
	NUM = vector<int>(s.size());
	for (int i = 0; i < NUM.size(); ++i) {
		NUM[i] = s[i]-'0';
	}
	int64_t cnt = 0;
	for (int sz = 1; sz < NUM.size(); ++sz) {
		cnt += tidy(sz, 1);
	}
	cnt += tidy(0, 1, 0);
	return cnt;
}

void solve() {
	int64_t N;
	cin >> N;
	string s = to_string(N);
	if (is_sorted(s.begin(), s.end())) {
		cout << s << endl;
		return;
	}

	int64_t target = count(s);

	int64_t lo = 0, hi = N;
	while (lo < hi) {
		int64_t mid = (lo+hi)/2;

		string s = to_string(mid);
		int64_t cnt = count(s);


		if (cnt < target) {
			lo = mid+1;
		} else {
			hi = mid;
		}

	}

	cout << lo << endl;

}

int main() {
	ios::sync_with_stdio(0);
	cin.tie(0);
	int T;
	cin >> T;
	for (int t = 0; t < T; ++t) {
		cout << "Case #" << (t+1) << ": ";
		solve();
	}
}