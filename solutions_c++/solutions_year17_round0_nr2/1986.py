#include <bits/stdc++.h>
#define LL long long
using namespace std;

const int MAXN = 1e3 + 10;
LL n;
LL ans[MAXN];
set<LL> spec;

string toString(LL n) {
	string res;
	while(n > 0) {
		res.push_back('0' + (n % 10));
		n /= 10;
	}
	reverse(res.begin(), res.end());
	return res;
}
LL toLL(string s) {
	LL res = 0;
	for(int i = 0; i < s.size(); i++) {
		res = (res * 10) + s[i] - '0';
	}
	return res;
}

string __solve(int idx, string s, bool tight) {
	if(idx + 1 == s.size()) {
		if(!tight) s.back() = '9';
		return s;
	}
	if(!tight) {
		s[idx] = '9';
		return __solve(idx + 1, s, tight);
	}
	if(s[idx + 1] < s[idx]) {
		if(idx > 0 && s[idx] - 1 < s[idx-1]) {
			return "-1";
		} else {
			s[idx]--;
			return __solve(idx + 1, s, false);
		}
	}
	string res = __solve(idx + 1, s, true);
	if(res == "-1") {
		if(s[idx] == '0') return "-1";
		else if(idx > 0 && s[idx] - 1 < s[idx-1]) {
			return "-1";
		} else {
			s[idx]--;
			return __solve(idx + 1, s, false);
		}
	}
	return res;
}

LL solve(LL n) {
	string s = toString(n);
	s = __solve(0, s, true);
	assert(s != "-1");
	return toLL(s);
}
bool is_tidy(LL n) {
	vector<int> digs;
	while(n > 0) {
		digs.push_back(n % 10);
		n /= 10;
	}
	reverse(digs.begin(), digs.end());
	int last = digs[0];
	for(int i = 1; i < digs.size(); i++) {
		if(digs[i] < last) return false;
		last = digs[i];
	}
	return true;
}

void checker() {
	ans[1] = 1;
	for(int i = 2; i < MAXN; i++) {
		if(is_tidy(i)) {
			ans[i] = i;
		} else ans[i] = ans[i-1];
	}
}

int main() {
	ios_base::sync_with_stdio(false);
	checker();
	LL ten = 1;
	for(LL i = 1; i <= 18; i++) {
		ten *= 10;
		spec.insert(ten);
	}
	int t;
	for(int i = 1; i < MAXN; i++) {
		if(ans[i] != solve(i)) cerr << "Failing at: " << i << ' ' << ans[i] << ' ' << solve(i) << endl;
		assert(ans[i] == solve(i));
	}
	cin >> t;
	for(int tc = 1; tc <= t; tc++) {
		cout << "Case #" << tc << ": ";
		cin >> n;
		cout << solve(n) << '\n';
	}
	return 0;
}
