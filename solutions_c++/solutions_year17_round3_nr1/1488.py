#include <bits/stdc++.h>

using namespace std;
typedef long long ll;
#define N 1005
#define PI acos(-1)
int main(){
  	//freopen("in.txt","r",stdin);
  	//freopen("out.txt","w",stdout);
  	int t;
  	cin>>t;
  	for(int tc = 1; tc<=t;tc++){
  		ll n,k;
  		cin>>n>>k;
  		pair<ll,pair<ll,int> > rh[N];
  		ll r[N],h[N];
		for(int i = 0;i<n;i++){
			cin>>r[i]>>h[i];
			rh[i] = make_pair(r[i]*h[i],make_pair(r[i],i));
		} 
		sort(rh,rh+n);
		reverse(rh,rh+n); 	
		double ans = 0.0;
		for(int i = 0;i<n;i++){
			ll A = r[i]*r[i] + 2*r[i]*h[i];
			ll count = 0;
			if(k == 1){
				ans = max(ans,PI*A);
				continue;	
			}
			for(int j = 0;j<n;j++){
				if(rh[j].second.second != i && rh[j].second.first <= r[i]){
					count++;
					A+=2*rh[j].first;
				}
				if(count == k-1){
					ans = max(ans,PI*A);
					break;	
				}
			}
		}
		cout.precision(9);
		cout<<fixed<<"Case #"<<tc<<": "<<ans<<endl;	
	}
	return 0;
}

