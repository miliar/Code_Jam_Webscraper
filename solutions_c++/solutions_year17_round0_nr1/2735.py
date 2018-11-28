#include <bits/stdc++.h>

using namespace std;

int main() {
	int T;
	cin >> T;
	string inp;
	int k;
	for(int t = 1; t <= T; t++) {
		cin >> inp >> k;
		int n = inp.length();
		int ans = 0;
		for(int i = 0; i <= n - k; i++) {
			if(inp[i] == '-') {
				ans += 1;
				for(int j = i; j < i + k; j++) {
					if(inp[j] == '-')
						inp[j] = '+';
					else
						inp[j] = '-';
				}
			}
		}
		int flag = 0;
		for(int i = 0; i < n; i++) {
			if(inp[i] == '-'){
				flag = 1;
				break;
			}
		}
		cout << "Case #" << t << ": ";
		if(flag)
			cout << "IMPOSSIBLE" << endl;
		else
			cout << ans << endl;

	}
	return 0;
}