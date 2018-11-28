//hi
#include<bits/stdc++.h>
using namespace std;
#define PB push_back
#define MP make_pair
#define F first
#define S second
typedef long long int LL;
priority_queue< pair<LL,LL> > pq;
map<LL,LL> mp;
LL n,k;
LL sol(){
	while(1){
		pair<LL,LL> a;
		mp.clear();
		//int gg=0;
		while(!pq.empty()){ //2
			a=pq.top();
			pq.pop();
			//gg++;
			if(a.S>=k){
				return a.F-1;
			}else{
				k-=a.S;
				a.F--;
				if(a.F%2==0){
					mp[a.F/2]+=a.S*2;
				}else{
					mp[a.F/2]+=a.S;
					mp[a.F/2+1]+=a.S;
				}
			}
		}
		//if(gg>2) printf("ddd\n");
		for(auto it=mp.begin();it!=mp.end();it++)
			pq.push(MP(it->F, it->S));
	}
}
int main(void){
    int t;
    scanf("%d",&t);
    for(int hh=1;hh<=t;hh++){
		scanf("%lld%lld",&n,&k);
		while(!pq.empty()) pq.pop();
		pq.push(MP(n,1));
		LL ans=sol();
		if(ans%2==0) printf("Case #%d: %lld %lld\n",hh,ans/2, ans/2);
		else printf("Case #%d: %lld %lld\n",hh,ans/2+1, ans/2);
	}
    return 0;
}
