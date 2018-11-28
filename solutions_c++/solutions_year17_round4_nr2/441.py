#include<cstdio>
#include<string>
#include<cstring>
#include<iostream>
#include<algorithm>
using namespace std;
struct tic
{
	int p,b;
}a[1001];
int s[1001],sx[1001];
int n,c,m;
inline int check(int mid)
{
	int la=0,i;
	int ax=0;
	for(i=n;i>=1;i--)
	{
		if(sx[i]+la>mid)
		{
			ax+=max(0,mid-sx[i]);
			la=la+sx[i]-mid;
		}
		else
		{
			ax+=la;
			la=0;
		}
	}
	if(la==0)
		return ax;
	return -1;
}
int main()
{
//	freopen("B-small-attempt0.in","r",stdin);
//	freopen("B-small-attempt0.out","w",stdout);
	freopen("B-large.in","r",stdin);
	freopen("B-large.out","w",stdout);
	int T,kk=0;
	scanf("%d",&T);
	while(T>0)
	{
		kk++;
		T--;
		scanf("%d%d%d",&n,&c,&m);
		int i;
		memset(s,0,sizeof(s));
		memset(sx,0,sizeof(sx));
		for(i=1;i<=m;i++)
		{
			scanf("%d%d",&a[i].p,&a[i].b);
			s[a[i].b]++;
			sx[a[i].p]++;
		}
		int ans=0;
		for(i=1;i<=c;i++)
			ans=max(ans,s[i]);
	//	sort(a+1,a+1+m);
		int l=1,r=1000000;
		while(l<=r)
		{
			int mid=(l+r)/2;
			int xt=check(mid);
			if(xt!=-1)
				r=mid-1;
			else
				l=mid+1;
		}
		ans=max(ans,l);
		printf("Case #%d: %d %d\n",kk,ans,check(ans));
	}
	return 0;
}
