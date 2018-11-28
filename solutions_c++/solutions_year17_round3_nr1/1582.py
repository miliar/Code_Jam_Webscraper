#include<bits/stdc++.h>
#define MAXN 100010
#define pb push_back
#define mp make_pair

using namespace std;

vector<pair<long double,long double>>v;

int main(){
	freopen("cj.in","r",stdin);
	freopen("cj.out","w",stdout);
	int t;
	scanf("%d",&t);
	for(int te=1;te<=t;te++){
		long long int n,k,r,h;
		scanf("%lld%lld",&n,&k);
		for(int i=0;i<n;i++){
			scanf("%lld%lld",&r,&h);
			v.pb(mp((long double)h*(long double)r,(long double)r));
		}
		sort(v.begin(),v.end(),greater<pair<long double,long double>>());
		long double pi=M_PI,mx=0.0;
		for(int i=0;i<n;i++){
			long double ar=pi*v[i].second*v[i].second+(long double)2*pi*v[i].first;
			int cnt=0;
			for(int j=0;j<n;j++){
				if(cnt==k-1)
					break;
				if(j!=i && v[i].second>=v[j].second){
					ar+=2*pi*v[j].first;
					cnt++;
				}
			}
			if(cnt==k-1)
				mx=max(mx,ar);
		}
		v.clear();
		printf("Case #%d: %.10Lf\n",te,mx);
	}
	return 0;
}
