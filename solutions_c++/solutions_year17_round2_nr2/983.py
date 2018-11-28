#include <bits/stdc++.h>

using namespace std;

int R, Y, B, V, O, G, n;

vector<string> rs, ys, bs;

string fail() {
	return "IMPOSSIBLE";
}

string concate() {
	return "";
}

bool solve(vector<string> &bs, int O, char Oc) {
	while (O) {
		if (bs.size() == 0) return false;
		if (bs.size() == 1) {
			// cout << n << " " << bs.size() << " " << O << endl;
			if (n == bs.size() + O) {
				bs.back() += Oc;
				n--;
				return true;
			} else {
				return false;
			}
		} else {
			string aa = bs.back();
			bs.pop_back();
			string bb = bs.back();
			bs.back() = aa + Oc + bb;
			n -= 2;
		}
		O--;
	}
	return true;
}

string solve() {
	while (B--) bs.push_back("B");
	if (!solve(bs, O, 'O')) return fail();
	while (Y--) ys.push_back("Y");
	if (!solve(ys, V, 'V')) return fail();
	while (R--) rs.push_back("R");
	if (!solve(rs, G, 'G')) return fail();
	// cout << "survive!" << endl;
	if (bs.size() == 1 && bs[0][0] != bs[0].back()) return bs[0];
	if (rs.size() == 1 && rs[0][0] != rs[0].back()) return rs[0];
	if (ys.size() == 1 && ys[0][0] != ys[0].back()) return ys[0];
	if (bs.size() > ys.size()) swap(bs, ys);
	if (bs.size() > rs.size()) swap(bs, rs);
	if (ys.size() > rs.size()) swap(ys, rs);
	string ans = "";
	if (bs.size() + ys.size() >= rs.size()) {
		for (int i = 0; i < rs.size(); i++) {
			ans += rs[i];
			if (bs.size()) {
				ans += bs.back();
				bs.pop_back();
			}
			if (rs.size() - i == ys.size()) {
				ans += ys.back();
				ys.pop_back();
			}
		}
		return ans;
	} else {
		return fail();
	}
}

int main() {
	int test;
	scanf("%d", &test);
	while (test--) {
		static int testCount = 0;
		printf("Case #%d: ", ++testCount);
		rs.clear();
		ys.clear();
		bs.clear();
		scanf("%d %d %d %d %d %d %d", &n, &R, &O, &Y, &G, &B, &V);
		cout << solve() << endl;
	}
	return 0;
}
