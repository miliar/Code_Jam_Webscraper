#include <bits/stdc++.h>
using namespace std;
int main() {
	std::ios_base::sync_with_stdio(false);
	int n;
	cin >> n;
	for(int t = 0; t < n; ++t) {
		string s;
		int k;
		cin >> s;
		cin >> k;
		int ans = 0;
		for(int i = 0; i <= s.size() - k; ++i) {
			if(s[i] == '-') {
				ans++;
				for(int j = i; j < i + k; j++) {
					if(s[j] == '+')
						s[j] = '-';
					else
						s[j] = '+';
				}
			}
		}
		bool flag = true;
		for(int i = 0; i < s.size(); ++i) {
			if(s[i] == '-') {
				flag = false;
				break;
			}
		}
		cout << "Case #" << t + 1 << ": ";
		if(flag) 
			cout << ans << endl;
		else
			cout << "IMPOSSIBLE" << endl;
	}
}