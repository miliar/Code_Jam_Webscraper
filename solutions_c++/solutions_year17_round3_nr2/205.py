#include <bits/stdc++.h>
using namespace std;
#define pii pair<int,int>

pair< pii, int > a[1500];
vector < int > v[2];
int main(){
	int rem[2];
	int t,tt,n,m,i,j,k;
	cin >> t;
	for(tt=1;tt<=t;tt++){
		cin >> n >> m;
		int ans=0;
		v[0].clear();
		v[1].clear();
		rem[0]=rem[1]=720;
		for(i=0;i<n;i++){
			cin >> a[i].first.first >> a[i].first.second;
			a[i].second=0;
			rem[0]-=(a[i].first.second-a[i].first.first);
		}
		for(;i<n+m;i++){
			cin >> a[i].first.first >> a[i].first.second;
			a[i].second=1;
			rem[1]-=(a[i].first.second-a[i].first.first);
		}
		sort(a,a+n+m);
		a[n+m].first.first=a[0].first.first+1440;
		a[n+m].second=a[0].second;
		for(i=0;i<n+m;i++){
			if(a[i].second==a[i+1].second){
				v[a[i].second].push_back(a[i+1].first.first-a[i].first.second);
			}
			else
				ans++;
		}
		sort(v[0].begin(), v[0].end());
		sort(v[1].begin(), v[1].end());
		for(i=0;i<v[0].size();i++)
			if(rem[0]>=v[0][i])
				rem[0]-=v[0][i];
			else
				ans+=2;
		for(i=0;i<v[1].size();i++)
			if(rem[1]>=v[1][i])
				rem[1]-=v[1][i];
			else
				ans+=2;
		printf("Case #%d: %d\n",tt,ans);
	}
}
