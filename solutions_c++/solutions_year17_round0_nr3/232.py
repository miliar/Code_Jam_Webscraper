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

struct I{
	int x;
	bool operator<(const I &r)const{
		return x>r.x;
	}
	pair<I,I> split(){
		return {{x-1-(x-1)/2},{(x-1)/2}};
	}
};

void solve(){
	int n,k;
	cin>>n>>k;
	map<I,int> m;
	m[I{n}]=1;
	int c=0;
	I i;
	for(;;){
		auto it=m.begin();
		i=it->fi;
		I i1,i2;
		tie(i1,i2)=i.split();
		int x=it->se;
		if(c+x<k){
			m.erase(it);
			c+=x;
			m[i1]+=x;
			m[i2]+=x;
		}else{
			cout<<i1.x<<" "<<i2.x<<'\n';
			break;
		}
	}
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
