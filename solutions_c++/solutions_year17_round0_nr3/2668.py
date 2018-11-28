#include<bits/stdc++.h>
using namespace std;

#define scl(x) scanf("%lld",&x)
#define sc(x)  scanf("%d",&x)
#define ll long long
#define lop(i,n) for(int i=0;i<n;++i)
typedef pair<int, int> ii;
typedef pair<ll, ll> pll;


int main(){
#ifndef ONLINE_JUDGE
	freopen("i.txt","r",stdin);
	freopen("o.txt","w",stdout);
#endif
	int t;
	sc(t);
	lop(C,t){
		printf("Case #%d: ",C+1);
		ll n,k;
		scl(n);
		scl(k);
		map<ll,ll> mp;
		mp[n]=1;
		while(1){
			ll v=mp.rbegin()->first;
			ll c=mp.rbegin()->second;
			v--;
			k-=c;
			if(k<=0){
				printf("%lld %lld\n",(v+1)/2,v/2);
				break;
			}
			mp[(v+1)/2]+=c;
			mp[v/2]+=c;
			mp.erase(mp.rbegin()->first);
		}
	}
}
