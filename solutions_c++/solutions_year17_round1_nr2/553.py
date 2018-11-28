#define TEST

#ifdef TEST 
#define _CRT_SECURE_NO_WARNINGS
#endif


#include <iostream>
#include <vector>
#include <algorithm>


struct Interval
{
	int from, to;
	bool used;

	bool operator<(const Interval& other) const
	{
		if (from < other.from) return true;
		else if (from > other.from) return false;
		return to < other.to;
	}
};



int needs[55];
int packages[55][55];


int main()
{
#ifdef TEST
	freopen("B-large.in", "r", stdin);
	freopen("B-large.out", "wb", stdout);
#endif

	int numOfTestcases;
	std::cin >> numOfTestcases;

	for (int t = 0; t < numOfTestcases; ++t)
	{
		std::cout << "Case #" << (t + 1) << ": ";

		int numOfItems, numOfPackages;
		std::cin >> numOfItems >> numOfPackages;

		for (int i = 0; i < numOfItems; ++i)
		{
			int a;
			std::cin >> a;
			needs[i] = a;
		}

		for (int i = 0; i < numOfItems; ++i)
		{
			for (int j = 0; j < numOfPackages; ++j)
			{
				int a;
				std::cin >> a;
				packages[i][j] = a;
			}
		}

		std::vector<std::vector<Interval>> intervals(numOfItems, std::vector<Interval>());

		// vegigmegyunk midnegyik termeket
		// es meghatarozzuk a min es max szamot amivel cuccot kepez
		for (int i = 0; i < numOfItems; ++i)
		{
			for (int j = 0; j < numOfPackages; ++j)
			{
				int minCucc = std::ceil((0.9090909090f * packages[i][j]) / needs[i]);
				int maxCucc = std::floor((1.1111111112 * packages[i][j]) / needs[i]);

				if (minCucc <= maxCucc)
				{
					intervals[i].push_back(Interval{ minCucc, maxCucc, false });
				}
			}
		}

		for (int i = 0; i < numOfItems; ++i)
		{
			std::sort(intervals[i].begin(), intervals[i].end());
		}

		/*
		for (int i = 0; i < numOfItems; ++i)
		{
			std::cout << i << ":" << std::endl;
			for (int j = 0; j < intervals[i].size(); ++j)
			{
				std::cout << "\t" << intervals[i][j].from << " " << intervals[i][j].to << std::endl;
			}
		}
		*/

		// vegigmegyunk az elsoben levo dobozokon
		int count = 0;
		for (int i = 0; i < intervals[0].size(); ++i)
		{
			int min = intervals[0][i].from;
			int max = intervals[0][i].to;

			// keresunk part minden masik intervallumbol
			std::vector<Interval*> chosen;
			bool ok = true;
			for (int j = 1; j < numOfItems; ++j)
			{
				bool found = false;
				for (auto& interval : intervals[j])
				{
					if (interval.from <= max && interval.to >= min)
					{
						interval.used = true;
						chosen.push_back(&interval);
						found = true;
						break;
					}
				}
				if (!found)
				{
					ok = false;
					break;
				}
			}
			if (!ok)
			{
				for (auto interval : chosen)
				{
					interval->used = false;
				}
			}
			else
			{
				count++;
			}
		}

		std::cout << count << std::endl;
	}
}