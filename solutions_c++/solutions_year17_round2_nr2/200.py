#include<bits/stdc++.h>
using namespace std;

int n;
int arr[15];
char C[15] = {'R', 'O', 'Y', 'G', 'B', 'V'};
bool ok(string &s, char c) {
	if (s[0] != '-')
		return false;
	for (int i = 0; i < int(s.size()); i++)
		if (s[i] == c)
			return false;
	return true;
}

void add(string &s, char c) {
	if (s[0] != '-')
		return;
	s += c;
}


string solve(vector<pair<int, char> > v) {
	int n = v[0].first + v[1].first + v[2].first;
	vector<string> ans;
	for (int i = 0; i < n; i++)
		ans.push_back("-");
	string final = "IMPOSSIBLE";
	int ind = 0;
	for (int i = 0; i < 3; i++) {
		char c = v[i].second;
		int cnt = v[i].first;
		while (cnt > 0) {
			int steps = 0;
			while (!ok(ans[ind], c) && steps < 2 * n)
				ind = (ind + 1) % n, steps++;
			if (!ok(ans[ind], c))
				break;
			cnt -= 1;
			ans[ind] = ""; ans[ind] += c;
			add(ans[(ind + 1) % n], c);
			add(ans[(ind - 1 + n) % n], c);
		}
		if (cnt > 0)
			break;
		if (i == 2) {
			final = "";
			for (int x = 0; x < n; x++)
				final += ans[x];
		}
	}
	return final;
}

string special() {
	for (int x = 1, y = 4; x < 6; x += 2, y = (y + 2) % 6) {
		if (arr[x] + arr[y] != n)
			continue;
		if (arr[x] != arr[y])
			return "IMPOSSIBLE";

		string ans = "";
		for (int i = 0; i < arr[x]; i++)
			ans += C[x], ans += C[y];
		return ans;

	}
	return "-";

}

bool ok(char c, char d) {
	if (c == d)
		return false;
	if (c == 'O' && d == 'R')
		return false;
	if (c == 'O' && d == 'Y')
		return false;
	if (c == 'Y' && d == 'O')
		return false;
	if (c == 'R' && d == 'O')
		return false;

	if (c == 'O' && d == 'R')
		return false;
	if (c == 'O' && d == 'Y')
		return false;
	if (c == 'Y' && d == 'O')
		return false;
	if (c == 'R' && d == 'O')
		return false;

	if (c == 'G' && d == 'B')
		return false;
	if (c == 'G' && d == 'Y')
		return false;
	if (c == 'Y' && d == 'G')
		return false;
	if (c == 'B' && d == 'G')
		return false;

	if (c == 'V' && d == 'B')
		return false;
	if (c == 'V' && d == 'R')
		return false;
	if (c == 'R' && d == 'V')
		return false;
	if (c == 'B' && d == 'V')
		return false;
	return true;
}

void makeSure(string s) {
	if (s == "IMPOSSIBLE")
		return;
	for (int i = 0; i < int(s.size()); i++)
		if (!ok(s[i], s[(i + 1) % s.size()]))
			assert(0);
}

int main() {
	ios::sync_with_stdio(0);
	freopen("/home/ahmed/Desktop/fiewojfe/B-large.in", "r", stdin);
	freopen("/home/ahmed/Desktop/fiewojfe/B-large.out", "w", stdout);

	int t; cin >> t;
	int id = 1;
	while (t--) {
		cin >> n;
		for (int i = 0; i < 6; i++)
			cin >> arr[i];
		cout << "Case #" << id++ << ": ";
		//  R, O, Y, G, B, and V.

		string q = special();
		if (q != "-") {
			cout << q << endl;
			makeSure(q);
			continue;
		}

		bool valid = true;
		for (int x = 1, y = 4; x < 6; x += 2, y = (y + 2) % 6) {
			if (arr[x] == 0)
				continue;
			if (arr[x] + 1 > arr[y])
				valid = false;
			arr[y] -= arr[x];
		}

		if (!valid) {
			cout << "IMPOSSIBLE" << endl;
			continue;
		}

		vector<pair<int, char> > v;
		v.push_back(make_pair(arr[0], 'R'));
		v.push_back(make_pair(arr[2], 'Y'));
		v.push_back(make_pair(arr[4], 'B'));
		sort(v.rbegin(), v.rend());
		string ans = solve(v);

		if (ans == "IMPOSSIBLE") {
			cout << "IMPOSSIBLE" << endl;
			continue;
		}

		for (int x = 1, y = 4; x < 6; x += 2, y = (y + 2) % 6) {
			if (arr[x] == 0)
				continue;
			string r = "";
			for (int a = 0; a < arr[x]; a++)
				r += C[y], r += C[x];
			r += C[y];
			for (int i = 0; i < int(ans.size()); i++) {
				if (ans[i] != C[y])
					continue;
				ans = ans.substr(0, i) + r + ans.substr(i + 1);
				break;
			}
		}
		cout << ans << endl;
		makeSure(ans);
	}

	return 0;
}
