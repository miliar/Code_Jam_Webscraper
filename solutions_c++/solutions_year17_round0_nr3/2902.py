#include <bits/stdc++.h>
#define ll long long
using namespace std;
vector<ll>N;
vector<ll>K;
vector< pair<ll,ll> >res;

ll powll(ll num,ll times){
	if(times==0)return 1;
	ll ret=num;
	for(ll a=0;a<times-1;++a){
		ret*=num;
	}
	return ret;
}

int main(){
	ll T;cin>>T;
	for(ll a=0;a<T;++a){
		ll b,c;
		cin>>b>>c;
		N.push_back(b);K.push_back(c);
	}
	for(ll a=0;a<T;++a){
		ll limit=1;
		ll ppp=0;
		ll qqq=0;
		ll tempNA=N[a];
		while(K[a]>limit){
			limit+=powll(2,++ppp);
			qqq+=powll(2,ppp-1);
			tempNA=tempNA/2;
		}
		ll powed=powll(2,ppp);
		ll gap=abs(N[a]-(tempNA*powed+qqq));
		ll top=powed-gap;
		ll rank=K[a]-(limit-powed);

		ll next=0;
		ll mid=0;
		ll left=0;
		ll right=0;
		ll maxR=0;
		ll minR=0;

		if(rank<=top)next=tempNA;
		else next=tempNA-1;
		mid=(next-1)/2;
		right=(next-1)-mid;
		left=mid;
		maxR=max(right,left);
		minR=min(right,left);
		res.push_back(pair<ll,ll>(maxR,minR));
	}
	for(ll a=0;a<T;++a)cout<<"Case #"<<a+1<<": "<<res[a].first<<" "<<res[a].second<<endl;
}
//int main(){
//	ll T;cin>>T;
//	for(ll a=0;a<T;++a){
//		ll b,c;
//		cin>>b>>c;
//		N.push_back(b);K.push_back(c);
//	}
//	for(ll a=0;a<T;++a){
//		vector<ll>rem;
//		vector<ll>strongRem;
//		vector<ll>weakRem;
//		rem.push_back(N[a]);
//		ll mid=0;
//		ll left=0;
//		ll right=0;
//		ll maxR=0;
//		ll minR=0;
//		ll maxtemp=-1;
//		for(ll b=0;b<K[a];++b){
//			if(rem.empty()){
//				copy(weakRem.begin(),weakRem.end(),std::back_inserter(strongRem));
//				rem=strongRem;strongRem.clear();weakRem.clear();
//				maxtemp=-1;
//			}
//			//if(b==K[a]-1)sort(rem.begin(),rem.end(),std::greater<ll>());
//			ll next=rem.front();
//			rem.erase(rem.begin());
//			mid=(next-1)/2;
//			left=(next-1)-mid;
//			right=mid;
//			if(maxtemp==-1)maxtemp=left;
//			if(left>=maxtemp)strongRem.push_back(left);
//			else weakRem.push_back(left);
//			if(right>=maxtemp)strongRem.push_back(right);
//			else weakRem.push_back(right);
//			maxR=max(right,left);
//			minR=min(right,left);
//		}
//		res.push_back(pair<ll,ll>(maxR,minR));
//	}
//	for(ll a=0;a<T;++a)cout<<"Case #"<<a+1<<": "<<res[a].first<<" "<<res[a].second<<endl;
//}
//int main(){
//	ll T;cin>>T;
//	for(ll a=0;a<T;++a){
//		ll b,c;
//		cin>>b>>c;
//		N.push_back(b);K.push_back(c);
//	}
//	for(ll a=0;a<T;++a){
//		vector<ll>rem;
//		ll mid=0;
//		ll left=0;
//		ll right=0;
//		rem.push_back(N[a]);
//		ll maxR=0;
//		ll minR=0;
//		for(ll b=0;b<K[a];++b){
//			ll next=rem.back();
//			rem.pop_back();
//			mid=(next-1)/2;
//			right=(next-1)-mid;
//			left=mid;
//			rem.push_back(right);
//			rem.push_back(left);
//			maxR=max(right,left);
//			minR=min(right,left);
//			sort(rem.begin(),rem.end());
//		}
//		res.push_back(pair<ll,ll>(maxR,minR));
//	}
//	for(ll a=0;a<T;++a)cout<<"Case #"<<a+1<<": "<<res[a].first<<" "<<res[a].second<<endl;
//}
