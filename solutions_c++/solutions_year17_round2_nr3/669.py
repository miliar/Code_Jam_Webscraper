#include<bits/stdc++.h>
using namespace std;
#define ll long long
#define mod 1000000007
int main()
{
	int t,z;
	cin>>t;
	for(z=1;z<=t;z++)
	{
		int n,q,i,j,k;
		cin>>n>>q;
		double val[n+1][2];
		for(i=1;i<=n;i++)
			cin>>val[i][0]>>val[i][1];
		double mat[101][101],gr[101][101];
		for(i=1;i<=n;i++)
		{
			for(j=1;j<=n;j++)
				cin>>mat[i][j];
		}
		printf("Case #%d: ",z);
		for(i=1;i<=n;i++)
		{
			for(j=1;j<=n;j++)
			{
				if(i==j)
					mat[i][j]=0;
				else
				{
					if(mat[i][j]==-1)
						mat[i][j]=111111111111;
				}
				gr[i][j]=mat[i][j];
			}
		}
		for(k=1;k<=n;k++)
		{
			for(i=1;i<=n;i++)
			{
				for(j=1;j<=n;j++)
				{
					if(gr[i][j]>=gr[i][k]+gr[k][j])
					{
						gr[i][j]=gr[i][k]+gr[k][j];
					}
				}
			}
		}
		double time[101][101];
		for(i=1;i<=n;i++)
		{
			for(j=1;j<=n;j++)
			{
			//	cout<<gr[i][j]<<" ";
				if(gr[i][j]>val[i][0])
					gr[i][j]=111111111111;
				time[i][j]=gr[i][j];
			}
		//	cout<<endl;
		}
		for(i=1;i<=n;i++)
		{
			for(j=1;j<=n;j++)
			{
				if(time[i][j]!=111111111111)
				{
					time[i][j]/=val[i][1];
				}
			}
		}
		for(k=1;k<=n;k++)
		{
			for(i=1;i<=n;i++)
			{
				for(j=1;j<=n;j++)
				{
					if(time[i][j]>=time[i][k]+time[k][j])
					{
						time[i][j]=time[i][k]+time[k][j];
					}
				}
			}
		}
		while(q--)
		{
			int u,v;
			cin>>u>>v;
			double ans=time[u][v];
			
			printf("%0.8lf ",ans);
		}
		printf("\n");
	}
	return 0;
}