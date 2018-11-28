/*Bathroom Stalls*/

#include<cstdio>
#include<map>
#include<set>

using namespace std;

int main()
{
	int i, K, left, length, N, right, stall, t, T;
	map< int, set<int> > ranges;
	map< int, set<int> >::reverse_iterator iter;
	freopen("C-small-2-attempt1.in", "r", stdin);
	freopen("C.out", "w", stdout);
	scanf("%d", &T);
	for (t = 1; t <= T; t++)
	{
		scanf("%d %d", &N, &K);
		ranges[N + 1].insert(0);
		for (i = 0; i < K; i++)
		{
			iter = ranges.rbegin();
			length = iter->first;
			left = *((iter->second).begin());
			right = left + length;
			stall = left + (length / 2);
			ranges[length].erase(left);
			if (ranges[length].empty())
				ranges.erase(length);
			ranges[stall - left].insert(left);
			ranges[right - stall].insert(stall);
		}
		printf("Case #%d: %d %d\n", t, right - stall - 1, stall - left - 1);
		ranges.clear();
	}
	return 0;
}