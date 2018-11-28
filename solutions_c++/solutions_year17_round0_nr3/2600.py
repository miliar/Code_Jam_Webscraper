#include <iostream>
#include <cstdlib>
#include <vector>
#include <algorithm>
#include <deque>
#include <string>
#include <map>

using namespace std;

#define pb push_back
#define mp make_pair
using ll = long long;
using pii = pair<int, int>;
using pll = pair<ll, ll>;


ll T, N, K, casenum = 1;
map <pll, pll >  M;
pll sol;

pll decompose(ll x)
{
	if (x & 1)
		return mp(x / 2, x / 2);
	else
		return mp(x / 2, x / 2 - 1);
}

int main()
{
	cin >> T;
	while (T--)
	{
		M.clear();
		cin >> N >> K;
		if (K == 1)
			sol = decompose(N);
		else
		{
			K--;
			pll pLLs = decompose(N);
			if (pLLs.first == pLLs.second)
			{
				M[mp(pLLs.first, -1)] = mp(2LL, -1LL);
				pLLs = mp(pLLs.first, -1);
			}
			else
				M[pLLs] = mp(1LL, 1LL);
			
			while (pLLs.first != 1)
			{
				if (pLLs.second == -1 && (pLLs.first & 1))
				{
					M[mp(pLLs.first / 2, -1)] = mp(M[pLLs].first * 2, -1);
					pLLs = mp(pLLs.first / 2, -1);
				}
				else if (pLLs.second == -1)
				{
					M[decompose(pLLs.first)] = mp(M[pLLs].first, M[pLLs].first);
					pLLs = decompose(pLLs.first);
				}
				else if (pLLs.first & 1)
				{
					M[decompose(pLLs.second)] = mp(2 * M[pLLs].first + M[pLLs].second, M[pLLs].second);
					pLLs = decompose(pLLs.second);
				}
				else
				{
					M[decompose(pLLs.first)] = mp(M[pLLs].first, M[pLLs].first + 2 * M[pLLs].second);
					pLLs = decompose(pLLs.first);
				}
			}

			map<pll, pll >::reverse_iterator MIT;

			/*
			ll sum = 0;
			for (auto p : M)
			{
				sum += p.second.first + ((p.first.second == -1 || p.first.second == 0) ? 0 : p.second.second);
			}
			*/

			
			for (MIT = M.rbegin(); MIT != M.rend(); ++MIT)
			{
				pll pLLpLLs = (*MIT).second;
				if (pLLpLLs.second == -1 && pLLpLLs.first >= K)
				{
					sol = decompose((*MIT).first.first);
					break;
				}
				else if (pLLpLLs.second == -1)
					K -= pLLpLLs.first;
				else if (pLLpLLs.first >= K)
				{
					sol = decompose((*MIT).first.first);
					break;
				}
				else if (pLLpLLs.first + pLLpLLs.second >= K)
				{
					sol = decompose((*MIT).first.second);
					break;
				}
				else
					K -= (pLLpLLs.first + pLLpLLs.second);
				
			}
			
		}

		cout << "Case #" << casenum << ": " << sol.first << " " << sol.second << endl;
		casenum++;
	}
	return 0;
}