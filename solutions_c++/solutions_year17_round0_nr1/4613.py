#include <bits/stdc++.h>
using namespace std;

void solve(){

	string s;
	int k, ans = 0;

	cin>>s;
	cin>>k;

	int len = s.length();

	for(int i = 0; i <= len - k; i++){
		if(s[i] == '-'){
			ans++;
			for(int j = i; j < i + k; j++){
				if(s[j] == '-')	s[j] = '+';
				else s[j] = '-';
			}
		}
	}

	for(int i = 0; i < len; i++){
		if(s[i] == '-')	ans = -1;
	}

	if(ans == -1)	cout<<"IMPOSSIBLE\n";
	else cout<<ans<<endl;
}

int main(){
	int t;
	cin>>t;
	for(int big = 1; big <= t; big++){
		cout<<"Case #"<<big<<": ";
		solve();
	}
}