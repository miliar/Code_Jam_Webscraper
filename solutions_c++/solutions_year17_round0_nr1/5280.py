#include <bits/stdc++.h>
using namespace std;
int main(){
	int cs = 0;
	int t; cin >> t;
	while(t--){
		string s; int k;
		++cs;
		cin >> s >> k;
		s = ' ' + s;
		int ans = 0, yes = 1;
		for(int i=1; i<=s.size(); ++i){
			if(s[i] == '+');
			else{
				++ans;
				for(int j=0; j<k; ++j){
					if(s[i+j] == '+') s[i+j] = '-';
					else s[i+j] = '+';
				}
			}
			if(i + k - 1 == s.size() - 1){
				for(int j=0; j<k; ++j){
					if(s[i+j] == '-'){
						yes = 0;
					}
				}
				break;
			}
		}
		cout << "Case #" << cs << ": ";
		if(yes) cout << ans << endl;
		else cout << "IMPOSSIBLE" << endl;
	}
}