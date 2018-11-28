#include <bits/stdc++.h>
using namespace std;

#define pb push_back
#define mp make_pair

typedef long long ll;
typedef pair<int, int> pii;

int T;
string s;
int k;

void load() {
	cin >> s >> k;
}

void solve(int tc) {
	cout << "Case #" << tc << ": ";
	int res = 0;
	for (int i = 0; i + k <= (int)s.size(); ++i) {
		if (s[i] == '-') {
			++res;
			for (int j = 0; j < k; ++j) {
				s[i + j] ^= '-' ^ '+';
			}
		}
	}
	if (s != string(s.size(), '+')) cout << "IMPOSSIBLE" << '\n';
	else cout << res << '\n';
}

void clear() {
}

int main() {
	ios_base::sync_with_stdio(false);
	cin.tie(0);
	cin >> T;
	for (int tc = 1; tc <= T; ++tc) {
		clog << tc << "/" << T << endl;
		load();
		solve(tc);
		clear();
	}
	return 0;
}
