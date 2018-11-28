#include <iostream>
#include <bits/stdc++.h>
using namespace std;
const long double INF = 1e13;

long double e[105], s[105];
long double d[105][105];
long double dis[105];
int n;
long double dp[105][105];

long double fun(int pos, int h)
{
	if(dis[pos] - dis[h] > e[h])
		return INF;
	if(pos == n)
		return 0;

	if(dp[pos][h] != -1)
		return dp[pos][h];

	dp[pos][h] =  min( d[pos][pos+1]/s[h] + fun(pos+1, h),

		        d[pos][pos+1]/s[pos] + fun(pos+1, pos));

	return dp[pos][h];
}

int main()
{
    FILE *fp = fopen("A.txt", "w");
    int T;
    scanf("%d",&T);
    for(int t=1; t<=T; t++)
    {
        fprintf(fp, "Case #%d: ",t);
        int q;
        scanf(" %d %d", &n, &q);
        for(int i=1; i<=n; i++)
        	cin>>e[i]>>s[i];

        for(int i=1; i<=n; i++)
        	for(int j=1; j<=n; j++)
        		cin>>d[i][j];

        for(int i=2; i<=n; i++)
        {
        	dis[i] = dis[i-1] + d[i-1][i];
        	cout<<dis[i]<<" ";
        }

        int u, v;
        scanf("%d %d", &u, &v);

        for(int i=0; i<105; i++)
        	for(int j=0; j<105; j++)
        		dp[i][j] = -1;

        fprintf(fp, "%Lf\n",d[1][2]/s[1] + fun(2, 1) );
    }
    return 0;
}
