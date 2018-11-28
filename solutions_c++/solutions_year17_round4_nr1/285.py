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

int P;
int dp[101][101][101][4];
int funk(int jeden, int dwa, int trzy, int reszta)
{
	if(dp[jeden][dwa][trzy][reszta] == 0)
	{
		int res = 0;
		if(reszta == 0)
		{
			if(jeden != 0)
				res = max(res, 1 + funk(jeden - 1, dwa, trzy, (reszta + 1) % P));
			if(dwa != 0)
				res = max(res, 1 + funk(jeden, dwa -1 , trzy, (reszta + 2) % P));
			if(trzy != 0)
				res = max(res, 1 + funk(jeden, dwa , trzy-1, (reszta + 3) % P));
		}
		else
		{
			if(jeden != 0)
				res = max(res, funk(jeden - 1, dwa, trzy, (reszta + 1) % P));
			if(dwa != 0)
				res = max(res, funk(jeden, dwa -1 , trzy, (reszta + 2) % P));
			if(trzy != 0)
				res = max(res, funk(jeden, dwa , trzy-1, (reszta + 3) % P));
		}
		dp[jeden][dwa][trzy][reszta] = res + 1;
	}
	return dp[jeden][dwa][trzy][reszta] - 1;
}
void solve()
{
	vi res = {0, 0, 0};
	for(int i =0 ; i < 101; ++i)
		for(int j = 0; j < 101; ++j)
			for(int k = 0; k < 101; ++k)
				for(int l = 0; l < 4; ++l)
					dp[i][j][k][l] = 0;

	int N;
	int wyn = 0;
	scanf("%d%d", &N, &P);
	for(int i = 0; i < N; ++i)
	{
		int G;
		scanf("%d", &G);
		G %= P;
		if(G == 0)
			++wyn;
		else
			++res[G-1];
	}
	wyn += funk(res[0], res[1], res[2], 0);
	printf("%d\n", wyn);
}
int main()
{
	int T;
	scanf("%d", &T);
	for(int i = 1; i <= T; ++i)
	{
		printf("Case #%d: ", i);
		solve();
		fprintf(stderr, "Rozwiazano %d\n", i);
	}
	
	
	return 0;
}
