// -*- compile-command: "g++ -g -Wno-return-type -Wall -Wextra -DLOCAL -std=c++11 -D_GLIBCXX_DEBUG c.cpp -oc && ./c " -*-
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

int simulate(int h_d,int a_d,int h_k,int a_k,int b,int d,int n_b,int n_d){
	int max_h=h_d;
	int steps=0;
	auto attack=[&](){ h_k -= a_d; steps++; };
	auto buff=[&](){ a_d += b; --n_b; steps++; };
	auto heal=[&](){ h_d = max_h; steps++; };
	auto debuff=[&](){ a_k = max(0LL,a_k-d); --n_d; steps++; };
	int limit=3*h_k;
	while(h_d>0 && h_k>0){
		if((n_d!=0||n_b!=0||h_k-a_d>0) && h_d-max(0LL,a_k-(n_d!=0)*d) <= 0){ heal(); /*cout<<"HEAL"<<endl;*/ }
		else if(n_d>0){ debuff(); /*cout<<"DEBUFF"<<endl;*/ }
		else if(n_b>0){ buff(); /*cout<<"BUFF"<<endl;*/ }
		else{ attack(); /*cout<<"ATTACK"<<endl;*/ }
		if(h_k>0) h_d -= a_k;
		if(--limit<=0) h_d=0;
	}
	if(h_d<=0) return 1e18;
	return steps;
}

void solve(){
	int h_d,a_d,h_k,a_k,b,d;
	cin>>h_d>>a_d>>h_k>>a_k>>b>>d;
	int best=1e18;
	f(n_b,101){
		f(n_d,101){
			int cand=simulate(h_d,a_d,h_k,a_k,b,d,n_b,n_d);
			if(cand<best) best=cand;
		}
	}
	if(best==1e18) cout<<"IMPOSSIBLE\n";
	else cout<<best<<'\n';
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
