#include "bits/stdc++.h"
using namespace std;
int t;
long long n , k;
map < long long , long long > mp;
int main(){
	scanf("%d" , &t);
	for(int tc = 1 ; tc <= t ; ++tc){
		printf("Case #%d: " , tc);
		scanf("%lld %lld" , &n , &k);
		mp.clear();
		mp[n] = 1;
		long long ans;
		while(1){
			auto it = *prev(mp.end());
			mp.erase(prev(mp.end()));
			if(it.second >= k){
				ans = it.first;
				break;
			}
			else{
				k -= it.second;
				mp[it.first >> 1] += it.second;
				mp[it.first - 1 >> 1] += it.second;
			}
		}
		printf("%lld %lld\n" , ans >> 1 , ans - 1 >> 1);
	}
}