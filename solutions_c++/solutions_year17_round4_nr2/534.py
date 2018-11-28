#include <bits/stdc++.h>

using namespace std;

const int N=1<<10;

int T,c,n,m,x,y,cas,res,pro,f[N],g[N];

int main()
{
	for(cin>>T;T--;)
	{
		cin>>n>>c>>m,res=pro=0;
		memset(f,0,sizeof(f));
		memset(g,0,sizeof(g));
		for(int i=0;i<m;i++)
			scanf("%d%d",&x,&y),f[x]++,g[y]++,res=max(res,g[y]);

		int s=0;
		for(int i=1;i<=n;i++)
			s+=f[i],res=max(res,(s+i-1)/i);
		for(int i=1;i<=n;i++)
			pro+=max(0,f[i]-res);
		printf("Case #%d: %d %d\n",++cas,res,pro);
	}
}