//============================================================================
// Name        : GCJ.cpp
// Author      : 
// Version     :
// Copyright   : Your copyright notice
// Description : Hello World in C++, Ansi-style
//============================================================================

#include <bits/stdc++.h>
using namespace std;

typedef long long ll;

pair<ll,ll> split(ll cur){
	pair<ll,ll> p;
	if(cur&1){
		p = make_pair(cur/2,cur/2);
	}else{
		p = make_pair(cur/2,cur/2-1);
	}
	return p;
}

int main() {
	freopen("input.txt","rt",stdin);
	freopen("output.txt","w",stdout);
	int t;
	scanf("%d",&t);
	for(int cn=1;cn<=t;cn++){
//		cerr<<cn<<endl;
		ll n,k;
		scanf("%lld%lld",&n,&k);
		map<ll,ll> mp;
		mp[n]=1;
		while(k > 0){
			map<ll,ll> ::reverse_iterator it = mp.rbegin();
			ll cnt = (*it).second;
			pair<ll,ll> sp = split((*it).first);
			mp.erase(it->first);
//			if(sp.first > 0)
			mp[sp.first]+=cnt;
//			if(sp.second > 0)
			mp[sp.second]+=cnt;
			if(k <= cnt){
				printf("Case #%d: %lld %lld\n",cn,sp.first , sp.second);
				break;
			}
			k-= cnt;
		}

	}
	return 0;
}
