#include<cstdio>
#include<algorithm>
#include<cstring>

int t;

int n,p,A;
int r[55];
int q[55][55];

int tot[55];
int s[55][55];
int e[55][55];
int k[55];

int main()
{
//	freopen("B-large.in","r",stdin);
//	freopen("B-large.out","w",stdout);

	scanf("%d",&t);
	for(int test_case=1;test_case<=t;test_case++)
	{
		memset(r,0,sizeof(r[0])*55);
		memset(q,0,sizeof(q[0][0])*55*55);
		memset(tot,0,sizeof(tot[0])*55);
		memset(s,0,sizeof(s[0][0])*55*55);
		memset(e,0,sizeof(e[0][0])*55*55);
		memset(k,0,sizeof(k[0])*55);

		scanf("%d%d",&n,&p);
		for(int i=0;i<n;i++) scanf("%d",r+i);
		for(int i=0;i<n;i++) for(int j=0;j<p;j++)
		{
			scanf("%d",&q[i][tot[i]]);
			s[i][tot[i]]=(10*q[i][tot[i]])/(11*r[i]);
			if((10*q[i][tot[i]])%(11*r[i])!=0) s[i][tot[i]]++;
			e[i][tot[i]]=(10*q[i][tot[i]])/(9*r[i]);
			if(s[i][tot[i]]<=e[i][tot[i]]) tot[i]++;
		}
		for(int i=0;i<n;i++)
		{
			std::sort(s[i],s[i]+tot[i]);
			std::sort(e[i],e[i]+tot[i]);
		}

		A=0;
		for(int v=1;;)
		{
			bool kit=true;
			for(int i=0;i<n&&kit;i++)
			{
				for(;v>e[i][k[i]]&&k[i]<tot[i];k[i]++);
				if(k[i]==tot[i]) kit=false;
			}
			if(!kit) break;

			for(int i=0;i<n&&kit;i++) if(v<s[i][k[i]]) kit=false;
			if(!kit) v++;
			else
			{
				A++;
				for(int i=0;i<n;i++) k[i]++;
			}
		}
		printf("Case #%d: %d\n",test_case,A);
	}
	return 0;
}
