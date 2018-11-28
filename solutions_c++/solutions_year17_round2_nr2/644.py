#include <algorithm>
#include <iostream>
#include <iomanip>
#include <cstdio>
#include <vector>
#include <map>
using namespace std;
#define int long long

vector <int> cnt(3, 0);

char decode(char c) {
	if (c == 0) {
		return 'R';
	}
	if (c == 1) {
		return 'Y';
	}
	return 'B';
}

string check(int num) {
	int a, b;
	if (num	== 0) {
		a = 1; b = 2;
	} else if (num == 1) {
		a = 0; b = 2;
	} else {
		a = 0; b = 1;
	}
	int n = cnt[num];
	vector <string> sep;
	if (cnt[a] == cnt[b]) {
		if (cnt[a] > 0) {
			sep.push_back("");
			for (int i = 0; i < cnt[a]; i++) {
				sep[0].push_back(a);
				sep[0].push_back(b);
			}
		}
	} else {
		if (cnt[a] > cnt[b]) {
			swap(a, b);
		}
		sep.push_back("");
		sep[0].push_back(b);
		for (int i = 0; i < cnt[a]; i++) {
			sep[0].push_back(a);
			sep[0].push_back(b);
		}
		for (int i = 0; i < cnt[b] - cnt[a] - 1; i++) {
			sep.push_back(string(1, b));
		}
	}
	while (sep.size() < n) {
		bool flag = false;
		for (int i = 0; i < sep.size() && sep.size() < n/**/; i++) {
			if (sep[i].size() > 1) {
				flag = true;
				sep.push_back(string(1, sep[i].back()));
				sep[i].pop_back();
			}
		}
		if (!flag) {
			break;
		}
	}
	if (sep.size() == n) {
		string ans = "";
		for (int i = 0; i < n; i++) {
			ans += decode(num);
			for (auto c : sep[i]) {
				ans += decode(c);
			}
		}
		return ans;
	} else {
		return "";
	}
}

void sol() {
	int n;
	int tmp;
	cin >> n;
	cin >> cnt[0] >> tmp >> cnt[1] >> tmp >> cnt[2] >> tmp;
	for (int i = 0; i < 3; i++) {
		if (cnt[i] > 0) {
			string ans = check(i);
			if (ans.size() == n) {
				cout << ans << endl;
				return;
			}
		}
	}
	cout << "IMPOSSIBLE" << endl;
}

signed main() {
	freopen("input.txt", "r", stdin);
	freopen("output.txt", "w", stdout);

	int t;
	cin >> t;
	for (int i = 0; i < t; i++) {
		cout << "Case #" << i + 1 << ": ";
		sol();
	}

	fclose(stdin);
	fclose(stdout);
}