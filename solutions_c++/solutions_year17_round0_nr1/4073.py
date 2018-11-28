#include <bits/stdc++.h>
using namespace std;
typedef long long LL;

main() {
	FILE *fin = freopen("A-large.in", "r", stdin);
	FILE *fout = freopen("A-large.out", "w", stdout);
	assert( fin!=NULL );
	int T;
	cin >> T;
	for(int t = 1; t <= T; t++){
		cout << "Case #" << t << ": ";
		string s;
		int k;
		cin >> s >> k;
		int ok = 1;
		int cnt = 0;
		for(int i = 0; i+k-1 < s.size(); i++){
			if((i == 0 && s[i] == '-') || (i > 0 && s[i] != s[i-1])){
				for(int j = i; j < i + k; j++){
					s[j] ^= ('+' ^ '-');
				}
				cnt++;
			}
		}
		for(int i = 0; i < s.size(); i++){
			if(s[i] == '-'){
				ok = 0;
			}
		}
		if(ok){
			cout << cnt << endl;
		} else {
			cout << "IMPOSSIBLE" << endl;
		}
	}
	exit(0);
}