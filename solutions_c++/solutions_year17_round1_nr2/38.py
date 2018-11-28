#include<algorithm>
#include <iostream>
#include <stdlib.h>
#include <string.h>
#include  <stdio.h>
#include   <math.h>
#include   <time.h>
#include   <vector>
#include   <bitset>
#include    <queue>
#include      <set>
#include      <map>
using namespace std;

const int N=55;

int n,m,k[N],v[N][N],l[N][N],r[N][N],Now[N];
pair<int,int> H[N][N];

void solve()
{
	cin>>n>>m;
	for(int i=1;i<=n;i++)
		cin>>k[i],Now[i]=1;
	for(int i=1;i<=n;i++)
		for(int j=1;j<=m;j++)
		{
			cin>>v[i][j];
			l[i][j]=(v[i][j]/(double)k[i]/1.1+1);
			while((l[i][j]-1)*k[i]*1.1>=v[i][j])
				l[i][j]--;
			r[i][j]=(v[i][j]/(double)k[i]/0.9-1);
			while((r[i][j]+1)*k[i]*0.9<=v[i][j])
				r[i][j]++;
			if(r[i][j]<l[i][j])
				r[i][j]=l[i][j]-1;
			//cout<<i<<" "<<j<<" "<<l[i][j]<<" "<<r[i][j]<<endl;
			H[i][j]=make_pair(l[i][j],r[i][j]);
		}
	for(int i=1;i<=n;i++)
		sort(H[i]+1,H[i]+m+1);
	int Ans=0;
	while(1)
	{
		int ll=-1,rr=1e9;
		for(int i=1;i<=n;i++)
		{
			if(Now[i]>m)
			{
				cout<<Ans<<endl;return;
			}
			ll=max(ll,H[i][Now[i]].first);
			rr=min(rr,H[i][Now[i]].second);
		}
		if(ll<=rr)
		{
			Ans++;
			for(int i=1;i<=n;i++)
				Now[i]++;
		}
		else
		{
			for(int i=1;i<=n;i++)
				if(H[i][Now[i]].second==rr)
					Now[i]++;
		}
	}
}

int main()
{
#ifndef ONLINE_JUDGE
	freopen("B.in","r",stdin);
	freopen("B.out","w",stdout);
#endif
	int T;cin>>T;
	for(int i=1;i<=T;i++)
		printf("Case #%d: ",i),solve();
	return 0;
}

