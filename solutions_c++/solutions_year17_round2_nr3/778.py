#include <bits/stdc++.h>
using namespace std;
typedef vector<int> vi;
typedef long long ll;
typedef vector<ll> vll;
typedef pair<int, int> Pii;
typedef pair<ll, ll> Pll;
#define pb push_back
#define fst first
#define snd second
int N, Q;
const ll INF = 1000000000000;
ll D[1000][1000];
double K[1000][1000];
ll E[1000];
ll S[1000];
void solve()
{
	scanf("%d%d", &N, &Q);
	for(int i =0; i < N; ++i)
		scanf("%lld%lld", &E[i], &S[i]);
	for(int i = 0; i < N; ++i)
	{
		for(int j = 0; j < N; ++j)
		{
			scanf("%lld", &D[i][j]);
			if(i == j) D[i][j] = 0;
			if(D[i][j] == -1)
				D[i][j] = INF;
		}
	}
	for(int i = 0; i < N; ++i)
		for(int j = 0; j < N; ++j)
			for(int k = 0; k < N; ++k)
			{
				D[j][k] = min(D[j][k], D[j][i] + D[i][k]);
			}
	for(int i = 0; i < N; ++i)
		for(int j = 0; j < N; ++j)
			K[i][j] = 1e18;
	for(int i = 0; i < N; ++i)
		for(int j = 0; j < N; ++j)
		{
			if(E[i] >= D[i][j])
				K[i][j] = min(K[i][j], ((double) D[i][j]) / S[i]);
		}
	
	for(int i = 0; i < N; ++i)
		for(int j = 0; j < N; ++j)
			for(int k = 0; k < N; ++k)
			{
				K[j][k] = min(K[j][k], K[j][i] + K[i][k]);
			}
	//puts("DEBUG");
	for(int i = 0; i < N; ++i)
		for(int j = 0; j < N; ++j)
		{
			//printf("D[%d][%d] = %lld\n", i, j, D[i][j]);
		}
	for(int i = 0; i < Q; ++i)
	{
		int u, v;
		scanf("%d%d", &u, &v);
		--u; --v;
		printf("%.9lf ", K[u][v]);
	}
	puts("");
}
int main()
{
	int T;
	scanf("%d", &T);
	for(int i = 1; i <= T; ++i)
	{
		printf("Case #%d: ", i);
		solve();
	}
	
	
	return 0;
}
