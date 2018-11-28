#include <bits/stdc++.h>
using namespace std;

const int N = 101;
int n , t , q;
vector < pair < int , int > > v;
int a[N][N];
double dp[101][101];


double rec(int x , int have , int cur_speed , int horse)
{
	if(have < 0) return 1e16;
	
	if(x == n-1) return 0;
	
	if(dp[x][horse] > 0.0) return dp[x][horse];
	
	double dont = 1e16 , take = 1e16;
	if(cur_speed) dont = rec(x + 1 , have - a[x][x+1] , cur_speed , horse) + ((double)a[x][x+1]/(double)cur_speed);
	take = rec(x + 1 , v[x].first - a[x][x+1] , v[x].second , x) + ((double)a[x][x+1]/(double)v[x].second);
	
	return dp[x][horse] = min(dont , take);
}


int main()
{
	freopen("C-small-attempt2.in","r",stdin);
	freopen("output.txt","w",stdout);

	cin >> t;
	
	for(int ct=1;ct<=t;ct++)
	{
		for(int i=0;i<=100;i++)
			for(int j=0;j<=100;j++)
				dp[i][j] = -100;
			
		cin >> n >> q;
		
		v.clear();
		for(int i=0,distance,speed;i<n;i++)
		{
			scanf("%d%d",&distance,&speed);
			v.push_back(make_pair(distance,speed));
		}
		
		for(int i=0;i<n;i++)
		{
			for(int j=0;j<n;j++)
			{
				scanf("%d",&a[i][j]);
			}
		}
		
		int u , v;
		cin >> u >> v;
		
		printf("Case #%d: %.9llf\n",ct,rec(0 , 0 , 0 , 0));
	}
}
	