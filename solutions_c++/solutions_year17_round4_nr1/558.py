#include <bits/stdc++.h>

using namespace std;

int T,n,p,x,res,cas,sum,f[4];

int main()
{
	for(cin>>T;T--;)
	{
		cin>>n>>p,res=1,sum=0;
		memset(f,0,sizeof(f));
		for(int i=0;i<n;i++)
			cin>>x,f[x%p]++,sum+=x;
		
		if(p==2)
			res+=f[0]+f[1]/2;
		if(p==3)
		{
			int x=min(f[1],f[2]),y=max(f[1],f[2]),z=y-x;
			res+=f[0]+x+z/3;
		}
		if(p==4)
		{
			int x=min(f[1],f[3]),y=max(f[1],f[3]),z=y-x;
			res+=f[0]+x;

			if(z>f[2]+f[2])
				res+=f[2]+(z-f[2]-f[2])/4;
			else
				res+=z/2+(f[2]-z/2)/2;
		}
		if(sum%p==0)
			res--;
		printf("Case #%d: %d\n",++cas,res);
	}
}