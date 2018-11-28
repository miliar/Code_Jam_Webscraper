#include <iostream>
#include <string>
#include <vector>
#include <sstream>
#include <cassert>
#include <set>
#include <map>

using namespace std;

std::pair<long long, long long> solve(long long N, long long K)
{
	std::set<long long> used;
	used.insert(0);
	used.insert(N + 1);
	long long bestMin = 0,
				bestMax = 0,
				bestId = -1;
	for (long long k = 0; k < K; ++k)
	{
		bestMin = 0;
		bestMax = 0;
		bestId = -1;
		for (auto L = used.begin(); L != used.end(); ++L)
		{
			auto R = L;
			R++;

			if (R == used.end())
				break;

			auto LB = *L, RB = *R;
			auto diff = RB - LB - 1;
			if (diff < bestMin + bestMax + 1)
				continue;

			auto empty = diff - 1;
			auto left = empty / 2LL;
			auto right = empty - left;
			auto selected = LB + left + 1;
			if (left > bestMin || (left == bestMin && right > bestMax))
			{
				bestMin = left;
				bestMax = right;
				bestId = selected;
			}
		}
		used.insert(bestId);
	}
	return std::make_pair(bestMax, bestMin);
}

std::pair<long long, long long> solve0(long long N, long long K)
{
	std::map<long long, long long> count;
	count[N] = 1;

	long long seated = 0, bestMin = 0, bestMax = 0;
	while (seated < K)
	{
		auto largest = *count.rbegin();
		count.erase(largest.first);

		seated += largest.second;
		auto empty = largest.first - 1LL;
		auto left = empty / 2LL;
		auto right= empty - left;

		bestMin = left;
		bestMax = right;

		count[left] += largest.second;
		count[right] += largest.second;
//		std::cerr << count.size() << " ";
	}
//	std::cerr << std::endl;
	
//	auto sol = solve(N, K);
//	if (sol.first != bestMax || sol.second != bestMin)
//		assert(false);
	return std::make_pair(bestMax, bestMin);
}

int main()
{
	std::ios_base::sync_with_stdio(0);

	int T;
	cin >> T;
	for (int i = 0; i < T; ++i)
	{
		long long N, K;
		cin >> N >> K;
		auto res = solve0(N, K);
		cout << "Case #" << i + 1 << ": " << res.first << " " << res.second << std::endl;
	}
	return 0;
}
