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
int N, C, M;
vi Pla[1100];
int promocji;
bool dasie(int ride)
{
	promocji = 0;
	int odl = 0;
	for(int i = N-1; i >= 0; --i)
	{
		int zajmiejsc = min(ride, (int)Pla[i].size());
		if(zajmiejsc < Pla[i].size())
		{
			odl += Pla[i].size() - zajmiejsc;
			promocji += Pla[i].size() - zajmiejsc;
		}
		else
			odl = max(0, odl - (ride - zajmiejsc));
	}
	//printf("Dasie %d to %d\n", ride, (odl == 0));
	return (odl == 0);
}
void solve()
{
	scanf("%d%d%d", &N, &C, &M);
	for(int i = 0; i < N; ++i)
		Pla[i].clear();
	vi Cust(C, 0);
	for(int i = 0; i < M; ++i)
	{
		int P, B;
		scanf("%d%d", &P, &B);
		--B; --P;
		Pla[P].pb(B);
		++Cust[B];
	}
	int minp = 0;
	for(int y : Cust)
		minp = max(minp, y);
	//printf("b = %d\n", 
	int b = minp-1;
	int e = 10000;
	while(e - b > 1)
	{
		int d = (b + e) / 2;
		if(dasie(d))
			e = d;
		else
			b = d;
	}
	dasie(e);
	printf("%d %d\n", e, promocji);
}
int main()
{
	//solve();
	//return 0;
	
	int T;
	scanf("%d", &T);
	for(int i = 1; i <= T; ++i)
	{
		printf("Case #%d: ", i);
		solve();
	}
	
	
	return 0;
}
