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
	int n,p;
	cin>>n>>p;
	vc<int> r(n);
	vc<vc<int> >q(n,vc<int>(p));
	f(i,n) cin>>r[i];
	f(i,n){
		f(j,p) cin>>q[i][j];
		sort(all(q[i]));
	}
	vc<vc<int>> low(n,vc<int>(p)), high(n,vc<int>(p));
	f(i,n){
		f(j,p){
			// x <= floor(q[i][j]*10/(r[i]*9))
			// ceil(q[i][j]/(r[i]*11)) <= x
			low[i][j]=(10*q[i][j]+r[i]*11-1)/(r[i]*11);
			high[i][j]=(10*q[i][j])/(r[i]*9);
		}
	}
	vc<int> cur(n,0);
	int res=0;
	for(;;){
		int clow=0,chigh=1e9;
		int tshigh=0;
		bool ok=true;
		f(i,n) if(cur[i]>=p) ok=false;
		if(!ok) break;
		f(i,n){
			clow=max(clow,low[i][cur[i]]);
			chigh=min(chigh,high[i][cur[i]]);
			if(high[i][cur[i]]<high[tshigh][cur[tshigh]])
				tshigh=i;
		}
		if(clow<=chigh){
			res++;
			f(i,n) cur[i]++;
		}else{
			cur[tshigh]++;
		}
	}
	cout<<res<<'\n';
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
