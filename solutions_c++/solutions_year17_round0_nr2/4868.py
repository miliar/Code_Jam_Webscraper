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

vector<int> cut(ll n){
	vector<int> res;
	while(n){
		res.push_back(n%10);
		n/=10;
	}
	reverse(res.begin() , res.end());
	return res;
}
vector<int> v;
ll pw[20];
ll memo[20][12][3];
ll solve(int index, int lstd ,bool isless ){
	if(index == (int)v.size()){
		return 0;
	}
	int po = (int)v.size()- index-1;
	ll ret = -2000000000LL * 1000000000LL;
	for(int i=lstd;i<=9;i++){

		if(isless){
			ret = max(ret, solve(index+1,i,isless) + i*pw[po] );
		}else{

			if(i < v[index]){
				ret = max(ret, solve(index+1,i,true) + i*pw[po] );
			}else if(i == v[index]){
				ret = max(ret, solve(index+1,i,isless) + i*pw[po] );
			}

		}

	}
	return ret;
}


int main() {
	freopen("input.txt","rt",stdin);
	freopen("output.txt","w",stdout);
	int t;
	scanf("%d",&t);
	for(int cn=1;cn<=t;cn++){
		ll n;
		scanf("%lld",&n);
		v = cut(n);
		pw[0]=1;
		for(int i=1;i<20;i++){
			pw[i] = pw[i-1] * 10;
		}
		memset(memo,-1,sizeof memo);
		cerr<<cn<<endl;
		printf("Case #%d: %lld\n",cn,solve(0,0,0));
	}
	return 0;
}
