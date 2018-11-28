#include <cmath>
#include <cstdio>
#include <cstring>
#include <algorithm>

using namespace std;

int a[55],b[55][55],k[55],l[55][55],r[55][55];

int main()
{
	freopen("input.txt","r",stdin);
	freopen("output.txt","w",stdout);
	int test;scanf("%d",&test);
	for (int T=1;T<=test;T++)
	{
		int n,p;scanf("%d%d",&n,&p);
		for (int i=1;i<=n;i++) scanf("%d",&a[i]);
		for (int i=1;i<=n;i++)
		{
			for (int j=1;j<=p;j++) scanf("%d",&b[i][j]);
			sort(b[i]+1,b[i]+p+1);
			for (int j=1;j<=p;j++)
			{
				l[i][j]=(10*b[i][j]-1)/(a[i]*11)+1;
				r[i][j]=10*b[i][j]/(a[i]*9);
			}
		}
		int ans=0;
		for (int i=1;i<=n;i++) k[i]=1;
		while (1)
		{
			bool ok=1;
			for (int i=1;i<=n;i++) if (k[i]>p) {ok=0;break;}
			if (!ok) break;
			int L=0,R=10000000;
			for (int i=1;i<=n;i++)
			{
				L=max(L,l[i][k[i]]);
				R=min(R,r[i][k[i]]);
			}
			if (L<=R)
			{
				for (int i=1;i<=n;i++) k[i]++;
				ans++;
				continue;
			}
			int x=1;
			for (int i=2;i<=n;i++) if (r[i][k[i]]<r[x][k[x]]) x=i;
			k[x]++;
		}
		printf("Case #%d: %d\n",T,ans);
	}
	return 0;
}

