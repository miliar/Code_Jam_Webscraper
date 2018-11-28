#pragma warning(disable : 4996)  
#include <stdio.h>
#include <string.h>
#include <stdlib.h>

int main()
{
	int nCases;
	freopen("C:\\Users\\kuhuan\\Downloads\\A-large.in", "r", stdin);
	freopen("A-large", "w", stdout);
	scanf("%d", &nCases);
	for (int caseID = 1; caseID <= nCases; ++caseID)
	{
		char pancakes[1024];
		int k;
		scanf("%s%d", pancakes, &k);
		int n = strlen(pancakes);
		int count = 0;
		for (int i = 0; i + k <= n; ++i)
		{
			if (pancakes[i] == '-')
			{
				for (int j = 0; j < k; ++j)
				{
					if (pancakes[i + j] == '-')
						pancakes[i + j] = '+';
					else
						pancakes[i + j] = '-';
				}
				++count;
			}
		}
		bool isPossible = true;
		for (int i = 0; i < n; ++i)
		{
			if (pancakes[i] != '+')
			{
				isPossible = false;
			}
		}
		if (isPossible)
		{
			printf("Case #%d: %d\n", caseID, count);
		}
		else
		{
			printf("Case #%d: IMPOSSIBLE\n", caseID);
		}
	}
	return 0;
}