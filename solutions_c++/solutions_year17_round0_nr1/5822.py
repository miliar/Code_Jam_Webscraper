#pragma warning(disable:4996)
#include <cstdlib>
#include <cstdio>
#include <vector>
#include <string>
#include <memory.h>
#include <algorithm>

using namespace std;

const char inFileName[] = "A-large.in";
const char outFileName[] = "A-large.out";

const int MAX_N = 1010;

int T, n, k;
char s[MAX_N];
int a[MAX_N];

int solve(int n, int k, char s[])
{
	memset(a, 0, sizeof(a));
	int ret = 0;
	int currSum = 0;
	for (int i = 0; i < n; i++)
	{
		currSum = currSum + a[i];
		if ((s[i] == '-' && currSum % 2 == 0) || (s[i] == '+' && currSum % 2 != 0))
		{
			if (i > (n - 1) - k + 1) 
				return -1;
			ret++;
			currSum++;
			a[i + k] = -1;
		}
	}
	return ret;
}

int main() {

	FILE* inFile = fopen(inFileName, "r");
	FILE* outFile = fopen(outFileName, "w");

	fscanf(inFile, "%d", &T);
	for (int t = 0; t < T; t++)
	{
		fscanf(inFile, "%s %d\n", s, &k);
		n = strlen(s);
		int sol = solve(n, k, s);
		if (sol == -1)
		{
			fprintf(outFile, "Case #%d: IMPOSSIBLE\n", t + 1);
		}
		else
		{
			fprintf(outFile, "Case #%d: %d\n", t + 1, sol);
		}
	}

	fclose(inFile);
	fclose(outFile);
	return 0;
}
