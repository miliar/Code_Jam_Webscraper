#include<bits/stdc++.h>

using namespace std;

typedef long long ll;

#include<bits/stdc++.h>

using namespace std;

typedef long long ll;

char st = 'H';

bool srt(pair<int, int> l, pair<int, int> r) {
	if (l.first == r.first) {
		if (l.second == st)
			return true;
		else
			return false;
	}
	return l.first > r.first;
}

int main() {
	freopen("out.txt", "w", stdout);
	freopen("B-small-attempt1.in", "r", stdin);
	ios::sync_with_stdio(false);
	int T;
	cin >> T;
	for (int tt = 1; tt <= T; tt++) {
		int n, r, g, b, o, v, y;
		cin >> n >> r >> o >> y >> g >> b >> v;
		int l = max(max(r, b), y);
		if (l > n - l) {
			cout << "Case #" << tt << ": IMPOSSIBLE\n";
			continue;
		}
		char ls = 'h';
		string ans = "";
		vector<pair<int, char>> x;
		x.push_back(make_pair(r, 'R'));
		x.push_back(make_pair(b, 'B'));
		x.push_back(make_pair(y, 'Y'));
		x.push_back(make_pair(o, 'O'));
		x.push_back(make_pair(g, 'G'));
		x.push_back(make_pair(v, 'V'));
		for (int i = 0; i < n; i++) {
			sort(x.begin(), x.end(), srt);
			for (int j = 0; j < 6; j++)
				if (ls != x[j].second) {
					ans += x[j].second;
					x[j].first--;
					ls = x[j].second;
					if (i == 0)
						st = x[j].second;
					break;
				}
		}
		cout << "Case #" << tt << ": " << ans << "\n";
	}
	return 0;
}
