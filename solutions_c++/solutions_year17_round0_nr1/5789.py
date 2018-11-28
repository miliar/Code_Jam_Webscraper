
#include <bits/stdc++.h>

using namespace std;

int main(void) {

	int n, k, t;
	int nCase;
	string s;

	cin >> t;
	nCase = 1;

	while(t--) {
		printf("Case #%d: ", nCase);
		nCase += 1;

		cin >> s;
		cin >> k;

		int ans = 0;
		for(int i = 0; i < (int)s.size() - k + 1; i++) {
			if(s[i] == '+') continue;
			ans += 1;
			for(int j = 0; j < k; j++)
				s[j + i] = ((s[j + i] == '-') ? '+' : '-');
		}

		int flag = 0;
		for(int i = 0; i < (int)s.size(); i++) {
			if(s[i] == '-') flag = 1;
		}

		if(flag) cout << "IMPOSSIBLE" << endl;
		else cout << ans << endl;
	}


	return 0;
}