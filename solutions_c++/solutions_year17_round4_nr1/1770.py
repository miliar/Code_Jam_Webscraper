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
	int n,p;
	cin>>n>>p;
	vc<int> g(n);
	vc<int> x(4);
	f(i,n){
		int g;
		cin>>g;
		x[g%p]++;
	}
	int cur=0,r=0;
	auto serve = [&](int k){
		if(!cur) r++;
		x[k]--;
		cur=(cur+k)%p;
	};
	while(x[0]) serve(0);
	switch(p){
		case 2:
			while(x[1]) serve(1);
			break;
		case 3:
			while(x[2]){
				serve(2);
				if(cur==2 && x[1]) serve(1);
			}
			while(x[1]) serve(1);
			break;
		case 4:
			int cur=0;
			while(x[2]&&(cur==2||x[2]>1))
				serve(2);
			while(x[1]){
				serve(1);
				if(x[3] && cur==1){
					serve(3);
				}
			}
			while(x[3]) serve(3);
			while(x[2]) serve(2);
			break;
	}
	f(i,p) assert(!x[i]);
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


// 1,2
