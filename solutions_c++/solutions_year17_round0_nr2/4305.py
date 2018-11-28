#include <bits/stdc++.h>
using namespace std;
void solve(string s){
	long long n=stoll(s);
	if(n==0) return;
	if(n<=9) cout << n;
	else if(n==10) cout << 9;
	else{
		int i;
		for(i=int(s.size())-1;i>0;--i)
			if(s[i-1]>s[i]) break;
		if(i==0) cout << s;
		else{
			solve(to_string(stoll(s.substr(0,i))-1));			
			for(;i<int(s.size());++i) cout << 9;
		}
	}
}
int main(){
	ios::sync_with_stdio(0);
	
	int t,tc=0;
	cin >> t;
	string s;
	while(t--){
		cin >> s;
		cout << "Case #" << ++tc << ": ";
		solve(s);
		cout << '\n';
	}
	return 0;
}