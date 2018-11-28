#include <bits/stdc++.h>
using namespace std;
string s;
int vis[105][15][2];
int id;
string solve(int ind, int minn, bool up) {
	if (ind >= int(s.size()))
		return "";
	if (vis[ind][minn][up] == id)
		return "-";
	vis[ind][minn][up] = id;
	for (int x = 9; x >= minn; x--) {
		int cur = s[ind] - '0';
		if (x > cur && !up)
			continue;
		string tmp = solve(ind + 1, x, up | (x < cur));
		if (tmp == "-")
			continue;
		tmp = char(x + '0') + tmp;
		return tmp;
	}
	return "-";
}

int main() {
	ios::sync_with_stdio(false);
	freopen("/home/ahmed/Desktop/few/B-large.in", "r", stdin);
	freopen("/home/ahmed/Desktop/few/B-large.out", "w", stdout);
	int t; cin >> t;
	while (t--) {
		cin >> s;
		cout << "Case #" << ++id << ": ";
		string ans = solve(0, 1, 0);
		if (ans == "-")
			ans = string(s.size() - 1, '9');
		cout << ans << endl;
	}

	return 0;
}
