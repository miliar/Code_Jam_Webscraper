#include <bits/stdc++.h>
#define endl '\n'
using namespace std;
typedef long long ll;
typedef long double ld;
typedef complex<ld> pt;
const int MOD = 1e9 + 7;

int main() {
	ios::sync_with_stdio(0);
	cin.tie(0);
	int T; cin >> T;
	for (int t = 1; t <= T; t++) {
		vector<bool> in;
		string s; cin >> s;
		for (char c : s)
			in.push_back(c == '+');
		int K; cin >> K;
		int ans = 0;
		for (int i = 0; i < in.size() - K + 1; i++) {
			if (!in[i]) {
				for (int j = i; j < i + K; j++) {
					in[j] = !in[j];
				}
				ans++;
			}
		}
		for (int i = in.size() - K; i < in.size(); i++) {
			if (!in[i]) {
				cout << "Case #" << t << ": IMPOSSIBLE" << endl;
				goto next;
			}
		}
		cout << "Case #" << t << ": " << ans << endl;
next:	;
	}
	return 0;
}