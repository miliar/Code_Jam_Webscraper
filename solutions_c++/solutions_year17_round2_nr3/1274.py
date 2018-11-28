#include <iostream>
#include <cstdint>
#include <string>
#include <limits>
#include <algorithm>
#include <vector>

struct node
{
	int64_t horsePower;
	int64_t horseSpeed;
	std::vector<int64_t> destinationCosts;
};

double solve(const std::vector<node>&graph, uint64_t source, uint64_t dest, int64_t curHorseRemPower, int64_t curHorseSpeed)
{
	if (source == dest)
	{
		return 0; // done
	}

	int dir;
	if (source > dest)
		dir = -1;
	else
		dir = 1;

	double curHorse = std::numeric_limits<double>::max();
	double newHorse = std::numeric_limits<double>::max();
	int64_t destCost = graph[source].destinationCosts[source + dir];

	// try both continuing with our horse or taking the new one
	if (curHorseRemPower >= destCost)
	{
		curHorse = (static_cast<double>(destCost) / static_cast<double>(curHorseSpeed)) + solve(graph, source + dir, dest, curHorseRemPower - destCost, curHorseSpeed);
	}

	if (graph[source].horsePower >= destCost)
	{
		newHorse = (static_cast<double>(destCost) / static_cast<double>(graph[source].horseSpeed)) + solve(graph, source + dir, dest, graph[source].horsePower - destCost, graph[source].horseSpeed);
	}
	
	return std::min(curHorse, newHorse);
}

int main()
{
	uint64_t t, N, Q, source, dest;
	std::cin >> t;
	for (uint64_t i = 1; i <= t; ++i)
	{
		std::cin >> N >> Q;
		std::vector<node> graph(N);
		for (uint64_t j = 0; j < N; ++j)
		{
			std::cin >> graph[j].horsePower >> graph[j].horseSpeed;
		}
		for (uint64_t j = 0; j < N; ++j)
		{
			graph[j].destinationCosts.resize(N);
			for (uint64_t k = 0; k < N; ++k)
			{
				std::cin >> graph[j].destinationCosts[k];
			}
		}

		//Q == 1 for small
		std::cin >> source >> dest;

		std::cout.precision(std::numeric_limits<double>::digits10);
		std::cout << "Case #" << i << ": " << std::fixed << solve(graph,source-1,dest-1, 0, 0) << std::endl;
	}
    return 0;
}