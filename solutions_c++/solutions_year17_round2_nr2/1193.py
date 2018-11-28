#include <bits/stdc++.h>

using namespace std;

typedef long long ll;
typedef pair<int, int> ii;

int main() {
	int tt;
	cin >> tt;
	for (int t = 1; t <= tt; t++) {
		int n; cin >> n;
		int r, o, y, g, b, v;
		cin >> r >> o >> y >> g >> b >> v;
		priority_queue<ii> pq;
		pq.push(ii(r, 1));
		pq.push(ii(y, 2));
		pq.push(ii(b, 3));
		int a[3]; a[0] = r; a[1] = b; a[2] = y;
		char cc[3]; cc[0] = 'R'; cc[1] = 'B'; cc[2] = 'Y';
		string ans = "";
		while (n) {
			char last;
			if (ans.size() == 0) {
				last = 'P';
			} else {
				last = ans[ans.size()-1];
			}
			int mx = 0;
			int ch = -1;
			for (int i = 0; i < 3; i++) {
				if (a[i] > 0 && last != cc[i]) {
					if (a[i] > mx) {
						mx = a[i];
						ch = i;
					} else if (a[i] == mx && cc[i] == ans[0]) {
						mx = a[i];
						ch = i;
					}
				}
			}
			if (ch == -1) {
				ans = "IMPOSSIBLE";
				break;
			} else {
				ans.push_back(cc[ch]);
				a[ch]--;
			}
			n--;
		}
		if (ans[0] == ans[ans.size()-1]) {
			ans = "IMPOSSIBLE";
		}
		cout << "Case #" << t << ": " << ans << "\n";
	}
}