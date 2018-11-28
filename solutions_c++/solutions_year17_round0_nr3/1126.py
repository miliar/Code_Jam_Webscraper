#include <bits/stdc++.h>
using namespace std;
map<long long,long long> m[100];
int main(){
	int T;
	cin>>T;
	for(int t=1;t<=T;t++){
		long long n,k;
		cin>>n>>k;
		int times = 0;
		long long ans = -1ll;
		m[0].clear();
		m[0][-n] = 1;
		int idx=0;
		while(1){
			m[times+1].clear();
			for(map<long long,long long>::iterator it = m[times].begin(); it!=m[times].end(); it++){
				//cout<<it->first<<" "<<it->second<<endl;
				if(k <= it->second){
					ans = -it->first;
					idx=1;
					break;
				}
				k -= it->second;
				long long x = -it->first;
				if(x%2) {
					m[times+1][-x/2ll] += 2ll*(it->second);
				}
				else{
					m[times+1][-x/2ll] += (it->second);
					m[times+1][-x/2ll+1ll] += (it->second);
				}
			}
			times++;
			if(idx) break;
		}

		if(ans%2) printf("Case #%d: %lld %lld\n",t,ans/2ll,ans/2ll);
		else printf("Case #%d: %lld %lld\n",t,ans/2ll,ans/2ll-1ll);
	}
}