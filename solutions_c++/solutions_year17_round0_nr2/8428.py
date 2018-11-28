#pragma warning(disable : 4996)  
#include <stdio.h>
#include <string.h>
#include <stdlib.h>


bool isTidy(int x)
{
	int digits[10];
	int length = 0;
	while (x)
	{
		digits[length++] = x % 10;
		x /= 10;
	}
	for (int i = 0; i+1 < length; ++i)
	{
		if (digits[i] < digits[i + 1])
			return false;
	}
	return true;
}

int main()
{
	int nCases;
	freopen("C:\\Users\\kuhuan\\Downloads\\B-small-attempt0.in", "r", stdin);
	freopen("B-small-attempt0.out", "w", stdout);
	scanf("%d", &nCases);
	for (int caseID = 1; caseID <= nCases; ++caseID)
	{
		int N;
		scanf("%d", &N);
		for (int i = N; i >= 1; --i)
		{
			if (isTidy(i))
			{
				printf("Case #%d: %d\n", caseID, i);
				break;
			}
		}
	}
	return 0;
}