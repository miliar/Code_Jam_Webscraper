#include <bits/stdc++.h>

using namespace std;

int main() {
	ios_base::sync_with_stdio(0);

	int z;
	cin >> z;
	for(int i = 1; i <= z; i++) {
		string s;
		cin >> s;

		int n = s.size();

		int k;
		cin >> k;

		int cnt = 0;

		for(int j = 0; j < n; j++) {
			if(s[j] == '-') {
				cnt++;
				int last = j + k - 1;
				if(last >= n) {
					cnt = -1;			
					break;
				} else {
					for(int l = j; l <= last; l++) {
						if(s[l] == '+') s[l] = '-';
						else s[l] = '+';
					}
				}
			} 			
		}	

		cout << "Case #" << i << ": ";
		if(cnt == -1) cout << "IMPOSSIBLE" << endl;
		else cout << cnt << endl;	
			
	}

	return 0;
}


