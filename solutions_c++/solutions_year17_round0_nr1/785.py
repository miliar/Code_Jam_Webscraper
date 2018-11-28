#include <bits/stdc++.h>
using namespace std;
int main(){
	int T;
	cin >> T;
	for(int t=1;t<=T;++t){
		string s;
		int k;
		cin >> s >> k;
		cout << "Case #" << t << ": ";
		int n = s.length();
		int res = 0;
		int i = 0;
		while(i <= n-k){
			if(s[i] == '-'){
				++res;
				for(int j=0;j<k;++j){
					s[i+j] = (s[i+j]=='+'?'-':'+');
				}
			}
			++i;
		}
		bool fail = false;
		for(int j=n-k;j<n;++j){
			if(s[j] == '-') {fail = true;break;}
		}
		if(fail) cout << "IMPOSSIBLE" << endl;
		else cout << res << endl;
	}	
}