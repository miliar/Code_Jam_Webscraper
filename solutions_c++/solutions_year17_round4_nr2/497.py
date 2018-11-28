#include<cstdio>
#include<cstring>
#include<algorithm>
#define fo(i,a,b) for(int i=a;i<=b;i++)
using namespace std;

const int maxn=1005;

int n,m,c,b[maxn],p[maxn],num[maxn];

int calc(int mid)
{
	int res=0, now=0, re=0;
	fo(i,1,m)
	{
		if (p[i]!=p[i-1]) res+=mid*(p[i]-p[i-1]), now=mid;
		if (res<=0) return -1;
		res--;
		if (now) now--; else re++;
	}
	return re;
}

int T;
int main()
{
	//freopen("B.in","r",stdin);	
	//freopen("B.out","w",stdout);
	
	scanf("%d",&T);
	fo(Ti,1,T)
	{
		printf("Case #%d: ",Ti);
		
		scanf("%d %d %d",&n,&c,&m);
		memset(num,0,sizeof(num));
		fo(i,1,m)
		{
			scanf("%d %d",&p[i],&b[i]);
			num[b[i]]++;
		}
		sort(p+1,p+1+m);
		
		int l=0, r=m, ans=0;
		fo(i,1,c) l=max(l,num[i]);
		while (l<=r)
		{
			int mid=(l+r)>>1;
			int t=calc(mid);
			if (t>-1) r=mid-1, ans=t; else l=mid+1;
		}
		
		printf("%d %d\n",r+1,ans);
	}
}