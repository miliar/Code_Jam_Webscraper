#pragma warning(disable : 4996)  
#include <stdio.h>
#include <string.h>
#include <stdlib.h>
#include <algorithm>

struct Stall
{
	bool isEmpty;
	int L, R;
	int min()
	{
		return std::min(L, R);
	}
	int max()
	{
		return std::max(L, R);
	}
} stalls[1024];

void updateLR(int n)
{
	int leftmost = 0;
	for (int i = 1; i <= n; ++i)
	{
		stalls[i].L = i - leftmost - 1;
		if (stalls[i].isEmpty == false)
		{
			leftmost = i;
		}
	}
	int rightmost = n+1;
	for (int i = n; i >= 1; --i)
	{
		stalls[i].R = rightmost - i - 1;
		if (stalls[i].isEmpty == false)
		{
			rightmost = i;
		}
	}
}

int main()
{
	int nCases;
	freopen("C:\\Users\\kuhuan\\Downloads\\C-small-1-attempt0.in", "r", stdin);
	freopen("C-small-attempt0.out", "w", stdout);
	scanf("%d", &nCases);
	for (int caseID = 1; caseID <= nCases; ++caseID)
	{
		int N, K;
		scanf("%d%d", &N, &K);
		stalls[0].isEmpty = false;
		stalls[N+1].isEmpty = false;
		for (int i = 1; i <= N; ++i)
		{
			stalls[i].isEmpty = true;
		}
		int candidate = -1;
		while(K-->0)
		{
			updateLR(N);
			candidate = -1;
			for (int i = 1; i <= N; ++i)
			{
				if (stalls[i].isEmpty == false)
				{
					continue;
				}
				if (candidate == -1 || stalls[candidate].min() < stalls[i].min() || stalls[candidate].min() == stalls[i].min() && stalls[candidate].max() < stalls[i].max())
				{
					candidate = i;
				}
			}
			stalls[candidate].isEmpty = false;
		}
		printf("Case #%d: %d %d\n", caseID, std::max(stalls[candidate].L,stalls[candidate].R), std::min(stalls[candidate].L, stalls[candidate].R));
	}
	return 0;
}