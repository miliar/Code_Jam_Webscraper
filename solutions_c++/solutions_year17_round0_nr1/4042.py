#include <bits/stdc++.h>

using namespace std; 

typedef pair<int, int> pii;
typedef long long ll;
#define mp make_pair
#define pb push_back;

void solve() {
	string s;
	int k;
	cin >> s >> k;
	
	int ans = 0;
	for (int i = 0; i <= (int) s.size() - k; i++) {
		if (s[i] == '+')
			continue;
		ans ++;
		for (int j = i; j < i + k; j++) {
			s[j] = (s[j] == '+') ? '-' : '+';
		} 
	}
	for (int i = 0; i < (int) s.size(); i++) {
		if (s[i] == '-') {
			cout << "IMPOSSIBLE\n";
			return ;	
		}
	}
	cout << ans << '\n';
}

int main () {
#ifdef LOCAL
	freopen ("test.in", "r", stdin);
	freopen ("test.out", "w", stdout);
#endif

	int t;
	cin >> t;
	for (int i = 1; i <= t; i++) {
		cout << "Case #" << i << ": ";
		solve();
	}

	return 0;
}