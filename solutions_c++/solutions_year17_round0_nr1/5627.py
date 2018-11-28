#pragma comment(linker, "/STACK:268435456")

#include <algorithm>
#include <iostream>
#include <iomanip>
#include <sstream>
#include <string>
#include <vector>
#include <queue>
#include <set>
#include <map>
#include <cstdio>
#include <cstdlib>
#include <cctype>
#include <cmath>
#include <climits>
#include <numeric>

using namespace std;

void work()
{
	string S;
	int K, countPlus = 0, countMinus;
	cin >> S >> K;

	for (int i = 0; i < S.length(); i++)
	{
		if (S[i] == '+')
			countPlus++;
	}
	countMinus = S.length() - countPlus;

	// Case 1 : All is +, 0 flip
	if (countPlus == S.length())
	{
		printf("0");
		return;
	}

	// Case 2 : N < K
	if (S.length() < K)
	{
		printf("IMPOSSIBLE");
		return;
	}

	// Case 3 : All is -
	if (countMinus == S.length())
	{
		// Case 3.1: K = N, 1 flip
		if (K == S.length())
		{
			printf("1");
			return;
		}
		// Case 3.2: N % K == 0
		else if (S.length() % K == 0)
		{
			printf("%d", S.length() / K);
			return;
		}
		// Case 3.3: N % K != 0
		else
		{
			printf("IMPOSSIBLE");
			return;
		}
	}

	// Case : Only one is -
	if (countMinus == 1)
	{
		printf("IMPOSSIBLE");
		return;
	}

	// Case : number of - < K
/*	if (countMinus < K)
	{
		printf("IMPOSSIBLE");
		return;
	}
*/
	// LOOP
	int minFlips = 0;
	int minFlipsLeft = 0, minFlipsRight = 0;

	string sOriginal = S;
	int countMinusOriginal = countMinus;
	int countPlusOriginal = countPlus;

	// Left check
	for (int i = 0; i < S.length() - K + 1; i++)
	{
		if (S[i] == '-')
		{
			for (int j = i; j < (i + K); j++)
			{
				if (S[j] == '-')
				{
					S[j] = '+';
					countPlus++;
					countMinus--;
				}
				else
				{
					S[j] = '-';
					countPlus--;
					countMinus++;
				}
			}
			minFlips++;
		}

		if (countMinus == 0)
		{
			minFlipsLeft = minFlips;
		}
	}

	minFlips = 0;
	string SR = sOriginal;
	int countMinusR = countMinusOriginal;
	int countPlusR = countPlusOriginal;

	// Right check
	for (int i = SR.length() - 1; i > K - 2; i--)
	{
		if (SR[i] == '-')
		{
			for (int j = i; j > i - K; j--)
			{
				if (SR[j] == '-')
				{
					SR[j] = '+';
					countPlusR++;
					countMinusR--;
				}
				else
				{
					SR[j] = '-';
					countPlusR--;
					countMinusR++;
				}
			}
			minFlips++;

		}

		if (countMinusR == 0)
		{
			minFlipsRight = minFlips;
		}
	}

	if (countMinusR > 0 && countMinus > 0)
	{
		printf("IMPOSSIBLE");
		return;
	}
	else if (countMinus == 0 && countMinusR > 0)
	{
		printf("%d", minFlipsLeft);
		return;
	}
	else if (countMinusR == 0 && countMinus > 0)
	{
		printf("%d", minFlipsRight);
		return;
	}
	else
	{
		if (minFlipsRight <= minFlipsLeft)
			printf("%d", minFlipsRight);
		else
			printf("%d", minFlipsLeft);
		return;
	}
}

int main()
{
	// Paths and filenames
	string name = "A-small";
	string path = "";

	// Open files
	freopen((path + name + ".in").c_str(), "r", stdin);
	freopen((path + name + ".out").c_str(), "w", stdout);

	// Problem solving
	int test_cases;
	scanf("%d", &test_cases);
	for (int test_case = 1; test_case <= test_cases; test_case++)
	{
		printf("Case #%d: ", test_case);
		work();
		printf("\n");
	}

	// Close files
	fclose(stdout);
	fclose(stdin);

	return 0;
}