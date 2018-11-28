#define _CRT_SECURE_NO_WARNINGS
#include <bits/stdc++.h>
using namespace std;

int main()
{
	freopen("A-large.in", "r", stdin);
	freopen("output.txt", "w", stdout);
	int t; cin >> t;
	int I = 1;
	while (t--){
		cout << "Case #" << I++ << ": ";
		string s; cin >> s;
		int k; cin >> k;
		int ans = 0;
		for (int i = 0; i < (int)s.size() - k + 1; i++){
			if (s[i] == '+')
				continue;
			ans++;
			for (int j = i, h = k; h--; j++){
				s[j] = s[j] == '+' ? '-' : '+';
			}
		}
		if (s.find('-') == -1)
			cout << ans << endl;
		else
			cout << "IMPOSSIBLE" << endl;
	}
	return 0;
}