#include <bits/stdc++.h>
using namespace std;
#define ll long long
#define pii pair<ll,ll>

pii ck[1003];
pii srt[1003];
int rnk[1003];
ll sum[1003];
int main(){
	ll ans;
	int t,tt,n,m,i,j,k;
	cin >> t;
	for(tt=1;tt<=t;tt++){
		cin >> n >> k;
		for(i=0;i<n;i++){
			cin >> ck[i].first >> ck[i].second;
			srt[i].first = ck[i].first*ck[i].second;
			srt[i].second=i;
		}
		sort(srt,srt+n);
		for(i=0;i<n;i++){
			rnk[srt[i].second]=i;
			sum[i]=srt[i].first;
		}
		for(i=1;i<n;i++)
			sum[i]+=sum[i-1];
		for(i=0,ans=0;i<n;i++){
              //  cout<<i<<"  "<<rnk[i]<<"  "<<sum[i]<<"\n";
			if(rnk[i]>=n-k)
				ans=max(ans,ck[i].first*ck[i].first+
					2*(sum[n-1]-sum[n-k-1]));
			else
				ans=max(ans,ck[i].first*ck[i].first+
					2*ck[i].first*ck[i].second+
					2*(sum[n-1]-sum[n-k]));
		}
		printf("Case #%d: %.9lf\n",tt,ans*M_PI);
	}
}
