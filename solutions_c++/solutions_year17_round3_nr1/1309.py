#include <bits/stdc++.h>
using namespace std;

typedef pair<long long, long long> pll;
int t,n,k;
long long r[1005],h[1005];
pll area[1005]; //height area, surface area
long long tmpmax;
map<long long, long long> mp;

int main(){
	freopen("A-small-attempt0.in","r",stdin);
	freopen("A-small.out","w",stdout);
	scanf("%d",&t);
	for(int tc=1;tc<=t;tc++){
		scanf("%d%d",&n,&k);
		for(int i=0;i<n;i++){
			scanf("%lld%lld",&r[i],&h[i]);
		}
		for(int i=0;i<n;i++){
			area[i]=pll(2*r[i]*h[i],r[i]*r[i]);
		}
		for(int i=0;i<n;i++){
			mp[area[i].first]=r[i];
		}
		sort(area,area+n);
		reverse(area,area+n);
		tmpmax=0;
		for(int i=0;i<n;i++){
			//printf("%lld %lld\n",area[i].first,area[i].second);
		}
		for(int i=0;i<n;i++){
			long long tmp=area[i].first+area[i].second;
			int cnt=1;
			for(int j=0;j<n;j++){
				if(i==j) continue;
				if(mp[area[j].first]>mp[area[i].first]) continue;
				if(cnt==k) break;
				cnt++;
				tmp+=area[j].first;
			}
			//printf("%lld\n",tmp);
			tmpmax=max(tmpmax,tmp);
		}
		printf("Case #%d: %lf\n",tc,tmpmax*3.14159265359);
	}
}
