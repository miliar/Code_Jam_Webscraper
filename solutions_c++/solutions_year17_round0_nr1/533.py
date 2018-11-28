#include <bits/stdc++.h>

using namespace std;

typedef long long int64;
typedef unsigned long long uint64;

int main(){
	ios::sync_with_stdio(false);
	int t, k;
	string str;
	
	char inv[500];
	inv['+'] = '-';
	inv['-'] = '+';

	cin >> t;

	for(int w = 1; w <= t; w++){
		cin >> str >> k;

		int ans = 0, n = str.size();
		for(int i = 0; (i+(k-1)) < n; i++){
			if( str[i] == '-' ){
				for(int j = 0; j < k; j++){
					str[i+j] = inv[str[i+j]];
				}
				ans++;
			}
		}

		for(int i = 0; i < n; i++){
			if( str[i] == '-' ){
				ans = -1;
				break;
			}
		}

		cout << "Case #" << w << ": ";
		if( ans == -1 ) cout << "IMPOSSIBLE\n";
		else cout << ans << '\n';

	}

	return 0;
}