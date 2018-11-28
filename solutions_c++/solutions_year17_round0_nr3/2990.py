#include <bits/stdc++.h>

using namespace std;

map<long long, long long> mapa;

int main()
{
	int tt, caso = 1;
	scanf("%d", &tt);

	while (tt--)
	{
		mapa.clear();

		long long n, k;
		scanf("%lld %lld", &n, &k);

		mapa.insert({n, 1});
		
		long long i = 0; 
		long long minimo, maximo;
		while (true)
		{
			auto act = *mapa.rbegin();
			//printf("%lld %lld\n", act.first, act.second);

			long long ls = act.first / 2 - (!(act.first & 1));
			long long rs = act.first / 2;
			if (i + act.second >= k)
			{
				minimo = ls;
				maximo = rs;
				break;
			}

			if (ls) mapa[ls] += act.second;
			if (rs) mapa[rs] += act.second;

			i += act.second;

			mapa.erase(act.first);
		}

		printf("Case #%d: %lld %lld\n", caso++, maximo, minimo);
	}
}