#include <algorithm>
#include <iostream>
#include <vector>

using namespace std;

void main()
{
	uint64_t T;
	cin >> T;
	for (uint64_t t = 0; t < T; ++t)
	{
		uint64_t N, K;
		cin >> N;
		cin >> K;

		vector<pair<uint64_t, uint64_t>> counts = { { N , 1 } };

		uint64_t s = 1;
		while (K > s)
		{
			N /= 2;
			K -= s;
			s *= 2;

			static vector<pair<uint64_t, uint64_t>> newCounts;
			newCounts.clear();
			for (const auto& count : counts)
			{
				uint64_t R = count.first / 2;
				uint64_t L = (count.first & 1) ? R : R - 1;
				auto itr = find_if(newCounts.begin(), newCounts.end(), [R](const pair<uint64_t, uint64_t>& newCount) { return newCount.first == R; });
				if  (itr != newCounts.end())
				{
					(*itr).second += count.second;
				}
				else
				{
					newCounts.push_back(make_pair(R, count.second));
				}

				auto itl = find_if(newCounts.begin(), newCounts.end(), [L](const pair<uint64_t, uint64_t>& newCount) { return newCount.first == L; });
				if (itl != newCounts.end())
				{
					(*itl).second += count.second;
				}
				else
				{
					newCounts.push_back(make_pair(L, count.second));
				}
			}
			counts = move(newCounts);
		}

		sort(counts.begin(), counts.end(), [](const pair<uint64_t, uint64_t>& lhs, const pair<uint64_t, uint64_t>& rhs) { return lhs.first > rhs.first; });

		for (const auto& count : counts)
		{
			if (K <= count.second)
			{
				uint64_t R = count.first / 2;
				uint64_t L = (count.first & 1) ? R : R - 1;
				cout << "Case #" << t + 1 << ": " << R << " " << L << endl;
				break;
			}
			K -= count.second;
		}
	}
}
