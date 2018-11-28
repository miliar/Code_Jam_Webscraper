#include<cstdio>
#include<cstdlib>
#include<cstring>
#include<algorithm>
#include<iostream>
using namespace std;
int n,m;
int R[1005];
int Q[1005][1005];
int l[1005][1005],r[1005][1005],cur[1005];
int main()
{
	freopen("b.in","r",stdin);
	freopen("b.out","w",stdout);
	int T=0;
	scanf("%d",&T);
	for(int qi=1;qi<=T;qi++)
	{
		printf("Case #%d: ",qi);
		scanf("%d%d",&n,&m);
		for(int i=1;i<=n;i++)
			scanf("%d",R+i);
		for(int i=1;i<=n;i++)
		{
			cur[i]=1;
			for(int j=1;j<=m;j++)
				scanf("%d",&Q[i][j]);
			sort(Q[i]+1,Q[i]+m+1);
			for(int j=1;j<=m;j++)
				l[i][j]=max(1,(Q[i][j]*10-1)/(11*R[i])+1),
				r[i][j]=(Q[i][j]*10)/(9*R[i]);
		}
		int ans=0;
		while(1)
		{
			int t=-1,flag=1;
			for(int i=1;i<=n;i++)
				if(cur[i]<=m)
				{
					if(t==-1||r[i][cur[i]]<r[t][cur[t]])
						t=i;
				}
				else flag=0;
			if(flag==0)break;
			flag=1;
			for(int i=1;i<=n;i++)
				if(l[i][cur[i]]>r[t][cur[t]])flag=0;
			if(flag)
			{
				ans++;
				for(int i=1;i<=n;i++)cur[i]++;
			}
			else cur[t]++;
		}
		cout<<ans<<endl;
	}
	return 0;
}

