#include <bits/stdc++.h>
using namespace std;

void solve(int t_num) {
	string s;
	int n, k, ans = 0;

	bool impossible = false;

	cin >> s >> k;
	n = s.size();
	for(int i = 0; i < n; ++i) {
		if(s[i] == '-') {
			if(i + k - 1 >= n) {
				impossible = true;
				break;
			}
			for(int j = i; j <= i + k - 1; ++j)
				s[j] = s[j] == '+' ? '-' : '+';
			ans++;
		}
	}
	cout << "Case #" << t_num << ": ";
	if(impossible) 
		cout << "IMPOSSIBLE\n";
	else
		cout << ans << "\n";
}

int main() {
	int t;
	cin >> t;
	for(int i = 1; i <= t; ++i) {
		solve(i);
	}
	return 0;
}