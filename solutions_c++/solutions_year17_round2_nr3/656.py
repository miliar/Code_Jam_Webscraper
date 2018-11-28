#include <bits/stdc++.h>
using namespace std;
#define LD long double
#define LL long long
const int mxn = 110;
const LL INF = 1e13 + 10;

int n, q;
LL e[mxn], v[mxn];
LL d[mxn][mxn];
LD wyn[mxn][mxn];

void FW()
{
	for(int a = 1 ; a <= n ; a++)
		for(int b = 1 ; b <= n ; b++)
			for(int c = 1 ; c <= n ; c++)
				d[b][c] = min(d[b][c], d[b][a] + d[a][c]);
}

void FWwyn()
{
	for(int a = 1 ; a <= n ; a++)
		for(int b = 1 ; b <= n ; b++)
			for(int c = 1 ; c <= n ; c++)
				wyn[b][c] = min(wyn[b][c], wyn[b][a] + wyn[a][c]);
}


LD solve()
{
	scanf("%d%d", &n, &q);
	for(int i = 1 ; i <= n ; i++)
		scanf("%lld%lld", &e[i], &v[i]);
	for(int i = 1 ; i <= n ; i++)
	{
		for(int j = 1 ; j <= n ; j++)
		{
			LL x;
			scanf("%lld", &x);
			if(x == -1LL)
				d[i][j] = INF;
			else
				d[i][j] = x;
		}
	}
	FW();
	for(int i = 1 ; i <= n ; i++)
		for(int j = 1 ; j <= n ; j++)
			wyn[i][j] = (LD)INF;
	for(int i = 1 ; i <= n ; i++)
		for(int j = 1 ; j <= n ; j++)
			if(d[i][j] <= e[i])
				wyn[i][j] = (LD)d[i][j] / (LD)v[i];
	
	
	FWwyn();
	
	
	
	for(int i = 1 ; i <= q ; i++)
	{
		int a, b;
		scanf("%d%d", &a, &b);
		printf("%.10Lf ", wyn[a][b]);
	}
}


int main()
{
	int t;
	scanf("%d", &t);
	for(int i = 1 ; i <= t ; i++)
	{
		printf("Case #%d: ", i);
		solve();
		printf("\n");
	}
}
