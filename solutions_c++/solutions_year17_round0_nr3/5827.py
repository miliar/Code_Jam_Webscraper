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

struct Pair
{
public:
	int left;
	int right;
	int index;

	int min()
	{
		if (left < right)
			return left;
		return right;
	}

	int max()
	{
		if (left > right)
			return left;
		return right;
	}
};

void work()
{
	int N, K;
	cin >> N >> K;

	// Case 1
	if (N == K)
	{
		printf("0 0");
		return;
	}

	// Case 2
	if (K == 1)
	{
		if (N % 2 == 0)
		{
			printf("%d %d", (N / 2), (N / 2) - 1);
		}
		else
		{
			printf("%d %d", (N / 2), (N / 2));
		}
		return;
	}

	vector<int> stalls(N + 2, 0);
	stalls[0] = stalls[N + 1] = 1;

	int leftS, rightS, indLastK, minLastK, maxLastK;
	for (int i = 0; i < K; i++)
	{
		vector<Pair> pairs;
		for (int j = 1; j < N + 2; j++)
		{
			if (stalls[j] == 0)
			{
				leftS = 0;
				rightS = 0;

				for (int k = j - 1; k > 0; k--)
				{
					if (stalls[k] == 0)
						leftS++;
					else
						break;
				}

				for (int k = j + 1; k < N + 1; k++)
				{
					if (stalls[k] == 0)
						rightS++;
					else
						break;
				}

				Pair p;
				p.left = leftS;
				p.right = rightS;
				p.index = j;
				pairs.push_back(p);
			}
		}

		//cout << endl;
		//for (int j = 0; j < pairs.size(); j++)
		//{
		//	cout << "(" << pairs[j].index << ", " << pairs[j].left << ", " << pairs[j].right << ") ";
		//}
		//cout << endl;

		// MAXIMUM of min(Ls, Rs)
		int maxOfMin = 0;
		for (int j = 0; j < pairs.size(); j++)
		{
			if (pairs[j].min() > maxOfMin)
				maxOfMin = pairs[j].min();
		}

		vector<Pair> maxOfMinPairs;
		for (int j = 0; j < pairs.size(); j++)
		{
			if (pairs[j].min() == maxOfMin)
			{
				maxOfMinPairs.push_back(pairs[j]);
			}
		}
		//for (int j = 0; j < maxOfMinPairs.size(); j++)
		//{
		//	cout << "(" << maxOfMinPairs[j].index << ", " << maxOfMinPairs[j].left << ", " << maxOfMinPairs[j].right << ") ";
		//}
		//cout << endl;

		if (maxOfMinPairs.size() == 1)
		{
			stalls[maxOfMinPairs[0].index] = 1;
			minLastK = maxOfMinPairs[0].min();
			maxLastK = maxOfMinPairs[0].max();
			indLastK = maxOfMinPairs[0].index;
		}
		else
		{
			// MAXIMUM of max(Ls, Rs)
			int maxOfMax = 0;
			for (int j = 0; j < maxOfMinPairs.size(); j++)
			{
				if (maxOfMinPairs[j].max() > maxOfMax)
					maxOfMax = maxOfMinPairs[j].max();
			}

			vector<Pair> maxOfMaxPairs;
			for (int j = 0; j < maxOfMinPairs.size(); j++)
			{
				if (maxOfMinPairs[j].max() == maxOfMax)
				{
					maxOfMaxPairs.push_back(maxOfMinPairs[j]);
				}
			}
			//for (int j = 0; j < maxOfMaxPairs.size(); j++)
			//{
			//	cout << "(" << maxOfMaxPairs[j].index << ", " << maxOfMaxPairs[j].left << ", " << maxOfMaxPairs[j].right << ") ";
			//}
			//cout << endl;

			if (maxOfMaxPairs.size() == 1)
			{
				stalls[maxOfMaxPairs[0].index] = 1;
				minLastK = maxOfMaxPairs[0].min();
				maxLastK = maxOfMaxPairs[0].max();
				indLastK = maxOfMinPairs[0].index;
			}
			else
			{
				Pair leftMostPair = maxOfMaxPairs[0];
				for (int j = 0; j < maxOfMaxPairs.size(); j++)
				{
					if (maxOfMaxPairs[j].index < leftMostPair.index)
						leftMostPair = maxOfMaxPairs[j];
				}

				stalls[leftMostPair.index] = 1;
				minLastK = leftMostPair.min();
				maxLastK = leftMostPair.max();
				indLastK = leftMostPair.index;
			}
		}

		//printf("K = %d : %d %d %d\n", i, indLastK, maxLastK, minLastK);
	}

	printf("%d %d", maxLastK, minLastK);
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