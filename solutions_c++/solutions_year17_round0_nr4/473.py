#include <iostream>
#include <vector>
#include <set>
#include <map>
#include <algorithm>

using namespace std;

void solve_small(int t) {
	int n, k;
	cin >> n >> k;
	vector <vector <char> > inp(n, vector <char>(n, '.'));
	bool smth = false;
	for (int i = 0; i < k; ++i) {
		char c;
		int x, y;
		cin >> c >> x >> y;
		inp[x - 1][y - 1] = c;
		if (c == 'x' || c == 'o')
			smth = true;
	}
	vector <vector <char> > arr = inp;
	for (int i = 0; i < n; ++i)
		if (inp[0][i] == '.')
			arr[0][i] = '+';
		else if (inp[0][i] == 'x')
			arr[0][i] = 'o';
	if (!smth)
		arr[0][0] = 'o';
	for (int i = 1; i < n - 1; ++i)
		arr[n - 1][i] = '+';

	set <int> pos;
	for (int i = 0; i < n; ++i)
		if (arr[0][i] != 'o')
			pos.insert(i);

	if (n > 1) {
		if (arr[0][n - 1] == 'o') {
			arr[n - 1][0] = 'x';
			pos.erase(0);
		}
		else {
			arr[n - 1][n - 1] = 'x';
			pos.erase(n - 1);
		}
	}

	for (int i = 1; i < n - 1; ++i) {
		int v = *pos.begin();
		arr[i][v] = 'x';
		pos.erase(v);
	}

	int ans = 0, s = 0;
	vector <pair <char, pair <int, int> > > res;
	for (int i = 0; i < n; ++i)
		for (int j = 0; j < n; ++j) {
			if (arr[i][j] != inp[i][j]) {
				++s;
				res.push_back({ arr[i][j], {i + 1, j + 1} });
			}
			if (arr[i][j] == '+' || arr[i][j] == 'x')
				++ans;
			else if (arr[i][j] == 'o')
				ans += 2;
		}

	cout << "Case #" << t << ": " << ans << " " << s << endl;
	for (int i = 0; i < s; ++i)
		cout << res[i].first << " " << res[i].second.first << " " << res[i].second.second << endl;
}

int main() {
	freopen("input.txt", "r", stdin);
	freopen("output.txt", "w", stdout);
	int tc;
	cin >> tc;
	for (int t = 1; t <= tc; ++t) {
		solve_small(t);
	}
}