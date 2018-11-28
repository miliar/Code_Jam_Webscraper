#include <bits/stdc++.h>
using namespace std;

#define rep(i, n) for(int i=0; i<int(n); ++i)
#define sz(v) ((int)(v).size())
#define all(v) (v).begin(),(v).end()
typedef long long ll;


int TC;
void solve() {
	string s;
	int w;
	cin >> s >> w;
	int cnt = 0;
	rep(i, sz(s) - w + 1) {
		if (s[i] == '-') {
			rep(j, w) s[i+j] = s[i+j] == '-' ? '+' : '-';
			cnt++;
		}
	}
	if (count(all(s), '+') == sz(s))
		cout << cnt << endl;
	else
		cout << "IMPOSSIBLE" << endl;
}
int main() {
	int T; cin >> T;
	for(int TC=1; TC<=T; TC++) {
		cout << "Case #" << TC << ": ";
		solve();
	}
}

