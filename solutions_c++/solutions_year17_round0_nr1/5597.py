// Khaled Alam - KhaledAlam.net
// Google Code Jam 2017 | Problem A
#include <bits/stdc++.h>
using namespace std;

string str;
map<int, bool> vis;
long long k, tests, strSz, tmpCnt, cntMinSoFar;
bool fine = false;

bool isOk() {
	for (char c : str)
		if (c != '+')
			return false;
	return true;
}
void go(int idx) {
//	cou1t << str <<   ' '<<tmpCnt<<endl;
	if (isOk()) {
		cntMinSoFar = min(cntMinSoFar, tmpCnt);
		fine = true;
		return;
	}
	if (idx == strSz - 1) {
		return;
	}

	for (int i = idx; i <= strSz - k; ++i) {

		if (!vis[i]) {

			tmpCnt++;
			vis[i] = true;
			for (int j = i; j < i + k; ++j) {
				str[j] = (str[j] == '+' ? '-' : '+');
			}
			go(i + 1);
			for (int j = i; j < i + k; ++j) {
				str[j] = (str[j] == '+' ? '-' : '+');
			}
			vis[i] = false;
			tmpCnt--;
		}
	}
}

void init() {
	cntMinSoFar = 1e9;
	tmpCnt = 0;
	strSz = str.length();
	vis.clear();
	fine = false;
}

int main() {
//	freopen("data.in", "r", stdin);
//	freopen("data.out", "w", stdout);
	cin >> tests;
	for (int t = 1; t <= tests; ++t) {
		cin >> str >> k;
		init();
		go(0);
		if (fine) {
			cout << "Case #" << t << ": " << cntMinSoFar << '\n';
			continue;
		}
		cout << "Case #" << t << ": IMPOSSIBLE\n";
	}
}
