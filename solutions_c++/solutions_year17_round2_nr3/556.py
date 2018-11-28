#include<stdio.h>
#include<iostream>
#include<algorithm>

using namespace std;

int n,m,mp[101][101];
long long int mp2[101][101];
long double mp3[101][101];
pair<int,long double> h[101];
long double dist[101];

int main()
{
	freopen("input.txt","r",stdin);
	freopen("output.txt","w",stdout);
	int t,i,j,k;

	scanf("%d",&t);

	for(int tt=1;tt<=t;tt++)
	{
		scanf("%d%d",&n,&m);

		if(n==100)
		{
			int t=1;
		}
		for(i=1;i<=n;i++)
		{
			scanf("%d%lf",&h[i].first,&h[i].second);
			dist[i]=-1;
		}

		for(i=1;i<=n;i++)for(j=1;j<=n;j++){
				scanf("%d",&mp[i][j]);
				mp2[i][j]=mp[i][j];
				mp3[i][j]=0;
		}

		int k;
		for(k=1;k<=n;k++)for(i=1;i<=n;i++)for(j=1;j<=n;j++)
		{
			if(mp2[i][k]!=-1&&mp2[k][j]!=-1&&(mp2[i][j]==-1||mp2[i][j]>mp2[i][k]+mp2[k][j]))
			{
				mp2[i][j] = mp2[i][k]+mp2[k][j];
			}
		}

		for(i=1;i<=n;i++)
		{
			for(j=1;j<=n;j++)
			{
				if(mp2[i][j]!=-1&&h[i].first>=mp2[i][j])
				{
					mp3[i][j] = (double)(mp2[i][j])/h[i].second;
				}
				else mp3[i][j]=-1;
			}
		}

		for(k=1;k<=n;k++)for(i=1;i<=n;i++)for(j=1;j<=n;j++)
		{
			if(mp3[i][k]!=-1&&mp3[k][j]!=-1&&(mp3[i][j]==-1||mp3[i][j]>mp3[i][k]+mp3[k][j]))
			{
				mp3[i][j] = mp3[i][k]+mp3[k][j];
			}
		}
		int a,b;

		printf("Case #%d:",tt);
		//cout << "Case #" << tt;
		for(i=1;i<=m;i++)
		{
			scanf("%d%d",&a,&b);
			printf(" %lf",mp3[a][b]);
			//cout << " " << mp3[a][b];
		}
		puts("");
		//cout << endl;
	}
	return 0;
}