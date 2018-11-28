#include<stdio.h>

int n,m,g[101],p[5];

int main()
{
	freopen("C:\\Users\\Administrator\\Downloads\\A-small-attempt0.in","r",stdin);
	freopen("output.txt","w",stdout);

	int t,i,j;
	scanf("%d",&t);

	for(int tt=1;tt<=t;tt++)
	{
		scanf("%d%d",&n,&m);
		for(i=0;i<m;i++)p[i]=0;
		for(i=1;i<=n;i++)
		{
			scanf("%d",&g[i]);
			p[g[i]%m]++;
		}

		int ans = p[0];
		if(m==2) ans += (p[1]+1)/2;
		else if(m==3)
		{
			if(p[1]>p[2]){
				ans += p[2];
				p[1]-=p[2];
				ans+=(p[1]+2)/3;
			}
			else
			{
				ans += p[1];
				p[2]-=p[1];
				ans += (p[2]+2)/3;
			}
		}
		else
		{
			ans += p[2]/2;
			p[2]%=2;
			if(p[1]>p[3])
			{
				ans +=p[3];
				p[1]-=p[3];
				if(p[2]==1&&p[1]>1)
				{
					ans++;
					p[1]-=2;
				}
				ans += (p[1]+3)/4;
			}
			else
			{
				ans += p[1];
				p[3]-=p[1];
				if(p[2]==1&&p[3]>2)
				{
					ans++;
					p[3]-=2;
				}
				ans += (p[3]+3)/4;
			}
		}

		printf("Case #%d: %d\n",tt,ans);
	}

	return 0;
}