// -*- compile-command: "g++ -g -Wno-return-type -Wall -Wextra -DLOCAL -std=c++11 -D_GLIBCXX_DEBUG a.cpp -oa && ./a " -*-
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
	int k;
	cin>>s>>k;
	int r=0;
	for(int a=0,b=s.size();b-a>=k;a++,b--){
		if(s[a]=='-'){
			r++;
			f(i,k) s[a+i]^='+'^'-';
		}
		if(s[b-1]=='-'){
			r++;
			f(i,k) s[b-1-i]^='+'^'-';
		}
	}
	fv(i,s) if(s[i]=='-'){ cout<<"IMPOSSIBLE\n"; return; }
	cout<<r<<'\n';
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
