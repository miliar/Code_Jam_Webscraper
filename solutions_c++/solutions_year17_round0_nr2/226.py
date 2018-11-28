// -*- compile-command: "g++ -g -Wno-return-type -Wall -Wextra -DLOCAL -std=c++11 -D_GLIBCXX_DEBUG b.cpp -ob && ./b " -*-
#include <bits/stdc++.h>
using namespace std;
using LL=long long;
#define int LL
#define vc vector
#define pb push_back
#define pr pair
#define fi first
#define se second
#define sz(v) ((int)(v).size())
#define all(v) (v).begin(),(v).end()
#define f(i,n) for(int i=0;i<(n);i++)
#define fv(i,v) f(i,sz(v))

void solve(){
	string s;
	cin>>s;
	for(int i=sz(s)-1;i>=1;i--){
		if(s[i-1]>s[i]){
			for(int j=i;j<sz(s);j++)
				s[j]='9';
			int j=i-1;
			for(;j>=1&&s[j]=='0';j--)
				s[j]='9';
			assert(s[j]!='0');
			s[j]--;
		}
	}
	while(s[0]=='0') s=s.substr(1,sz(s)-1);
	cout<<s<<'\n';
}

main(){
	ios::sync_with_stdio(0),cin.tie(0);
	int T;
	cin>>T;
	for(int t=1;t<=T;t++){
		cout<<"Case #"<<t<<": ";
		solve();
	}
}
