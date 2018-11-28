#include <bits/stdc++.h>

using namespace std;

#define ll long long
#define mp make_pair
#define f first
#define s second
#define ld long double
#define pb push_back

inline void solve() {
	string s;
	cin >> s;
	int k;
	cin >> k;
	int n = s.size();
	int v[n];
	for (int i = 0; i < n; ++i) {
		if (s[i] == '+') {
			v[i] = 1;
		}
		else {
			v[i] = 0;
		}
	}
	int ans = 0;
	for (int i = 0; i < n - k + 1; ++i) {
		if (v[i] == 0) {
			++ans;
			for (int j = i; j < i + k; ++j) {
				v[j] = 1 - v[j];
			}
		}
	}
	for (int i = 0; i < n; ++i) {
		if (v[i] == 0) {
			cout << "IMPOSSIBLE";
			return;
		}
	}
	cout << ans;
}

int main(){
    freopen("gcj.txt", "w", stdout);
	int n;
	cin >> n;
	for (int i = 1; i <= n; ++i) {
		cout << "Case #" << i << ": ";
		solve();
		cout << '\n';
	}
}
