#include <bits/stdc++.h>
using namespace std;

#define FOR(i,l,r) for(int i = (int) (l);i < (int) (r);i++)
#define ALL(x) x.begin(),x.end()
template<typename T> bool chmax(T& a,const T& b){ return a < b ? (a = b,true) : false; }
template<typename T> bool chmin(T& a,const T& b){ return b < a ? (a = b,true) : false; }
typedef long long ll;

int T;
ll N,K;
map<ll,ll> mp;

int main()
{
	scanf("%d",&T);
	FOR(testCase,1,T + 1){
		scanf("%lld%lld",&N,&K);

		mp.clear();
		mp [N]++;
		priority_queue<ll> pq;
		pq.push(N);
		while(pq.empty() == false){
			ll curr = pq.top();
			pq.pop();

			if(curr == 0) continue;
			if(curr % 2 == 0){
				if(mp.count(curr / 2 - 1) == 0) pq.push(curr / 2 - 1);
				if(mp.count(curr / 2) == 0) pq.push(curr / 2);
				mp [curr / 2 - 1] += mp [curr];
				mp [curr / 2] += mp [curr];
			}
			else{
				if(mp.count(curr / 2) == 0) pq.push(curr / 2);
				mp [curr / 2] += mp [curr] * 2;
			}
		}

		ll curr = 0;
		for(auto it = mp.rbegin();it != mp.rend();it++){
			if(K <= curr + it->second){
				if(it->first % 2 == 0){
					printf("Case #%d: %lld %lld\n",testCase,it->first / 2,it->first / 2 - 1);
					break;
				}
				else{
					printf("Case #%d: %lld %lld\n",testCase,it->first / 2,it->first / 2);
					break;
				}
			}
			curr += it->second;
		}
	}

	return 0;
}
