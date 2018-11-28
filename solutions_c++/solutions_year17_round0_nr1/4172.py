#include <bits/stdc++.h>
using namespace std;
int t, co, cnt, k; string s;
int main () {
	freopen("in", "r", stdin);
	freopen("out", "w", stdout);
    cin >> t; while(t--) {
		cin>>s>>k; cnt = 0;
		for(int i=0; i<s.size()-k+1; i++) {
			if(s[i] == '-') {
				for(int j=i; j<i+k; j++) 
					s[j] = s[j] == '-' ? '+' : '-';
				cnt++; 
			} 
		} bool f=1;
		printf("Case #%d: ", ++co);
		for(char ch : s) {
			if(ch == '-') {
				f = 0, puts("IMPOSSIBLE");
				break;
			}
		} if(f) cout<<cnt<<endl;
    }
}
