#include <algorithm>
#include <cstdio>
#include <map>
using namespace std;

pair<long long, long long> getPair(long long nStall, long long nPeople)
{
	long long stallSize, stallCnt;
	pair<long long, long long> dividedStall;
	map<long long, long long> stallMap;

	stallMap[nStall] = 1;

	while (1) {
		auto it = stallMap.rbegin();

		stallSize = it->first;
		stallCnt = it->second;

		stallMap.erase(stallSize);

		dividedStall.first = stallSize/2;
		dividedStall.second = (stallSize-1)/2;

		if (nPeople <= stallCnt)
			break;

		nPeople -= stallCnt;

		stallMap[dividedStall.first] += stallCnt; 
		stallMap[dividedStall.second] += stallCnt; 
	}

	return dividedStall;
}

int main()
{
	int tcase;
	long long nStall, nPeople;

	scanf("%d", &tcase);
	for (int i = 1; i <= tcase; ++i) {
		pair<long long, long long> res;
	
		scanf("%lld%lld", &nStall, &nPeople);
		res = getPair(nStall, nPeople);

		printf("Case #%d: %lld %lld\n", i, res.first, res.second);
	}

	return 0;
}
