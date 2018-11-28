#include<bits/stdc++.h>
#define endl '\n'
using namespace std;

int tt, n, pocz, kon, q, met[1010], w;
long double dp[1010], tab[210][210], tabb[210][210], inf = 1e18, z[1010], s[1010];
priority_queue< pair< long double, int > > Q;

void dijkstra()
{
	while( !Q.empty() )
	{
		w = Q.top().second;
		Q.pop();
		if( met[w] )continue;
		met[w] = 1;
		for( int a = 1; a <= n; a++ )
		{
			if( tab[w][a] != -1 && dp[a] > dp[w] + tab[w][a] )
			{
				dp[a] = dp[w] + tab[w][a];
				Q.push( make_pair( -dp[a], a ) );
			}
		}
	}
}
void dijkstra2()
{
	while( !Q.empty() )
	{
		w = Q.top().second;
		Q.pop();
		if( met[w] )continue;
		met[w] = 1;
		for( int a = 1; a <= n; a++ )
		{
			if( tabb[w][a] != -1 && dp[a] > dp[w] + tabb[w][a] )
			{
				dp[a] = dp[w] + tabb[w][a];
				Q.push( make_pair( -dp[a], a ) );
			}
		}
	}
}
int main()
{
	cin>>tt;
	cout<<setprecision( 10 )<<fixed;
	for( int ii = 1; ii <= tt; ii++ )
	{
		cin>>n>>q;
		cout<<"Case #"<<ii<<": ";
		for( int a = 1; a <= n; a++ )cin>>z[a]>>s[a];
		for( int a = 1; a <= n; a++ )
		{
			for( int b = 1; b <= n; b++ )
			{
				cin>>tab[a][b];
			}
		}
		for( int a = 1; a <= n; a++ )
		{
			for( int b = 1; b <= n; b++ )dp[b] = inf;
			for( int b = 1; b <= n; b++ )met[b] = 0;
			dp[a] = 0;
			Q.push( make_pair( -dp[a], a ) );
			dijkstra();
			for( int b = 1; b <= n; b++ )
			{
				if( z[a] >= dp[b] )tabb[a][b] = dp[b] / s[a];
				else tabb[a][b] = -1;
			}
		}
		for( int a = 1; a <= q; a++ )
		{
			cin>>pocz>>kon;
			for( int b = 1; b <= n; b++ )dp[b] = inf, met[b] = 0;
			dp[pocz] = 0;
			Q.push( make_pair( -dp[pocz], pocz ) );
			dijkstra2();
			cout<<dp[kon]<<" ";
		}
		cout<<endl;
	}
	
	return 0;
}
 

