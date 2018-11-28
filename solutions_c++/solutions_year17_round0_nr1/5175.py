#include <bits/stdc++.h>
using namespace std;
int main() {
	freopen("A-large.in", "r", stdin);
	freopen("output.txt", "w", stdout);
	int nTest, k, result, tmp;
	bool changed;
	string s;
	cin >> nTest;
	for(int i = 1; i <= nTest; i++) {
		cin >> s >> k;
		result = -1;
		tmp = 0;
		changed = true;
		while(changed) {
			changed = false;
			for(int j = 0; j < s.length()-k+1; j++) {
				if( s[j] == '-' ) {
					tmp++;
					for(int jj = 0; jj < k; jj++) {
						s[j+jj] = ( s[j+jj] == '-' ? '+' : '-');

					}
					changed = true;
					break;
				}
		}
		}
		for(int j = 0; j < s.length(); j++) {
			if( s[j] == '-') break;
			if( j == s.length()-1) result = tmp;
		}
		if( result == -1)
			cout << "Case #" << i << ": IMPOSSIBLE" << endl;
		else
			cout << "Case #" << i << ": "<<result << endl;
	}
	return 0;
}
