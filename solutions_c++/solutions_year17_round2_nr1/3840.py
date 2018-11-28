#include <stdio.h>
struct Data
{
	int molecule;
	int denominator;
	float velocity;
};

int main()
{
	int testCase, testCaseCount, len, n, i, start, velocity;
	float value, tmp;
	Data maxData;

	scanf("%d", &testCaseCount);

	for (testCase = 1; testCase <= testCaseCount; testCase++)
	{
		maxData.molecule = 0;
		maxData.denominator = 0;
		maxData.velocity = 0;

		scanf("%d %d", &len, &n);

		for (i = 0; i < n; i++)
		{
			scanf("%d %d", &start, &velocity);
			tmp = (float)((float)(len - start) / (float)velocity);
			if (maxData.velocity < tmp)
			{
				maxData.molecule = len - start;
				maxData.denominator = velocity;
				maxData.velocity = tmp;
			}
		}
		value = (float)(((float)maxData.denominator * len) / (float)maxData.molecule);

		printf("Case #%d: %.6f\n", testCase, value);
	}
	return 0;
}	