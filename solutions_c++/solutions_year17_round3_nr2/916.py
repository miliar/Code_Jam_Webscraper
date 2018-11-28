#include <cstdio>
#include <vector>
#include <string>
#include <algorithm>
#include <map>

using namespace std;

int Solve(vector<pair<int, int>>& Acs, vector<pair<int, int>>& Ajs)
{
	sort(Acs.begin(), Acs.end());
	sort(Ajs.begin(), Ajs.end());
	
	int AcCnt = Acs.size();
	int AjCnt = Ajs.size();

	if (AcCnt == 1 && AjCnt == 0)
	{
		return 2;
	}

	if (AcCnt == 0 && AjCnt == 1)
	{
		return 2;
	}

	if (AcCnt == 1 && AjCnt == 1)
	{
		return 2;
	}

	if (AcCnt == 2 && AjCnt == 0)
	{
		return (1440 + Acs[0].second - Acs[1].first > 720) && (Acs[1].second - Acs[0].first > 720)
			? 4 : 2;
	}

	if (AcCnt == 0 && AjCnt == 2)
	{
		return (1440 + Ajs[0].second - Ajs[1].first > 720) && (Ajs[1].second - Ajs[0].first > 720)
			? 4 : 2;
	}
	
	return 0;
}

int main()
{
	int T;
	scanf("%d", &T);
	for (int i = 1; i <= T; ++i)
	{
		int Ac, Aj;
		scanf("%d %d", &Ac, &Aj);

		vector<pair<int, int>> Acs(Ac), Ajs(Aj);
		for (int j = 0; j < Ac; ++j)
		{
			scanf("%d %d", &Acs[j].first, &Acs[j].second);
		}
		for (int j = 0; j < Aj; ++j)
		{
			scanf("%d %d", &Ajs[j].first, &Ajs[j].second);
		}
		
		printf("Case #%d: %d\n", i, Solve(Acs, Ajs));
	}
	
	return 0;
}
