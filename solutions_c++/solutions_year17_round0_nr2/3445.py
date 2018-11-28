#include <bits/stdc++.h>

using namespace std;

void solve (int current_case) {
	string s; cin >> s;

	cout << "Case #" << current_case << ": ";
	for (int i = 1; i < s.size(); ++i) 
		if (s[i] < s[i - 1]) {
			if (s[i - 1] == '1') {
				cout << string(s.size() - 1, '9') << '\n';
				return;
			}
			while (i > 0 && s[i] < s[i - 1]) {
				--s[i - 1];
				--i;
			}
			cout << s.substr(0, i) << char(s[i]) << string(s.size() - i - 1, '9') << '\n';
			return;
		}
	cout << s << '\n';
}

int main () {
    ios_base::sync_with_stdio(false);
    cin.tie(0);
    
    #ifdef FSOCIETY
		freopen("B-large.in", "r", stdin);
		freopen("output.txt", "w", stdout);
	#endif
       
    int t; cin >> t;
    for (int i = 1; i <= t; ++i)
    	solve(i);
}