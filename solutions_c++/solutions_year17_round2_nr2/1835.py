#include <iostream>
#include <cstdio>
#include <vector>
#include <algorithm>
#include <utility>
#include <string>
#include <queue>

using namespace std;
using PIC = pair<int, char>;

const string impossible = "IMPOSSIBLE";

string solve() {
	int n, r, o, y, g, b, v;
	cin >> n >> r >> o >> y >> g >> b >> v;

	bool has_bob = false;
	bool has_rgr = false;
	bool has_yvy = false;
	string s_bob;
	string s_rgr;
	string s_yvy;
	for (int i = 0; i < o; i++) {
		s_bob += "BO";
		has_bob = true;
	}
	for (int i = 0; i < g; i++) {
		s_rgr += "RG";
		has_rgr = true;
	}
	for (int i = 0; i < v; i++) {
		s_yvy += "YV";
		has_yvy = true;
	}

	if (has_bob && o == b && n == o + b) {
		return s_bob;
	}
	if (has_rgr && r == g && n == r + g) {
		return s_rgr;
	}
	if (has_yvy && y == v && n == y + v) {
		return s_yvy;
	}

	if (has_bob) {
		s_bob += "B";
		b -= o;
	}
	if (has_rgr) {
		s_rgr += "R";
		r -= g;
	}
	if (has_yvy) {
		s_yvy += "Y";
		y -= v;
	}

	if (b < 0 || r < 0 || y < 0) {
		return impossible;
	}

	vector<PIC> chars;
	chars.push_back(make_pair(b, 'B'));
	chars.push_back(make_pair(r, 'R'));
	chars.push_back(make_pair(y, 'Y'));

	sort(chars.begin(), chars.end());
	int nc0 = chars[0].first;
	int nc1 = chars[1].first;
	int nc2 = chars[2].first;
	int n_common = (nc0 + nc1) - nc2;

	if (nc0 + nc1 < nc2) {
		return impossible;
	}

	string ans = "";
	for (int i = 0; i < nc0 - n_common; i++) {
		ans += chars[2].second;
		ans += chars[0].second;
	}
	for (int i = 0; i < n_common; i++) {
		ans += chars[2].second;
		ans += chars[0].second;
		ans += chars[1].second;
	}
	for (int i = 0; i < nc1 - n_common; i++) {
		ans += chars[2].second;
		ans += chars[1].second;
	}

	if (has_bob) {
		int pos = ans.find('B');
		ans = ans.substr(0, pos) + s_bob + ans.substr(pos+1);
	}
	if (has_rgr) {
		int pos = ans.find('R');
		ans = ans.substr(0, pos) + s_rgr + ans.substr(pos+1);
	}
	if (has_yvy) {
		int pos = ans.find('Y');
		ans = ans.substr(0, pos) + s_yvy + ans.substr(pos+1);
	}

	return ans;
}

int main() {

	int t;

	cin >> t;
	vector<string> ans(t);

	for (int i = 0; i < t; i++) {
		ans[i] = solve();
	}

	for (int i = 0; i < t; i++) {
		printf("Case #%d: %s\n", i + 1, ans[i].c_str());
	}
	return 0;
}
