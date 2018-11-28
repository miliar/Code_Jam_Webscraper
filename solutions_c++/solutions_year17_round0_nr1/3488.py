#include <bits/stdc++.h>

using namespace std;

void solve (int current_case) {
	string s; cin >> s;
	int k; cin >> k;

	int last = s.size() - k;
	int ans = 0;
	for (int i = 0; i <= last; ++i) 
		if (s[i] == '-') {
			++ans;
			for (int j = i, h = 0; h < k; ++j, ++h)
				s[j] = (s[j] == '-' ? '+' : '-');
		}

	bool happy_side = true;
	for (int i = last + 1; i < s.size(); ++i)
		if (s[i] == '-') {
			happy_side = false;
			break;
		}

	cout << "Case #" << current_case << ": ";
	if (happy_side)
		cout << ans << '\n';
	else
		cout << "IMPOSSIBLE\n";
}

int main () {
    ios_base::sync_with_stdio(false);
    cin.tie(0);
    
    #ifdef FSOCIETY
		freopen("A-large.in", "r", stdin);
		freopen("output.txt", "w", stdout);
	#endif
       
    int t; cin >> t;
    for (int i = 1; i <= t; ++i)
    	solve(i);
}