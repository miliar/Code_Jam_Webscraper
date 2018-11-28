#include<bits/stdc++.h>
using namespace std;
typedef long long ll;
const int maxn=1440;
void ioinit()
{
	freopen("B-large.in","r",stdin);
	freopen("B-large.out","w",stdout);
}
int a[1500];
struct Node
{
	int l,d;
	Node(){}
	Node(int _l,int _d):l(_l),d(_d){}
	bool operator < (const Node &r ) const
	{
		return d<r.d;
	}
};
vector<Node> itv;
int main()
{
	ioinit();
	int T,kase=1;
	scanf("%d",&T);
	int n,m;
	while(~scanf("%d%d",&n,&m))
	{
		itv.clear();
		memset(a,-1,sizeof(a));
		int u,v;
		int C=720,J=720;
		//puts("INPUT:");
		//printf("%d %d\n",n,m);
		for(int i=0;i<n;i++)
		{
			scanf("%d%d",&u,&v);
			//printf("%d %d\n",u,v);
			C-=v-u;
			for(int j=u;j<v;j++) a[j]=0;
		}
		for(int i=0;i<m;i++)
		{
			scanf("%d%d",&u,&v);
			//printf("%d %d\n",u,v);
			J-=v-u;
			for(int j=u;j<v;j++) a[j]=1;
		}
		for(int i=0;i<maxn;i++)
		{
			if(a[i]==0&&a[(i+1)%maxn]==-1)
			{
				for(int j=(i+1)%maxn;;j=(j+1)%maxn)
				{
					if(a[j]==0)
					{
						itv.push_back(Node((i+1)%maxn,(j-i-1+maxn)%maxn));
						break;
					}
					else if(a[j]==1) break;
				}
			}
		}
		sort(itv.begin(),itv.end());
		int it=0;
		while(it<itv.size()&&itv[it].d<=C)
		{
			C-=itv[it].d;
			int l=itv[it].l;
			for(int i=0;i<itv[it].d;i++)
				a[(l+i)%maxn]=0;
			++it;
		}
		itv.clear();
		for(int i=0;i<maxn;i++)
		{
			if(a[i]==1&&a[(i+1)%maxn]==-1)
			{
				for(int j=(i+1)%maxn;;j=(j+1)%maxn)
				{
					if(a[j]==1)
					{
						itv.push_back(Node((i+1)%maxn,(j-i-1+maxn)%maxn));
						break;
					}
					else if(a[j]==0) break;
				}
			}
		}
		sort(itv.begin(),itv.end());
		it=0;
		while(it<itv.size()&&itv[it].d<=J)
		{
			J-=itv[it].d;
			int l=itv[it].l;
			for(int i=0;i<itv[it].d;i++)
				a[(l+i)%maxn]=1;
			++it;
		}
		for(int i=0;i<maxn&&C>0;i++)
		{
			if(a[i]==0)
			{
				for(int j=1;a[(i-j+maxn)%maxn]==-1&&C>0;j++) a[(i-j+maxn)%maxn]=0,--C;
				for(int j=1;a[(i+j)%maxn]==-1&&C>0;j++) a[(i+j)%maxn]=0,--C;
			}
		}
		for(int i=0;i<maxn&&J>0;i++)
		{
			if(a[i]==1)
			{
				for(int j=1;a[(i-j+maxn)%maxn]==-1&&J>0;j++) a[(i-j+maxn)%maxn]=1,--J;
				for(int j=1;a[(i+j)%maxn]==-1&&J>0;j++) a[(i+j)%maxn]=1,--J;
			}
		}
		for(int i=0;i<maxn&&C>0;i++)
			if(a[i]==-1) a[i]=0,--C;
		for(int i=0;i<maxn;i++) if(a[i]==-1) a[i]=1;
		int ans=0;/*
		for(int i=0;i<24;i++)
		{
			for(int j=0;j<60;j++)
				printf("%d",a[i*60+j]);
			puts("");
		}*/
		//puts("OUTPUT:");
		for(int i=1;i<=maxn;i++)
			if(a[i%maxn]!=a[i-1]) ans++;
		printf("Case #%d: %d\n",kase++,ans);
	}
	return 0;
}
