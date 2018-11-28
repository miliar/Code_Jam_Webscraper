#include <cstdio>
#include <vector>
#include <string>
#include <algorithm>
#include <map>

using namespace std;

struct NRange
{
	int minN = 0;
	int maxN = 0;

	bool IsValid() const
	{
		return minN > 0 && maxN >= minN;
	}

	bool IsOverlap(const NRange& right)
	{
		return minN <= right.maxN && maxN >= right.minN;
	}
};

NRange CalcNServe(int recipeGram, int gram)
{
	NRange range;
	range.minN = (10 * gram + 11 * recipeGram - 1) / (11 * recipeGram);
	range.maxN = 10 * gram / (9 * recipeGram);

	return range;
}

int Solve1(const vector<int>& serveGrams, const vector<vector<int>>& ingGrams)
{
	int ans = 0;
	
	for (int i = 0; i < (int)ingGrams[0].size(); ++i)
	{
		NRange range = CalcNServe(serveGrams[0], ingGrams[0][i]);
		if (range.IsValid())
		{
			++ans;
		}
	}
	
	return ans;
}

int Solve2(const vector<int>& serveGrams, const vector<vector<int>>& ingGrams)
{
	int N = serveGrams.size();
	int P = ingGrams[0].size();
	vector<vector<NRange>> ranges(N, vector<NRange>(P));
	for (int i = 0; i < N; ++i)
	{
		for (int j = 0; j < P; ++j)
		{
			ranges[i][j] = CalcNServe(serveGrams[i], ingGrams[i][j]);
		}
	}

	vector<int> perm;
	for (int i = 0; i < P; ++i)
	{
		perm.push_back(i);
	}

	int ans = 0;
	
	do
	{
		int localMax = 0;
		
		for (int i = 0; i < P; ++i)
		{
			NRange first = ranges[0][i];
			NRange second = ranges[1][perm[i]];

			if (first.IsOverlap(second))
			{
				++localMax;
			}
		}

		if (localMax > ans)
		{
			ans = localMax;
		}
	} while (next_permutation(perm.begin(), perm.end()));

	return ans;
}

int Solve(const vector<int>& serveGrams, vector<vector<int>>& ingGrams)
{
	if (serveGrams.size() == 1)
	{
		return Solve1(serveGrams, ingGrams);
	}
	else if (serveGrams.size() == 2)
	{
		return Solve2(serveGrams, ingGrams);
	}
	else
	{
		return 0;
	}
}

int main()
{
	int T;
	scanf("%d", &T);
	for (int i = 1; i <= T; ++i)
	{
		int N, P;
		scanf("%d %d", &N, &P);
		
		vector<int> serveGrams(N, 0);
		for (int j = 0; j < N; ++j)
		{
			scanf("%d", &serveGrams[j]);
		}

		vector<vector<int>> ingGrams(N, vector<int>(P, 0));
		for (int j = 0; j < N; ++j)
		{
			for (int k = 0; k < P; ++k)
			{
				scanf("%d", &ingGrams[j][k]);
			}
		}
		
		printf("Case #%d: %d\n", i, Solve(serveGrams, ingGrams));
	}
	
	return 0;
}
