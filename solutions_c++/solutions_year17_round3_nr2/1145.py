#define _GLIBCXX_DEBUG
#include<iostream>
#include<cstdio>
#include<bits/stdc++.h>//"geometry.cpp"
#include<iomanip>//"cout<<fixed<<setprecision(n)<<sth<<endl;"
#include<queue>
#include<string>
#include<vector>
#include<utility>
#include<set>
#include<map>
#include<algorithm>//"lower_bound(it,it,v)", "next_permutation(a,a+n)"
#include<functional>//"greater<T>" Ex. sort(a,a+n,greater<int>());
#include<cmath>//"abs", "sqrt"
using namespace std;
#define pb push_back
#define fi first
#define sc second
#define mp make_pair
#define is insert
typedef pair<bool,pair<int,int> > pii;//Add other types in the same way.

bool cmp (pii x,pii y){
	return x.sc.fi<y.sc.fi;
}

void solve(){
	int c0,j0;
	cin>>c0>>j0;
	vector<pii> j;
	vector<int> cw,jw;
	int cws=0,jws=0,f=0;
	for(int i=0;i<c0;++i){
		int s,t;
		cin>>s>>t;
		j.pb(mp(true,mp(s,t)));
	}
	for(int i=0;i<j0;++i){
		int s,t;
		cin>>s>>t;
		j.pb(mp(false,mp(s,t)));
	}
	sort(j.begin(),j.end(),cmp);
	c0=0;j0=0;
	for(int i=0;i<j.size();++i){
		if(j[i].fi){
			c0+=j[i].sc.sc-j[i].sc.fi;
		}else{
			j0+=j[i].sc.sc-j[i].sc.fi;
		}
	}
	c0=720-c0;
	j0=720-j0;
	int ans=0;
	for(int i=0;i<j.size()-1;++i){
		if(j[i].fi!=j[i+1].fi){
			++ans;
			f+=j[i+1].sc.fi-j[i].sc.sc;
		}else if(j[i].fi){
			int in=j[i+1].sc.fi-j[i].sc.sc;
			if(in>0) cw.pb(in);
		}else{
			int in=j[i+1].sc.fi-j[i].sc.sc;
			if(in>0) jw.pb(in);
		}
	}
	if(j[0].fi!=j[j.size()-1].fi){
		++ans;
		f+=j[0].sc.fi+1440-j[j.size()-1].sc.sc;
	}else if(j[0].fi){
		int in=j[0].sc.fi+1440-j[j.size()-1].sc.sc;
		if(in>0) cw.pb(in);
	}else{
		int in=j[0].sc.fi+1440-j[j.size()-1].sc.sc;
		if(in>0) jw.pb(in);
	}
	for(int i=0;i<cw.size();++i){
		cws+=cw[i];
	}
	for(int i=0;i<jw.size();++i){
		jws+=jw[i];
	}
	if(cws<=c0&&jws<=j0){
		cout<<ans<<endl;
	}else if(cws>c0){
		sort(cw.begin(),cw.end(),greater<int>());
		cws-=c0;
		int i=0;
		for(;cws>0&&i<cw.size();++i){
			cws-=cw[i];
		}
		cout<<ans+2*i<<endl;
	}else{
		sort(jw.begin(),jw.end(),greater<int>());
		jws-=j0;
		int i=0;
		for(;jws>0&&i<jw.size();++i){
			jws-=jw[i];
		}
		cout<<ans+2*i<<endl;
	}
}

int main(){
	int Q;
	cin>>Q;
	for(int q=1;q<=Q;++q){
		cout<<"Case #"<<q<<": ";
		solve();
	}
}
