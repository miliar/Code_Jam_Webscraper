#include<bits/stdc++.h>
using namespace std;

#define sd(mark) scanf("%d",&mark)
#define ss(mark) scanf("%s",mark)
#define sl(mark) scanf("%lld",&mark)
#define debug(mark) printf("check%d\n",mark)
#define clr(mark) memset(mark,0,sizeof(mark))
#define MP make_pair
#define PB push_back
#define F first
#define S second
#define ll long long
#define N 60
#define M 1200000
int cnt[N][M];
pair<int,int> packages[N][N];
int r[N];
int ptr[N];
int Find(ll q, ll r, ll frac)
{
	ll lo=0, hi = M, mid;
	while(lo<hi)
	{
		mid=(lo+hi)/2;
		if(mid*frac*r>=q*10)
			hi=mid;
		else
			lo=mid+1;
	}
	return lo;
}

int main()
{
	// freopen("B1.in","r",stdin);
	// freopen("B1.out","w",stdout);
	int t,i,j,k;
	sd(t);
	for(int tt=1;tt<=t;++tt)
	{
		cerr<<tt<<'\n';
		clr(cnt);
		int n,p;
		sd(n);sd(p);
		for(i=0;i<n;i++)
			sd(r[i]);
		for(i=0;i<n;i++)
		{
			for(j=0;j<p;j++)
			{
				int q;
				sd(q);
				int lo=Find(q,r[i],11);
				int hi=Find(q+1,r[i],9)-1;
				cnt[i][lo]++;
				cnt[i][hi+1]--;
				packages[i][j]=MP(lo,hi);
			}
			for(j=1;j<M;j++)
				cnt[i][j]+=cnt[i][j-1];
			sort(packages[i],packages[i]+p);
		}
		for(i=0;i<n;i++)
			ptr[i]=0;
		int ans=0;
		for(i=0;i<M;i++)
		{
			while(true)
			{
				for(j=0;j<n;j++)
				{
					while(ptr[j]<p)
					{
						if(packages[j][ptr[j]].S>=i)	break;
						ptr[j]++;
					}
				}
				for(j=0;j<n;j++)
					if(!cnt[j][i])
						break;
				if(j<n)	break;
				ans++;
				for(j=0;j<n;j++)
				{
					for(k=packages[j][ptr[j]].F;k<=packages[j][ptr[j]].S;k++)
						cnt[j][k]--;
					ptr[j]++;
				}
			}
		}
		printf("Case #%d: %d\n",tt,ans);
	}
}