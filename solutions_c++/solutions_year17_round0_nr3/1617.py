/*
 * C.cpp
 *
 *  Created on: Apr 8, 2017
 *      Author: xing
 */

#include <iostream>
#include <map>

using namespace std;

//#define DEBUG

void solve(int ca){
	long N, K, res;
	cin>>N>>K;
	map<long, long> lookup;
	lookup[N] = 1;

	while(K>lookup.rbegin()->second){
		auto it = lookup.rbegin();
		K -= it->second;
		if(it->first & 1){
			//odd
			lookup[it->first/2] += it->second*2;
		}
		else{
			lookup[it->first/2] += it->second;
			lookup[it->first/2-1] += it->second;
		}
		lookup.erase( --it.base() );

#ifdef DEBUG
		cout<<"N "<<K<<endl;
		cout<<"lookup:";
		for(auto&& p:lookup)
			cout<<" ("<<p.first<<","<<p.second<<")";
		cout<<endl;
#endif

	}
	res = lookup.rbegin()->first;
	cout<<"Case #"<<ca<<": ";
	if(res & 1){
		//odd
		cout<<res/2<<" "<<res/2<<endl;
	}
	else{
		cout<<res/2<<" "<<res/2-1<<endl;
	}

}

int main(){
	int T;
	cin>>T;
	for(int i = 1;i<=T;i++){
		solve(i);
	}
}
