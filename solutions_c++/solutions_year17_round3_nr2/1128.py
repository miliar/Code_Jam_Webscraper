#include<bits/stdc++.h>
#define rep(i,j,k) for(int i=(j);i<(k);i++)
#define mp make_pair
#define sz(a) (int)(a).size()
#define pb push_back
using namespace std;
typedef long long ll;
typedef pair<int,int> pii;
typedef long double ld;
//----head----
int t[1500];
pii data1[105],data2[105];
vector<int> V,V2;
int cmpp(int a,int b)
{
	return a>b;
}
int main()
{
	freopen("0.in","r",stdin);
	freopen("0.out","w",stdout);
	int T;
	scanf("%d",&T);
	rep(cas,1,T+1)
	{
		int an=0;
		memset(t,0,sizeof(t));
		V.clear();
		V2.clear();
		int a,b,res=720;
		scanf("%d%d",&a,&b);
		if(a==0)swap(a,b);
		rep(i,0,a)
		{
			scanf("%d%d",&data1[i].first,&data1[i].second);
			rep(j,data1[i].first,data1[i].second)t[j]=1;
			res-=data1[i].second-data1[i].first;
		}
		rep(i,0,b)
		{
			scanf("%d%d",&data2[i].first,&data2[i].second);
			rep(j,data2[i].first,data2[i].second)t[j]=2;
		}
		if(a<2&&b<2)
		{
			printf("Case #%d: %d\n",cas,2);
			continue;
		}
		sort(data1,data1+a);
		sort(data2,data2+b);
		int ans=a<<1;
		rep(i,0,a-1)
		{
			int l=data1[i].second;
			int r=data1[i+1].first;
			int flag=1;
			rep(j,l,r)
			{
				if(t[j]==0&&flag==0)
				{
					flag=3;
					l=j;
				}
				if(t[j]==2)
				{
					if(flag==1)an+=j-l;
					else if(flag==3)V2.pb(j-l);
					flag=0;
				}
			}
			if(flag==1)V.pb(r-l);
			else if(flag==3)V2.pb(r-l);
		}
		int l=data1[a-1].second;
		int r=data1[0].first;
		int flag=1;
		rep(j,l,1440)
		{
			if(t[j]==0&&flag==0)
			{
				flag=3;
				l=j;
			}
			if(t[j]==2)
			{
				if(flag==1)an+=j-l;
				else if(flag==3)V2.pb(j-l);
				flag=0;
			}
		}
		rep(j,0,r)
		{
			if(t[j]==0&&flag==0)
			{
				flag=3;
				l=j+1440;
			}
			if(t[j]==2)
			{
				if(flag==1)an+=j+1440-l;
				else if(flag==3)V2.pb(1440+j-l);
				flag=0;
			}
		}
		if(flag)V.pb(1440-l+r);
		else V2.pb(1440+r-l);
		sort(V.begin(),V.end());
		sort(V2.begin(),V2.end(),cmpp);
		rep(i,0,sz(V))
		{
			if(res>=V[i])
			{
				res-=V[i];
				ans-=2;
			}
			else break;
		}
		res-=an;
		rep(i,0,sz(V2))if(res>0)
		{
			res-=V2[i];
			ans+=2;
		}
		printf("Case #%d: %d\n",cas,ans);
	}
	return 0;
}
