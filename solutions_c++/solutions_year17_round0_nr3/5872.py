#include <iostream>
#include <fstream>
#include <string>
#include <vector>
#include <algorithm>


// Simulation - VERY SLOW
void calculate_costs(std::vector<std::pair<long long, long long>>& stalls)
{
	for (size_t idx = 1; idx < (stalls.size() - 1); idx++)
	{
		size_t ridx = (stalls.size() - 1) - idx;

		if (stalls[idx].first != -1)
			stalls[idx].first = stalls[idx - 1].first + 1;
		
		if (stalls[ridx].second != -1)
			stalls[ridx].second = stalls[ridx + 1].second + 1;
	}
}

size_t find_suitable_stall(std::vector<std::pair<long long, long long>>& stalls)
{
	long long maxRS = -1;
	long long maxLS = -1;
	size_t suitable_stall = 0;
	for (size_t idx = 1; idx < (stalls.size() - 1); idx++)
	{
		long long tmin = std::min(stalls[idx].first, stalls[idx].second);
		long long rmin = std::min(maxRS, maxLS);
		if (tmin > rmin)
		{
			maxLS = stalls[idx].first;
			maxRS = stalls[idx].second;
			suitable_stall = idx;
		}
		else if (tmin == rmin)
		{
			long long tmax = std::max(stalls[idx].first, stalls[idx].second);
			long long rmax = std::max(maxRS, maxLS);
			if (tmax > rmax)
			{
				maxLS = stalls[idx].first;
				maxRS = stalls[idx].second;
				suitable_stall = idx;
			}
		}
	}

	return suitable_stall;
}

std::pair<long long, long long> solve1(size_t& N, size_t& K)
{
	std::vector<std::pair<long long, long long>> stalls(N+2);
	stalls[0].first = -1;
	stalls[0].second = -1;
	stalls[N + 1].first = -1;
	stalls[N + 1].second = -1;
	std::pair<long long, long long> cost;
	for (size_t idx = 0; idx < K; idx++)
	{
		calculate_costs(stalls);
		size_t sidx = find_suitable_stall(stalls);
		cost.first = stalls[sidx].first;
		cost.second = stalls[sidx].second;
		stalls[sidx].first = -1;
		stalls[sidx].second = -1;
	}
	return cost;
}

void read_and_solve(std::string fpath)
{
	std::fstream infile;
	std::ofstream outfile;
	infile.open(fpath);
	outfile.open("../resources/res.out");

	if (infile.is_open() && outfile.is_open())
	{
		size_t T;
		size_t N, K;
		infile >> T;
		for (size_t idx = 0; idx < T; idx++)
		{
			infile >> N;
			infile >> K;
			std::pair<long long, long long> cost;
			cost = solve1(N, K);

			outfile << "Case #" << idx + 1 << ": " << std::max(cost.first, cost.second) << " " << std::min(cost.first, cost.second) << std::endl;
		}
		infile.close();
		outfile.close();
	}
	else
	{
		std::cout << "FILE ERROR" << std::endl;
	}
}

int main(int argc, char* argv[])
{
	read_and_solve(argv[1]);
	std::cout << "FINISHED" << std::endl;
	getchar();
	return 0;
}
