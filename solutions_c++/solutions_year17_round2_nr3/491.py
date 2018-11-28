#include<bits/stdc++.h>
using namespace std;
#define FOR(i,s,e) for(int i = (s); i < (e); i++)
#define FOE(i,s,e) for(int i = (s); i <= (e); i++)
#define FOD(i,s,e) for(int i = (s); i >= (e); i--)
#define ll long long
#define pb push_back

int tc, n, tt, QQ, w, x, y;
int a, b;
ll dist[105][105], len[105], speed[105];
double dist2[105][105];

int main ()
{
	scanf("%d", &tc);
	while (tc--)
	{
		scanf("%d %d", &n, &QQ);
		FOE(i, 1, n) scanf("%lld %lld", &len[i], &speed[i]);
		FOE(i, 1, n) FOE(j, 1, n) scanf("%lld", &dist[i][j]);
		
		FOE(k, 1, n) FOE(i, 1, n) FOE(j, 1, n) 
		{
			if (dist[i][k] == -1ll || dist[k][j] == -1ll) continue;
			if (dist[i][j] == -1ll || dist[i][j] > dist[i][k] + dist[k][j]) 
				dist[i][j] = dist[i][k] + dist[k][j];
		}
		
		FOE(i, 1, n) FOE(j, 1, n) if (dist[i][j] > len[i]) dist[i][j] = -1ll;
		
		FOE(i, 1, n) FOE(j, 1, n) 
		{
			if (dist[i][j] == -1ll) dist2[i][j] = -1.0;
			else dist2[i][j] = (double)dist[i][j] / (double)speed[i];
		}
		
		FOE(k, 1, n) FOE(i, 1, n) FOE(j, 1, n)
		{
			if (dist2[i][k] < -0.5 || dist2[k][j] < -0.5) continue;
			if (dist2[i][j] < -0.5 || dist2[i][j] > dist2[i][k] + dist2[k][j]) 
				dist2[i][j] = dist2[i][k] + dist2[k][j];
		}
		
		printf("Case #%d:", ++tt);
		
		while (QQ--)
		{
			scanf("%d %d", &x, &y);
			printf(" %.10lf", dist2[x][y]);
		}
		printf("\n");
	}
	
	return 0;
}

