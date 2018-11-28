#include <bits/stdc++.h>
using namespace std;
using ll=long long;
long double K[1007],S[1007];

int main(){
	ll T;cin>>T;
	for(ll num=0;num<T;++num){
		long double D;
		ll N;
		cin>>D>>N;
		for(ll a=0;a<N;++a)cin>>K[a]>>S[a];
		long double latest=0;
		for(ll a=0;a<N;++a){
			long double total=D-K[a];
			long double b=total/S[a];
			latest=max(latest,b);
		}
		long double ret=D/latest;
		cout<<"Case #"<<(num+1)<<": "<<fixed<<setprecision(6)<<ret<<endl;
	}
}
