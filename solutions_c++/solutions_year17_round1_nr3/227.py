#include <cstdio>
#include <map>
#include <algorithm>

using namespace std;

map<long long, int> states;

long long hashVars(int hd, int ad, int hk, int ak)
{
	return (long long)hd * 101 * 101 * 101 + (long long)ad * 101 * 101 + (long long)hk * 101 + (long long)ak;
}

int minMoves(int hd, int ad, int hk, int ak, int b, int d, int h)
{
	if (hk <= 0)
		return 0;
	if (hd <= 0)
		return -1;
	long long curState = hashVars(hd, ad, hk, ak);
	if (!states[curState])
	{
		states[curState] = -1;
		int attack = minMoves(hd - ak, ad, hk - ad, ak, b, d, h);
		int buff = minMoves(hd - ak, min(ad + b, hk), hk, ak, b, d, h);
		int cure = minMoves(h - ak, ad, hk, ak, b, d, h);
		int debuff = minMoves(hd - max(ak - d, 0), ad, hk, max(ak - d, 0), b, d, h);
		int minval = 1000000000;
		if (attack != -1 && attack < minval)
			minval = attack;
		if (buff != -1 && buff < minval)
			minval = buff;
		if (cure != -1 && cure < minval)
			minval = cure;
		if (debuff != -1 && debuff < minval)
			minval = debuff;
		if (minval == 1000000000)
		{
			states[curState] = -1;
		}
		else
		{
			states[curState] = minval + 1;
		}
	}
	return states[curState];
}

int main()
{
	int t;
	scanf("%d", &t);

	int hd, ad, hk, ak, b, d, ret;

	for (int tt = 1; tt <= t; tt++)
	{
		states.clear();
		scanf("%d %d %d %d %d %d", &hd, &ad, &hk, &ak, &b, &d);
		ret = minMoves(hd, ad, hk, ak, b, d, hd);
		printf("Case #%d: ", tt);
		if (ret == -1)
			printf("IMPOSSIBLE\n");
		else
			printf("%d\n", ret);
	}
	return 0;
}
