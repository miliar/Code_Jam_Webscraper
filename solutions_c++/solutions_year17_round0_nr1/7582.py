#include <bits/stdc++.h>
using namespace std;
int main() {
	int K,i,j,k,t,ans;
	cin>>t;
	string s;
	for(k = 0; k < t ; k++) {
	    ans = 0;
		cin>>s>>K;
		for(i = 0; i <= s.size() - K; i++) {
			if(s[i] == '-') {
				ans++;
				for(j = i; j < i+K; j++) {
					(s[j] == '-')?s[j]='+':s[j]='-';
				}
			}
		}
		cout<<"Case #"<<k+1<<": ";
		for(i = s.size() - K; i < s.size(); i++) {
			if(s[i] == '-') {
                cout<<"IMPOSSIBLE\n";
                break;
			}
		}
		if(i == s.size())
			cout<<ans<<"\n";
	}
	return 0;
}