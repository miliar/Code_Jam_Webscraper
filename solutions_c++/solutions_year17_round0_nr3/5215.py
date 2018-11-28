#include <iostream>
#include <queue> 
#include <vector> 
#include <utility> 

typedef std::pair<long long, long long> lrPair;

class PqCompare
{
public:
    bool operator() (const lrPair& lhs, const lrPair& rhs) const
    {
        return lhs.second - lhs.first < rhs.second - rhs.first;
    }
};

int main() {
	std::size_t n;
	std::cin >> n;
	for(std::size_t numCase = 0; numCase < n; ++numCase)
	{
		long long num;
		std::cin >> num;
		long long k;
		std::cin >> k;
		std::priority_queue<lrPair, std::vector<lrPair>, PqCompare> pq;
		pq.push(std::make_pair(0,num+1));
		for(std::size_t i = 1; i < k; ++i)
		{
			auto nextPair = pq.top();
			pq.pop();
			auto left = nextPair.first;
			auto right = nextPair.second;
			long long mid = (right - left) / 2 + left;
			pq.push(std::make_pair(left,mid));
			pq.push(std::make_pair(mid,right));
			
		}
		auto lastPair = pq.top();
		auto left = lastPair.first;
		auto right = lastPair.second;
		long long mid = (right - left) / 2 + left;
		long long minRes = std::min(mid - left, right - mid) - 1;
		long long maxRes = std::max(mid - left, right - mid) - 1;
		std::cout << "Case #" << numCase + 1 << ": " << maxRes << " " << minRes  << std::endl;
	}
	return 0;
}
