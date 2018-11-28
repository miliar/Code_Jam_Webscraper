#include <bits/stdc++.h>
using namespace std;
typedef long long LL;

main() {
	FILE *fin = freopen("B-small-attempt1.in", "r", stdin);
	FILE *fout = freopen("B-small-attempt1.out", "w", stdout);
	assert( fin!=NULL );
	int T;
	cin >> T;
	for(int t = 1; t <= T; t++){
		cout << "Case #" << t << ": ";
		LL n;
		cin >> n;
		for(int k = n; k >= 1; k--){
			LL c = k;
			LL prev = 9;
			LL ok = 1;
			while(c > 0){
				if(c % 10 > prev){
					ok = 0;
					break;
				} else {
					prev = c % 10;
					c /= 10;
				}
			}
			if(ok){
				cout << k << endl;
				break;
			} else {
				continue;
			}
		}
	}
	exit(0);
}