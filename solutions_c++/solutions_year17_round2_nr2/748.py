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
int L[10];
int K[10];
char tab[] = "_RYOBVG____";
int chosen;
int dajNajmniejsza(int niew)
{
	int nmin = 0;
	for(int i = 1; i < 8; ++i)
		if((niew & i) == 0 && (K[nmin] < K[i] || (i == chosen && K[i] == K[nmin])))
			nmin = i;
	--K[nmin];
	return nmin;
}
void solve()
{
	int N;
	scanf("%d%d%d%d%d%d%d", &N, L + 1, L + 1 + 2, L + 2, L + 4 + 2, L + 4, L + 4 + 1);
	//printf("%d %d %d %d\n", N, L[1], L[2], L[4]);
	vi res;
	for(int i = 0; i < 8; ++i)
		if(tab[i] != '_' && L[i] != 0)
		{
			chosen = i;
			res = vi();
			res.pb(i);
			for(int j = 0; j < 8; ++j)
				K[j] = L[j];
			--K[i];
			int last = i;
			for(int j = 1; j < N; ++j)
			{
				last = dajNajmniejsza(last);
				res.pb(last);
			}
			bool ok = true;
			for(int j = 1; j < res.size(); ++j)
				if((res[j] & res[j-1]) != 0)
					ok = false;
			if((res[0] & res[N - 1]) != 0)
				ok = false;
			for(int j = 0; j < 8; ++j)
				if(K[j] < 0)
					ok = false;
			if(ok)
			{
				for(int x : res)
					printf("%c", tab[x]);
				puts("");
				return;
			}
			else if(0)
			{
				printf("ODRZUCONA: ");
				for(int x : res)
					printf("%c", tab[x]);
				puts("");
			}
		}
	puts("IMPOSSIBLE");
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
