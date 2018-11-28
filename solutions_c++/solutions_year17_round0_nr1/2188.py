#include <iostream>
#include <algorithm>
#include <vector>
using namespace std;

char s[1007];
int n, k;

int main() {
	ios_base::sync_with_stdio(0);
	int tt;
	cin >> tt;
	for(int it = 1; it <= tt; ++it) {
		n = 0;
		cin >> (s + 1);
		cin >> k;
		while(s[n + 1]) n++;
		int res = 0;
		for(int i = 1; i + k - 1 <= n; ++i) {
			if(s[i] == '-') {
				for(int j = 0; j < k; ++j) {
					if(s[i + j] == '-') s[i + j] = '+';
					else s[i + j] = '-';
				}
				res++;
			}
		}	
		
		int ok = 1;
		for(int i = 1; i <= n; ++i) if(s[i] != '+') ok = 0;
		cout << "Case #" << it << ": ";
		if(ok) cout << res << '\n';
		else cout << "IMPOSSIBLE\n";
	}
	return 0;
}	
