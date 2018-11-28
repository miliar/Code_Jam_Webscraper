#include <set>
#include <iostream>
#include <utility>

namespace bathroom_stalls
{
std::pair< int, int > solve( int stalls, int people )
{
	std::multiset< int > freeSets;
	freeSets.insert(stalls);
	
	while (people)
	{
		auto it = freeSets.end(); --it;
		
		auto biggestSet = *it - 1 /*ocupy stall!*/;
		int left = biggestSet / 2;
		int right = biggestSet - left;
		if (people == 1)
			return std::make_pair(right, left);

		freeSets.erase(it);
		freeSets.insert(left);
		freeSets.insert(right);
		people -= 1;
	}
	return std::make_pair(0, 0);
}
} // namespace bathroom_stalls
int main()
{
	int cases;
	std::cin >> cases;
	for (int i = 0; i < cases; ++i)
	{
		std::string cakes;
		int stalls = 0;
		int people = 0;
		std::cin >> stalls >> people;
		auto result = bathroom_stalls::solve(stalls, people);
		std::cout << "Case #" << i + 1 << ": " << result.first << " " << result.second << std::endl;
	}
}